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

"""Тесты контентной части разделов сайта"""
# BE - 2210 Блок "Галерея" на главной странице
def test_gallery(driver):
    name_part = driver.find_element(*main_page.NAME_MODUL_GALLERY)
    driver.execute_script("arguments[0].scrollIntoView(true);", name_part)
    # WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '*[aria-label="Next"]')))
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '*[aria-label="Next"]').click()
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'slick-prev.slick-arrow').click()
    time.sleep(1)
    foto = driver.find_element(By.CSS_SELECTOR, '*[src="/images/__content/gallery/1.jpg"]').is_displayed()
    driver.find_element(By.CSS_SELECTOR, '*[src="/images/__content/gallery/1.jpg"]').click()
    time.sleep(1)
    play_foto = driver.find_element(By.XPATH, '//*[@id="fancybox-1"]/div[2]/div[2]/button[2]').is_displayed()
    assert name_part.text == 'Галерея'
    assert foto == True
    assert play_foto == True

# BE - 2220 Блок "Проживание" на главной странице      ОШИБКА В НАЗВАНИИ РАЗДЕЛА   Проживание в гостиницЫ  !!!!!!!!!!!
def test_live_rent(driver):
    name_modul = driver.find_element(*main_page.NAME_MODUL_HOME)                  # Находим название блока ПРОЖИВАНИЕ
    driver.execute_script("arguments[0].scrollIntoView(true);", name_modul)       # Скролим страницу до блока Проживание
    assert name_modul.text == 'Проживание'
    # WebDriverWait(driver, 2).until(EC.element_to_be_selected((By.CLASS_NAME, 'living_block__item__inner')))
    time.sleep(1)
    driver.find_elements(By.CLASS_NAME, 'living_block__item__inner')[0].click()   # Находим и нажимаем на картинку для перехода в раздел ДОМА
    name_part_home = driver.find_element(*name_part.NAME_PART).text               # Находим название раздела ДОМА ДЛЯ ПРОЖИВАНИЯ, сравниваем название
    assert name_part_home == 'Дома для проживания'
    driver.back()
    driver.find_elements(By.CLASS_NAME, 'living_block__item__inner')[1].click()  # Находим и нажимаем на картинку для перехода в раздел НОМЕРА (Гостинка)
    name_part_room = driver.find_element(*name_part.NAME_PART).text              # Находим название раздела "Проживание в гостинице", сравниваем название
    assert name_part_room == 'Проживание в гостиницы'      # !!!!!!!!!!!!!!ОШИБКА В НАЗВАНИИ РАЗДЕЛА!!!!!!!!!!!
    driver.back()
    name_parts_on_img = driver.find_elements(By.CLASS_NAME, 'living_block__item__title')  # Находим названия разделов в изображениях блока ПРОЖИВАНИЕ
    assert (name_parts_on_img[0].text, name_parts_on_img[1].text) == ('Дом', 'Номер')