# file: test.py
import time
from pprint import pprint
from web_driver_setup import WebDriverSetup
from selenium.webdriver.common.by import By


def main():
    web_driver_setup = WebDriverSetup()
    driver = web_driver_setup.setup_driver()

    url = f"https://www.ilovepdf.com/ru/word_to_pdf"
    driver.get(url)
    time.sleep(3)
    uploader_button = driver.find_element(By.CSS_SELECTOR, 'a.uploader')
    uploader_button.click()
    time.sleep(3)
    driver.get

if __name__ == "__main__":
   main() 
    
