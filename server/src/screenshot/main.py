import asyncio
import base64
from typing import Optional, Callable

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from cache import cache_image, get_cached_image, clear_cached_image
from config import cache_image_time

driver_options = webdriver.ChromeOptions()

driver_options.add_argument("--headless=new")

driver = webdriver.Chrome(driver_options)
driver.set_window_size(1920, 1227)


def take_screenshot(website: str) -> bytes:
    try:
        driver.get(website)

        return driver.get_screenshot_as_png()
    except WebDriverException as e:
        raise ValueError(f'Not found website: {website}, {str(e)}')


def to_base64(data: bytes) -> str:
    return base64.b64encode(data).decode('utf-8')


async def delayed_call(seconds: int, func: Callable, *args, **kwargs):
    await asyncio.sleep(seconds)

    func(*args, **kwargs)


def get_screenshot(website: str) -> str:
    cache: Optional[bytes] = get_cached_image(website)

    if cache:
        return to_base64(cache)

    data: bytes = take_screenshot(website)

    cache_image(website, data)

    asyncio.create_task(delayed_call(cache_image_time, clear_cached_image, website))

    return to_base64(data)
