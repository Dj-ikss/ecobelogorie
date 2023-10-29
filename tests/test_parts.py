import time
from itertools import count
import datetime
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pages.locators import btn_menu_about, click_btn_menu_about, name_part, btn_menu_what_to_do, btn_menu_rent, \
    btn_rent_equipment, btn_right_side, callback, main_page, footer_btn
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BE - 2300 Раздел "Активности" - кнопки "Лето", "Зима", "Все сезоны"
def test_part_activity_btn_winter_summer_allseason(driver):
    btn_activity = driver.find_element(By.LINK_TEXT, 'Развлечения').get_attribute('href')    # Находим кнопку Развлечения
    driver.get(btn_activity)                                                                 # Переходим по нопке в раздел "Активности"
    part_name = driver.find_element(*name_part.NAME_PART)
    assert part_name.text == 'Активности'
    btn_summer = driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0]
    assert btn_summer.text == 'Лето'
    btn_summer.click()
    driver.implicitly_wait(1)
    all_blocks_summer = driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')
    assert len(all_blocks_summer) == 5
    btn_winter = driver.find_elements(By.CSS_SELECTOR, '*[data-season="winter"]')[0]
    assert btn_winter.text == 'Зима'
    btn_winter.click()
    driver.implicitly_wait(1)
    all_blocks_winter = driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')
    assert len(all_blocks_winter) == 6
    btn_all_seasons = driver.find_elements(By.CSS_SELECTOR, '*[data-season="all_seasons"]')[0]
    assert btn_all_seasons.text == 'Все сезоны'
    btn_all_seasons.click()
    driver.implicitly_wait(1)
    all_blocks_all_seasons = driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')
    assert len(all_blocks_all_seasons) == 8
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru"]').click()              # Переходим на главную страницу по лого

