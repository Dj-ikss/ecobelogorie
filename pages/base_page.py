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

from pages.locators import btn_menu_about, click_btn_menu_about, name_part, btn_menu_what_to_do, btn_menu_rent, \
    btn_rent_equipment, btn_right_side, callback

def GO_MAIN_PAGE(driver):
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru"]').click()      # Переходим на главную страницу по лого

"""Раздел АКТИВНОСТИ """
def SUMMER_ACTIVITY_BTN(driver):
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()            # Нажимаем на кнопку "Лето" в разделе "Активности"
def WINTER_ACTIVITY_BTN(driver):
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="winter"]')[0].click()            # Нажимаем на кнопку "Зима" в разделе "Активности"
def ALL_SEASON_ACTIVITY_BTN(driver):
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="all_seasons"]')[0].click()       # Нажимаем на кнопку "Все сезоны" в разделе "Активности"

def CROSS_SKIING_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[2].click()       # Нажимаем на картинку "Катание на беговых лыжах" и переходим в этот раздел
def MOUNT_SKIING_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[4].click()       # Нажимаем на картинку "Катание на горных лыжах" и переходим в это раздел
def SNOWBOARD_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[5].click()       # Нажимаем на картинку "Катание на сноуборде" и переходим в это раздел
def TUBING_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[6].click()       # Нажимаем на картинку "Катание на сноутюбинге" и переходим в это раздел
def DRAGON_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[7].click()       # Нажимаем на картинку "Катание на надувном драконе" и переходим в это раздел
def SNOWBIKE_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[10].click()      # Нажимаем на картинку "Катание на снегоходах" и переходим в это раздел


def ATV_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[0].click()    # Нажимаем на картинку "Катание на квадроцикле" и переходим в это раздел
def BADMINTON_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[1].click()    # Нажимаем на картинку "Бадминтон" и переходим в это раздел
def CATAMARAN_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[3].click()    # Нажимаем на картинку "Катание на катамаране" и переходим в это раздел
def SUPBOARD_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[4].click()  # Нажимаем на изображение "Катание на SUP-Доске"
def ARCHERY_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity__image')[9].click()  # Нажимаем на картинку "Стрельба из лука" и переходим в это раздел


"""Раздел Аренда Инвентаря"""
def RENT_EQUIPMENT_BTN(driver):
    driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0].click()       # Нажимаем Кнопка-меню "Прокат снаряжения" в хэдере
def RENT_EQUIPMENT_WINTER_BTN(driver):
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="winter"]')[0].click()   # Нажимаем на кнопку "Зима" в разделе "Аренда Инвентаря"
def RENT_BADMINTON_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[6].click()               # Нажимаем на картинку "Прокат ракеток для бадминтона"
def RENT_ARCHERY_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[7].click()               # Нажимаем на картинку "Прокат инвентаря для стрельбы из лука"
def RENT_SUPBOARD_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[8].click()               # Нажимаем на картинку "Прокат SUP-Борда"
def RENT_KATAMARAN_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[9].click()               # Нажимаем на картинку "Прокат катамарана"
def RENT_ATV_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[10].click()               # Нажимаем на картинку "Прокат квадроцикла"
def RENT_SNOWBIKE_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[0].click()               # Нажимаем на картинку "Прокат снегохода"
def RENT_TUBING_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[1].click()               # Нажимаем на картинку "Прокат сноутюбинга"
def RENT_DRAGON_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[2].click()               # Нажимаем на картинку "Прокат сноутюбинга"
def RENT_SNOWBOARD_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[3].click()               # Нажимаем на картинку "Прокат сноуборда"

def RENT_CROSS_SKI_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[4].click()           # Нажимаем на картинку "Прокат беговых лыж"
def RENT_MOUNT_SKI_BTN(driver):
    driver.find_elements(By.CLASS_NAME, 'card_activity')[5].click()           # Нажимаем на картинку "Прокат горных лыж"


"""Раздел ГОРНОЛЫЖКА"""
def SKI_RESORT_BTN(driver):
    btn_mountain_ride = driver.find_element(By.LINK_TEXT, 'Горнолыжка')             # Находим кнопку Горнолыжка
    link_btn_mountain_ride = btn_mountain_ride.get_attribute('href')                # Получаем ссылку из этой кнопки
    driver.get(link_btn_mountain_ride)                                              # Переходим по ссылке