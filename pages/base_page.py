import time
from itertools import count
import datetime
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pages.locators import btn_menu_about, click_btn_menu_about, name_part, btn_menu_what_to_do, btn_menu_rent, \
    btn_rent_equipment, btn_right_side, callback, main_page
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def GO_MAIN_PAGE(driver):
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru"]').click()      # Переходим на главную страницу по лого

"""Раздел АКТИВНОСТИ """
def SUMMER_ACTIVITY_BTN(driver):
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()            # Нажимаем на кнопку "Лето" в разделе "Активности"

def ALL_SEASON_ACTIVITY_BTN(driver):
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="all_seasons"]')[0].click()       # Нажимаем на кнопку "Все сезоны" в разделе "Активности"