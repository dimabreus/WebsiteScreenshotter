from selenium import webdriver

driver_options = webdriver.ChromeOptions()

driver_options.add_argument("--headless=new")

driver = webdriver.Chrome(driver_options)
driver.set_window_size(1920, 1227)


def take_screenshot(website: str) -> str:
    driver.get(website)

    return driver.get_screenshot_as_base64()
