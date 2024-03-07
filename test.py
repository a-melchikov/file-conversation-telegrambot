# file: test.py
import time
import os
from web_driver_setup import WebDriverSetup
from selenium.webdriver.common.by import By


def main():
    web_driver_setup = WebDriverSetup(headless=False)
    driver = web_driver_setup.setup_driver()

    url = "https://www.ilovepdf.com/ru"
    driver.get(url)
    time.sleep(1)

    try:
        tools_items = driver.find_elements(By.CSS_SELECTOR, 'div.tools__item')
        href_items = [element.find_element(By.CSS_SELECTOR, 'a').get_attribute(
            'href') for element in tools_items]
        title_items = [element.find_element(By.CSS_SELECTOR, 'a').get_attribute(
            'title') for element in tools_items]
        description_items = [element.find_element(
            By.CSS_SELECTOR, '.tools__item__content').text for element in tools_items]

        driver.get(url=href_items[6])
        accept_cookies(driver)
        upload_file(driver, os.path.join(os.getcwd(), 'test.docx'))
        convert_file(driver)
        time.sleep(15)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


def accept_cookies(driver):
    try:
        cookie_button = driver.find_element(By.ID, 'okck')
        cookie_button.click()
        time.sleep(5)
    except Exception as e:
        print(f"Error accepting cookies: {e}")


def upload_file(driver, file_path):
    try:
        uploader_button = driver.find_element(
            By.CSS_SELECTOR, 'input[type=file]')
        uploader_button.send_keys(file_path)
        time.sleep(5)
    except Exception as e:
        print(f"Error uploading file: {e}")


def convert_file(driver):
    try:
        convertation_button = driver.find_element(By.ID, 'processTask')
        convertation_button.click()
        time.sleep(15)
    except Exception as e:
        print(f"Error converting file: {e}")


if __name__ == "__main__":
    main()
