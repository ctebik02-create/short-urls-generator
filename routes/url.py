from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from models.schemas import UrlInput, UrlOutput, StatisticOutput
from services.url import random_url
from storage.db import add_link_data, get_link_by_shortcode, get_all_links, clicks_count
from storage.db import delete_link_from_db
from sqlalchemy.exc import IntegrityError


router = APIRouter()


@router.post('/link', response_model=UrlOutput)
def post_link(url_input: UrlInput):
    #convert pydantic URL to str because SQLite cannot store it directly
    original_url = str(url_input.url)
    #test if we have that short code already

    for a in range(10):
        short_code = random_url(5)
        link = get_link_by_shortcode(short_code)
        if link is None:
            try:
                added_link = add_link_data(original_url, short_code)
            except IntegrityError:
                continue
            return added_link
    else:
        raise HTTPException(status_code=500, detail='Internal server error')



@router.get('/links', response_model=list[UrlOutput])
def get_links():
    links = get_all_links()
    if not links:
        raise HTTPException(status_code=404, detail='Links not found')
    return links

@router.get('/link', response_model=UrlOutput)
def get_link_from_shortcode(short_code: str):
    link = get_link_by_shortcode(short_code)
    if link is None:
        raise HTTPException(status_code=404, detail='Short code not found')
    return link

@router.get('/statistic', response_model=StatisticOutput)
def get_statistics(short_code: str):
    link = get_link_by_shortcode(short_code)
    if not link:
        raise HTTPException(status_code=404, detail='Short code not found')
    return link

@router.delete('/delete')
def delete_link(short_code: str):
    result = delete_link_from_db(short_code)
    if not result:
        raise HTTPException(status_code=404, detail='Short code not found')
    return {'status': 'success'}



@router.get('/{short_code}', response_class=RedirectResponse)
def redirect_link(short_code: str):
    #here we count clicks, and also return link object so we can use it for redirect
    link = clicks_count(short_code)

    if link is None:
        raise HTTPException(status_code=404, detail='Short code not found')

    return link.original_url
