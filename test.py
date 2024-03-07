# file: test.py
import time
import os
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
        driver.get(url=href_items[6])
        cookie_button = driver.find_element(
            By.ID, 'okck')
        cookie_button.click()
        time.sleep(5)
        uploader_button = driver.find_element(
            By.CSS_SELECTOR, 'input[type=file]')
        uploader_button.send_keys(f"{os.getcwd()}\\test.docx")
        time.sleep(5)
        convertation_button = driver.find_element(
            By.ID, 'processTask')
        convertation_button.click()
        time.sleep(15)

    except Exception as e:
        print(e)
    driver.quit()


if __name__ == "__main__":
    main()
