from selenium import webdriver
from selenium.common.exceptions import WebDriverException
driver_options = webdriver.ChromeOptions()

driver_options.add_argument("--headless=new")

driver = webdriver.Chrome(driver_options)
driver.set_window_size(1920, 1227)


def take_screenshot(website: str) -> str:
    try:
        driver.get(website)

        return driver.get_screenshot_as_base64()
    except WebDriverException as e:
        raise ValueError(f'Not found website: {website}, {str(e)}')
