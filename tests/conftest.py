import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.fixture(scope="session")  # scope="session"
def driver():
    chrome_driver = webdriver.Chrome()
    link = 'https://ecobelogorie.ru/'
    chrome_driver.get(link)
    chrome_driver.maximize_window()  # макс размер экрана
    # time.sleep(3)
    return chrome_driver
