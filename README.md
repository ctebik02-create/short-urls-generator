URL shortener project, created for making short codes for long URLs or common URLs

With that you can create short code for your URLs
And with that you can check statistics of your short codes, 
and that make possible to manage exists links, for example
you can change link etc.


Stack: Python, SqlAlchemy, FastAPI, Docker, Alembic, PostgreSQL

Prerequisites:

Docker Desktop for Windows and working Docker Engine, Docker Compose

Environment Variables:

DATABASE_URL='postgresql://user:password@localhost:5434/short_urls'

DATABASE_URL_DOCKER='postgresql://user:password@db:5432/short_urls'

You must put it on your .env before start running programm

Installation & Running:

to write in terminal from main app where is docker-compose.yml:

docker compose up --build

^After containers are running you can do database migrations

Database Migrations:

docker compose exec backend alembic upgrade head
- that command run last alembic migration and all before that

API Usage:

POST /link - post new link with json

json example:
```json
{
  "url": "https://example.com/"
}
```
response example:
```json
{
  "original_url": "https://example.com/",
  "short_code": "j1dqz"
}
```
GET /links - get all links

GET /link?short_code=j1dqz
- get link by shortcode

GET /statistic?short_code=j1dqz
- get statistic about link with shortcode

response example:
```json
{
  "original_url": "https://example.com/",
  "clicks": 3,
  "short_code": "j1dqz",
  "condition": true
}
```
DELETE /delete - delete link

PUT /change_original_link - change original link

PUT /change_condition - turn on/off link shortcode

json example:
```json
{
  "short_code": "j1dqz",
  "condition": true

}
```
Condition True - Turn ON, False - Turn OFF.

GET /{your_short_code} - redirect to link

Once the application is running, you can access the API at:

http://localhost:8000/docs - Swagger UI

http://localhost:8000/links - To get all links