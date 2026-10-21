import random
import string

def random_url(size):
    return ''.join(
        random.choice(
            string.ascii_lowercase + string.digits) for _ in range(size)
        )
