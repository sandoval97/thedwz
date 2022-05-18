import asyncio
from concurrent.futures import ThreadPoolExecutor
from requests import Session, get
from django.db import models
from .managers import JokesManager
from django.conf import settings


class Jokes(models.Model):
    url = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    icon_url = models.CharField(max_length=200)

    objects = JokesManager()

    @classmethod
    def fetch_random_joke(cls, session):
        base_url = f'{settings.CHUCKNORRIS_API_URL}/{settings.RANDOM_PREFIX_API}'
        with session.get(base_url) as response:
            return response.json()

    @classmethod
    async def get_jokes_asynchronous(cls):
        with ThreadPoolExecutor(max_workers=15) as executor:
            with Session() as session:
                loop = asyncio.get_event_loop()
                tasks = [
                    loop.run_in_executor(
                        executor,
                        cls.fetch_random_joke,
                        session
                    )
                    for _ in range(0, settings.RANDOM_JOKES_LIMIT)
                ]
                return await asyncio.gather(*tasks)
    
    @classmethod
    def random_jokes(cls):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future = asyncio.ensure_future(cls.get_jokes_asynchronous())
        jokes = loop.run_until_complete(future)
        return jokes

