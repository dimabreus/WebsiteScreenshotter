import os

from dotenv import load_dotenv

load_dotenv()


def getenv(key: str):
    result = os.getenv(key)

    if not result:
        raise RuntimeError(f"{key} is not specified.")

    return result


turnstile_secret_key = getenv('TURNSTILE_SECRET_KEY')
cache_image_folder = getenv('CACHE_IMAGE_FOLDER')
cache_image_time = int(getenv('CACHE_IMAGE_TIME'))
