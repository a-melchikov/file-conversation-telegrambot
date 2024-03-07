# file: test.py
import time
from pprint import pprint
from web_driver_setup import WebDriverSetup
from selenium.webdriver.common.by import By


def main():
    web_driver_setup = WebDriverSetup(headless=False)
    driver = web_driver_setup.setup_driver()

    url = f"https://www.ilovepdf.com/ru"
    driver.get(url)
    time.sleep(1)
    try:
        tools_items = [element for element in driver.find_elements(
            By.CSS_SELECTOR, 'div.tools__item')]
        href_items = [element.find_element(By.CSS_SELECTOR, 'a').get_attribute(
            'href') for element in tools_items]
        title_items = [element.find_element(By.CSS_SELECTOR, 'a').get_attribute(
            'title') for element in tools_items]
        description_items = [element.find_element(
            By.CSS_SELECTOR, '.tools__item__content').text for element in tools_items]
    except Exception as e:
        print(e)
    pprint(description_items)


if __name__ == "__main__":
    main()
