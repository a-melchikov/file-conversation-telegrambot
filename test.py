# file: test.py
from time import sleep
import os
from web_driver_setup import WebDriverSetup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

file_name = 'test.docx'


def main():
    web_driver_setup = WebDriverSetup(headless=False)
    driver = web_driver_setup.setup_driver()

    url = "https://www.ilovepdf.com/ru"
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.tools__item')))
        tools_items = driver.find_elements(By.CSS_SELECTOR, 'div.tools__item')
        href_items = [element.find_element(By.CSS_SELECTOR, 'a').get_attribute(
            'href') for element in tools_items]
        title_items = [element.find_element(By.CSS_SELECTOR, 'a').get_attribute(
            'title') for element in tools_items]
        description_items = [element.find_element(
            By.CSS_SELECTOR, '.tools__item__content').text for element in tools_items]

        driver.get(url=href_items[6])
        accept_cookies(driver)
        upload_file(driver, os.path.join(os.getcwd(), file_name))
        convert_file(driver)
        download_file(driver)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()


def accept_cookies(driver):
    try:
        cookie_button = driver.find_element(By.ID, 'okck')
        cookie_button.click()
    except Exception as e:
        print(f"Error accepting cookies: {e}")


def upload_file(driver, file_path):
    try:
        sleep(1)
        uploader_button = driver.find_element(
            By.CSS_SELECTOR, 'input[type=file]')
        uploader_button.send_keys(file_path)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'processTask')))
    except Exception as e:
        print(f"Error uploading file: {e}")


def convert_file(driver):
    try:
        convertation_button = driver.find_element(By.ID, 'processTask')
        convertation_button.click()
    except Exception as e:
        print(f"Error converting file: {e}")


def download_file(driver):
    try:
        WebDriverWait(driver, 120).until(file_downloaded)
        print("File downloaded successfully.")
    except Exception as e:
        print(f"Error downloading file: {e}")


def file_downloaded(driver):
    download_directory = WebDriverSetup.download_directory
    for filename in os.listdir(download_directory):
        if (filename.split('.')[0] == file_name.split('.')[0]) and (filename.split('.')[-1] != 'crdownload'):
            file_path = os.path.join(download_directory, filename)
            return os.path.exists(file_path)
    return False


if __name__ == "__main__":
    main()
