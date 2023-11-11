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
from pages.base_page import GO_MAIN_PAGE, SUMMER_ACTIVITY_BTN, ALL_SEASON_ACTIVITY_BTN

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
    GO_MAIN_PAGE(driver)                                                                          # Переходим на главную страницу по лого

# BE - 2310 Летние виды развлечений в разделе "Активности"
def test_part_activity_summer(driver):
    btn_activity = driver.find_element(By.LINK_TEXT, 'Развлечения').get_attribute('href')    # Находим кнопку Развлечения
    driver.get(btn_activity)                                                                 # Переходим по нопке в раздел "Активности"
    SUMMER_ACTIVITY_BTN(driver)                                                              # Нажимаем на кнопку "Лето"
    driver.implicitly_wait(1)
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[0].click()             # Нажимаем на первое изображение "Катание на квадроцикле"
    part_name_atv = driver.find_element(*name_part.NAME_PART_SLIDER).text                    # Находим в открывшемся окне и сравнием название раздела
    assert part_name_atv == 'Катание на квадроцикле'
    driver.back()
    SUMMER_ACTIVITY_BTN(driver)                                                              # Нажимаем на кнопку "Лето"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[1].click()             # Нажимаем на второе изображение "Бадминтон"
    part_name_badminton = driver.find_element(*name_part.NAME_PART_SLIDER).text              # Находим в открывшемся окне и сравнием название раздела
    assert part_name_badminton == 'Бадминтон'
    driver.back()
    SUMMER_ACTIVITY_BTN(driver)                                                              # Нажимаем на кнопку "Лето"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[2].click()             # Нажимаем на третье изображение "Катание на катамаране"
    part_name_catamaran = driver.find_element(*name_part.NAME_PART_SLIDER).text              # Находим в открывшемся окне и сравнием название раздела
    assert part_name_catamaran == 'Катание на катамаране'
    driver.back()
    SUMMER_ACTIVITY_BTN(driver)                                                              # Нажимаем на кнопку "Лето"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[3].click()             # Нажимаем на изображение "Катание на SUP-Доске"
    part_name_supboard = driver.find_element(*name_part.NAME_PART_SLIDER).text               # Находим в открывшемся окне и сравнием название раздела
    assert part_name_supboard == 'Катание на SUP-Доске'
    driver.back()
    SUMMER_ACTIVITY_BTN(driver)                                                              # Нажимаем на кнопку "Лето"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[4].click()             # Нажимаем на изображение "Стрельба из лука"
    part_name_archery = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим в открывшемся окне и сравнием название раздела
    assert part_name_archery == 'Стрельба из лука'
    GO_MAIN_PAGE(driver)

# BE - 2320 Зимние виды развлечений в разделе "Активности"
def test_part_activity_winter(driver):
    btn_activity = driver.find_element(By.LINK_TEXT, 'Развлечения').get_attribute('href')    # Находим кнопку Развлечения
    driver.get(btn_activity)                                                                 # Переходим по нопке в раздел "Активности"
    driver.implicitly_wait(1)
    """ По умолчанию активна кнопка ЗИМА, отображаются зимние виды развлечений """
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity "]')[0].click()       # Нажимаем на первое изображение "Катание на снегоходах"
    part_name_snowbike = driver.find_element(*name_part.NAME_PART_SLIDER).text          # Находим в открывшемся окне и сравнием название раздела
    assert part_name_snowbike == 'Катание на снегоходах'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity "]')[1].click()       # Нажимаем на первое изображение "Катание на беговых лыжах"
    part_name_cross_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text      # Находим в открывшемся окне и сравнием название раздела
    assert part_name_cross_skiing == 'Катание на беговых лыжах'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity "]')[2].click()       # Нажимаем на первое изображение "Катание на горных лыжах"
    part_name_mount_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text      # Находим в открывшемся окне и сравнием название раздела
    assert part_name_mount_skiing == 'Катание на горных лыжах'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity "]')[3].click()       # Нажимаем на первое изображение "Катание на сноуборде"
    part_name_snowboard = driver.find_element(*name_part.NAME_PART_SLIDER).text         # Находим в открывшемся окне и сравнием название раздела
    assert part_name_snowboard == 'Катание на сноуборде'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity "]')[4].click()       # Нажимаем на первое изображение "Катание на сноутюбинге"
    part_name_tubing = driver.find_element(*name_part.NAME_PART_SLIDER).text            # Находим в открывшемся окне и сравнием название раздела
    assert part_name_tubing == 'Катание на сноутюбинге'
    driver.back()
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity "]')[5].click()       # Нажимаем на первое изображение "Катание на надувном драконе"
    part_name_dragon = driver.find_element(*name_part.NAME_PART_SLIDER).text            # Находим в открывшемся окне и сравнием название раздела
    assert part_name_dragon == 'Катание на надувном драконе'
    GO_MAIN_PAGE(driver)

# BE - 2330 Все сезоны - виды развлечений в разделе "Активности"
def test_part_activity_all_season(driver):
    btn_activity = driver.find_element(By.LINK_TEXT, 'Развлечения').get_attribute('href')    # Находим кнопку Развлечения
    driver.get(btn_activity)                                                                 # Переходим по нопке в раздел "Активности"
    ALL_SEASON_ACTIVITY_BTN(driver)                                                          # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.implicitly_wait(1)
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[0].click()             # Нажимаем на первое изображение "Массаж"
    part_name_massage = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим в открывшемся окне и сравнием название раздела
    assert part_name_massage == 'Массаж'
    driver.back()
    ALL_SEASON_ACTIVITY_BTN(driver)                                                 # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[1].click()    # Нажимаем на первое изображение "Проведение мероприятий в закрытой беседке"
    part_name_pavilion = driver.find_element(*name_part.NAME_PART_SLIDER).text      # Находим в открывшемся окне и сравнием название раздела
    assert part_name_pavilion == 'Проведение мероприятий в закрытой беседке'
    driver.back()
    ALL_SEASON_ACTIVITY_BTN(driver)                                                      # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[2].click()         # Нажимаем на первое изображение "Проведение мероприятий в открытой беседке"
    part_name_open_pavilion = driver.find_element(*name_part.NAME_PART_SLIDER).text      # Находим в открывшемся окне и сравнием название раздела
    assert part_name_open_pavilion == 'Проведение мероприятий в открытой беседке'
    driver.back()
    ALL_SEASON_ACTIVITY_BTN(driver)                                                      # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[3].click()         # Нажимаем на первое изображение "Посещение сауны"
    part_name_sauna = driver.find_element(*name_part.NAME_PART_SLIDER).text              # Находим в открывшемся окне и сравнием название раздела
    assert part_name_sauna == 'Посещение сауны'
    driver.back()
    ALL_SEASON_ACTIVITY_BTN(driver)                                                      # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[4].click()         # Нажимаем на первое изображение "Проведение презентаций и пресс-конференций"
    part_name_presentation = driver.find_element(*name_part.NAME_PART_SLIDER).text       # Находим в открывшемся окне и сравнием название раздела
    assert part_name_presentation == 'Проведение презентаций и пресс-конференций'
    driver.back()
    ALL_SEASON_ACTIVITY_BTN(driver)                                                      # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[5].click()         # Нажимаем на первое изображение "Проведение банкетов, выпускных, корпоративов"
    part_name_paty = driver.find_element(*name_part.NAME_PART_SLIDER).text               # Находим в открывшемся окне и сравнием название раздела
    assert part_name_paty == 'Проведение банкетов, выпускных, корпоративов'
    driver.back()
    ALL_SEASON_ACTIVITY_BTN(driver)                                                      # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")             # Скролим страницу в нижнюю часть
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[6].click()         # Нажимаем на первое изображение "Русская баня"
    part_name_bathhouse = driver.find_element(*name_part.NAME_PART_SLIDER).text          # Находим в открывшемся окне и сравнием название раздела
    assert part_name_bathhouse == 'Русская баня'
    driver.back()
    ALL_SEASON_ACTIVITY_BTN(driver)                                                      # Нажимаем на кнопку "Все сезоны" в разделе "Активности"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")             # Скролим страницу в нижнюю часть
    driver.find_elements(By.CSS_SELECTOR, '*[class="card_activity"]')[7].click()         # Нажимаем на первое изображение "Посещение белогорского монастыря"
    part_name_monastery = driver.find_element(*name_part.NAME_PART_SLIDER).text          # Находим в открывшемся окне и сравнием название раздела
    assert part_name_monastery == 'Посещение белогорского монастыря'
    GO_MAIN_PAGE(driver)

# BE - 2340 Блок "Проживание" в разделе "Проживание на курорте Белогорье"
def test_part_rent_block_home_and_room(driver):
    driver.find_elements(*btn_menu_rent.BTN_MENU_RENT)[0].click()                            # Нажимаем  Кнопка-меню "проживание" в хэдере
    name_block = driver.find_element(By.CLASS_NAME, 'title_y--living_block__live')           # Находим название блока "Проживание" и проверяем название
    assert name_block.text == 'Проживание'
    name_block_home = driver.find_elements(By.CLASS_NAME, 'living_block__item__title')[0]    # Находим название изображения с домом и проверяем название
    assert name_block_home.text == 'Дом'
    btn_home = driver.find_elements(By.CLASS_NAME, 'living_block__item')[0].get_attribute('href')   # Нажимаем/переходим по изображению "Дом" в раздел "Дома"
    driver.get(btn_home)
    name_part_rent_house = driver.find_element(*name_part.NAME_PART).text                    # Находим название открывшегося раздела
    assert name_part_rent_house == 'Дома для проживания'
    driver.back()
    name_block_room = driver.find_elements(By.CLASS_NAME, 'living_block__item__title')[1]    # Находим название изображения с номером и проверяем название
    assert name_block_room.text == 'Номер'
    btn_room = driver.find_elements(By.CLASS_NAME, 'living_block__item')[1].get_attribute('href')  # Нажимаем/переходим по изображению "Номер"
    driver.get(btn_room)
    name_part_rent_room = driver.find_element(*name_part.NAME_PART).text                      # Находим название открывшегося раздела "Проживание в гостинице"
    assert name_part_rent_room == 'Проживание в гостинице'
    GO_MAIN_PAGE()

# BE - 2350 Блок "Питание" в разделе "Проживание на курорте Белогорье"


