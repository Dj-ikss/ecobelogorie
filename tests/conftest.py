import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.locators import btn_right_side


@pytest.fixture(scope="session")  # scope="session"
def driver():
    chrome_driver = webdriver.Chrome()
    link = 'https://ecobelogorie.ru/'
    chrome_driver.get(link)
    chrome_driver.maximize_window()  # макс размер экрана
    # time.sleep(3)
    return chrome_driver


@pytest.fixture(scope="function")
def open_callback(driver):
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru"]').click()   # Нажимаем по Лого, для перехода к главной странице
    driver.find_element(*btn_right_side.BTN_CALLBACK).click()            # Находим кнопку "Обратный звонок", нажимаем
    yield
    driver.find_element(By.CLASS_NAME, 'carousel__button.is-close').click()  # Находим кнопку и закрываем форму "Оставить заявку"
