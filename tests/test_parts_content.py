import time
from itertools import count
import datetime
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from pages.base_page import CROSS_SKIING_BTN, MOUNT_SKIING_BTN, SNOWBOARD_BTN, TUBING_BTN, DRAGON_BTN, SNOWBIKE_BTN, \
    ATV_BTN, SUPBOARD_BTN, CATAMARAN_BTN, BADMINTON_BTN, ARCHERY_BTN
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
    close_foto = driver.find_element(By.CSS_SELECTOR, '*[title="Close"]')
    assert name_part.text == 'Галерея'
    assert foto == True
    assert close_foto.is_displayed() == True
    close_foto.click()

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

# BE - 2240 Переключатель "Зима" , "Лето" в блоке  "Активности на курорте"
def test_switch_summer_winter(driver):
    name_modul = driver.find_element(*main_page.NAME_MODUL_ACTIVITY)             # Находим название блока "Активности на курорте"
    driver.execute_script("arguments[0].scrollIntoView(true);", name_modul)      # Скролим страницу до блока "Активности на курорте"
    assert name_modul.text == 'Активности на курорте'
    time.sleep(1)
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()  # Нажимаем кнопку "Лето" в блоке "Активности на курорте"
    driver.implicitly_wait(1)
    summer_activity = driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')    # Находим карточку летнего вида спорта и сравниваем их кол-во на странице
    assert len(summer_activity) == 5
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="winter"]')[0].click()  # Нажимаем кнопку "Зима" в блоке "Активности на курорте"
    driver.implicitly_wait(1)
    summer_activity = driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')    # Находим карточку зимнего вида спорта и сравниваем их кол-во на странице
    assert len(summer_activity) == 6

# BE - 2250 Разделы зимних видов развлечений в блоке "Активности на курорте"
def test_parts_of_winter_activity(driver):
    name_modul = driver.find_element(*main_page.NAME_MODUL_ACTIVITY)             # Находим название блока "Активности на курорте"
    driver.execute_script("arguments[0].scrollIntoView(true);", name_modul)      # Скролим страницу до блока "Активности на курорте"
    time.sleep(1)
    CROSS_SKIING_BTN(driver)                                                        # Нажимаем на картинку "Катание на беговых лыжах" и переходим в это раздел
    part_name_cross_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text  # Находим название раздела "Катание на беговых лыжах"
    assert part_name_cross_skiing == 'Катание на беговых лыжах'
    driver.back()
    MOUNT_SKIING_BTN(driver)                                                        # Нажимаем на картинку "Катание на горных лыжах" и переходим в это раздел
    part_name_mount_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text  # Находим название раздела "Катание на горных лыжах"
    assert part_name_mount_skiing == 'Катание на горных лыжах'
    driver.back()
    SNOWBOARD_BTN(driver)                                                        # Нажимаем на картинку "Катание на сноуборде" и переходим в это раздел
    part_name_snowboard = driver.find_element(*name_part.NAME_PART_SLIDER).text  # Находим название раздела "Катание на сноуборде"
    assert part_name_snowboard == 'Катание на сноуборде'
    driver.back()
    TUBING_BTN(driver)                                                           # Нажимаем на картинку "Катание на сноутюбинге" и переходим в это раздел
    part_name_tubing = driver.find_element(*name_part.NAME_PART_SLIDER).text     # Находим название раздела "Катание на сноутюбинге"
    assert part_name_tubing == 'Катание на сноутюбинге'
    driver.back()
    DRAGON_BTN(driver)                                                           # Нажимаем на картинку "Катание на надувном драконе" и переходим в это раздел
    part_name_dragon = driver.find_element(*name_part.NAME_PART_SLIDER).text     # Находим название раздела "Катание на надувном драконе"
    assert part_name_dragon == 'Катание на надувном драконе'
    driver.back()
    SNOWBIKE_BTN(driver)                                                          # Нажимаем на картинку "Катание на снегоходах" и переходим в это раздел
    part_name_snowbike = driver.find_element(*name_part.NAME_PART_SLIDER).text    # Находим название раздела "Катание на снегоходах"
    assert part_name_snowbike == 'Катание на снегоходах'
    driver.back()

# BE - 2260 Разделы летних развлечений в блоке "Активности на курорте"
def test_parts_of_summer_activity(driver):
    name_modul = driver.find_element(*main_page.NAME_MODUL_ACTIVITY)             # Находим название блока "Активности на курорте"
    driver.execute_script("arguments[0].scrollIntoView(true);", name_modul)      # Скролим страницу до блока "Активности на курорте"
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[5]/div[3]/div[2]/a[2]').click()
    # driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()   # Нажимаем кнопку "Лето" в блоке "Активности на курорте"
    driver.implicitly_wait(3)
    ATV_BTN(driver)                                                               # Нажимаем на картинку "Катание на квадроцикле" и переходим в это раздел
    part_name_atv = driver.find_element(*name_part.NAME_PART_SLIDER)              # Находим название раздела "Катание на квадроцикле"
    assert part_name_atv.text == 'Катание на квадроцикле'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()   # Нажимаем кнопку "Лето" в блоке "Активности на курорте"
    driver.implicitly_wait(3)
    BADMINTON_BTN(driver)                                                         # Нажимаем на картинку "Бадминтон" и переходим в это раздел
    part_name_badminton = driver.find_element(*name_part.NAME_PART_SLIDER)        # Находим название раздела "Бадминтон"
    assert part_name_badminton.text == 'Бадминтон'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()   # Нажимаем кнопку "Лето" в блоке "Активности на курорте"
    driver.implicitly_wait(3)
    CATAMARAN_BTN(driver)                                                         # Нажимаем на картинку "Катание на катамаране" и переходим в это раздел
    part_name_catamaran = driver.find_element(*name_part.NAME_PART_SLIDER)        # Находим название раздела "Катание на катамаране"
    assert part_name_catamaran.text == 'Катание на катамаране'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()   # Нажимаем кнопку "Лето" в блоке "Активности на курорте"
    driver.implicitly_wait(3)
    SUPBOARD_BTN(driver)                                                          # Нажимаем на картинку "Катание на SUP-Доске" и переходим в это раздел
    part_name_supboard = driver.find_element(*name_part.NAME_PART_SLIDER)         # Находим название раздела "Катание на SUP-Доске"
    assert part_name_supboard.text == 'Катание на SUP-Доске'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[data-season="summer"]')[0].click()   # Нажимаем кнопку "Лето" в блоке "Активности на курорте"
    driver.implicitly_wait(3)
    ARCHERY_BTN(driver)                                                           # Нажимаем на картинку "Стрельба из лука" и переходим в это раздел
    part_name_archery = driver.find_element(*name_part.NAME_PART_SLIDER)          # Находим название раздела "Стрельба из лука"
    assert part_name_archery.text == 'Стрельба из лука'
    driver.back()

# BE - 2280 Кнопка "Все новости" блока "Новости" на главное странице
def test_btn_all_news(driver):
    name_modul = driver.find_element(*main_page.NAME_MODUL_NEWS)                      # Находим название блока "Новости" на гл.странице
    driver.execute_script("arguments[0].scrollIntoView(true);", name_modul)           # Скролим страницу до блока "Новости"
    assert name_modul.text == 'Новости'
    time.sleep(1)
    btn_all_news = driver.find_elements(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/blog"]')[1]    # Находим кнопку "Все новости"
    assert btn_all_news.text == 'Все новости'
    btn_all_news.click()                                                                                 # Нажимаем кнопку "Все новости"
    part_name_news = driver.find_element(*name_part.NAME_PART)                                           # Находим название раздела и проверяем его
    assert part_name_news.text == 'Новости'
    driver.back()

# BE - 2290 Переход в статью новости из блока "Новости" на главной странице.
def test_news(driver):
    name_modul = driver.find_element(*main_page.NAME_MODUL_NEWS)                      # Находим название блока "Новости" на гл.странице
    driver.execute_script("arguments[0].scrollIntoView(true);", name_modul)           # Скролим страницу до блока "Новости"
    time.sleep(2)
    news_first = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[6]/div[2]/div/div[1]/div/div[2]/a').text  # Название первой новости
    driver.find_elements(By.CLASS_NAME, 'news__item')[0].click()                      # Находим и нажимаем на первую новость в блоке "Новости"
    name_news_of_part = driver.find_element(By.CLASS_NAME, 'single__content__text__preview').text   # Находим название открывшейся новости
    assert news_first == name_news_of_part
    driver.back()
    news_last = driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[6]/div[2]/div/div[4]/div/div[2]/a').text   # Название последней новости
    time.sleep(2)
    driver.find_elements(By.CLASS_NAME, 'news__item')[3].click()                      # Находим и нажимаем на последнюю новость в блоке "Новости"
    name_news_of_part = driver.find_element(By.CLASS_NAME, 'single__content__text__preview').text  # Находим название открывшейся новости
    assert news_last == name_news_of_part
    driver.back()

