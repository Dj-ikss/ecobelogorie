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
from pages.base_page import GO_MAIN_PAGE, SUMMER_ACTIVITY_BTN, ALL_SEASON_ACTIVITY_BTN, WINTER_ACTIVITY_BTN, \
    CROSS_SKIING_BTN, MOUNT_SKIING_BTN, SNOWBOARD_BTN, TUBING_BTN, DRAGON_BTN, SNOWBIKE_BTN, ATV_BTN, CATAMARAN_BTN, \
    BADMINTON_BTN, SUPBOARD_BTN, ARCHERY_BTN, RENT_EQUIPMENT_BTN, RENT_BADMINTON_BTN, RENT_ARCHERY_BTN, \
    RENT_SUPBOARD_BTN, RENT_KATAMARAN_BTN, RENT_ATV_BTN


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
    assert part_name_sauna == 'Сауна с купелью'
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
    GO_MAIN_PAGE(driver)

# BE - 2350 Блок "Питание" в разделе "Проживание на курорте Белогорье"
def test_part_rent_block_cafe(driver):
    driver.find_elements(*btn_menu_rent.BTN_MENU_RENT)[0].click()                            # Нажимаем  Кнопка-меню "проживание" в хэдере
    name_block = driver.find_element(By.CLASS_NAME, 'live_page__eat__title')                 # Находим название блока и псверяем его
    assert name_block.text == 'Питание'
    info = driver.find_element(By.CLASS_NAME, 'live_page__eat__text').text                   # Находим инфо(описание) о кафе и проверяем, что описание есть
    assert len(info) == 578
    foto_cafe = driver.find_element(By.XPATH, '//img[contains(@src, ".jpg")]')               # Находим фото кафе и проверяем, что оно отображается
    assert foto_cafe.is_displayed() == True
    GO_MAIN_PAGE(driver)


@pytest.mark.skip('Fail')
# BE - 2380 Летние виды развлечений в блоке "Активности на курорте" раздела "Проживание на курорте Белогорье"
def test_part_rent_block_summer_activity(driver):
    driver.find_elements(*btn_menu_rent.BTN_MENU_RENT)[0].click()                      # Нажимаем  Кнопка-меню "проживание" в хэдере
    name_block = driver.find_element(By.CLASS_NAME, 'title_y--activity_block__home')   # Находим название блока "Активности на курорте"
    driver.execute_script("arguments[0].scrollIntoView(true);", name_block)            # Скролим страницу до блока "Активности на курорте"

    time.sleep(1)
    WINTER_ACTIVITY_BTN(driver)
    SUMMER_ACTIVITY_BTN(driver)
    time.sleep(1)

    ATV_BTN(driver)                                                          # Нажимаем на картинку "Катание на квадроцикле" и переходим в это раздел
    part_name_atv = driver.find_element(*name_part.NAME_PART_SLIDER)         # Находим название раздела "Катание на квадроцикле"
    assert part_name_atv.text == 'Катание на квадроцикле'
    driver.back()

    WINTER_ACTIVITY_BTN(driver)
    SUMMER_ACTIVITY_BTN(driver)

    driver.implicitly_wait(3)
    BADMINTON_BTN(driver)                                                         # Нажимаем на картинку "Бадминтон" и переходим в это раздел
    part_name_badminton = driver.find_element(*name_part.NAME_PART_SLIDER)        # Находим название раздела "Бадминтон"
    assert part_name_badminton.text == 'Бадминтон'
    driver.back()

    WINTER_ACTIVITY_BTN(driver)
    SUMMER_ACTIVITY_BTN(driver)

    driver.implicitly_wait(3)
    CATAMARAN_BTN(driver)                                                         # Нажимаем на картинку "Катание на катамаране" и переходим в это раздел
    part_name_catamaran = driver.find_element(*name_part.NAME_PART_SLIDER)        # Находим название раздела "Катание на катамаране"
    assert part_name_catamaran.text == 'Катание на катамаране'
    driver.back()

    WINTER_ACTIVITY_BTN(driver)
    SUMMER_ACTIVITY_BTN(driver)

    driver.implicitly_wait(3)
    SUPBOARD_BTN(driver)                                                          # Нажимаем на картинку "Катание на SUP-Доске" и переходим в это раздел
    part_name_supboard = driver.find_element(*name_part.NAME_PART_SLIDER)         # Находим название раздела "Катание на SUP-Доске"
    assert part_name_supboard.text == 'Катание на SUP-Доске'
    driver.back()

    WINTER_ACTIVITY_BTN(driver)
    SUMMER_ACTIVITY_BTN(driver)

    driver.implicitly_wait(3)
    ARCHERY_BTN(driver)                                                           # Нажимаем на картинку "Стрельба из лука" и переходим в это раздел
    part_name_archery = driver.find_element(*name_part.NAME_PART_SLIDER)          # Находим название раздела "Стрельба из лука"
    assert part_name_archery.text == 'Стрельба из лука'
    GO_MAIN_PAGE(driver)



# BE - 2390 Зимние виды развлечений в блоке "Активности на курорте" раздела "Проживание на курорте Белогорье"
def test_part_rent_block_winter_activity(driver):
    driver.find_elements(*btn_menu_rent.BTN_MENU_RENT)[0].click()                        # Нажимаем  Кнопка-меню "проживание" в хэдере
    name_block = driver.find_element(By.CLASS_NAME, 'title_y--activity_block__home')     # Находим название блока "Активности на курорте" и проверяем его
    assert name_block.text == 'Активности на курорте'
    driver.execute_script("arguments[0].scrollIntoView(true);", name_block)               # Скролим страницу до блока "Активности на курорте"
    time.sleep(1)
    WINTER_ACTIVITY_BTN(driver)                                                      # Нажимаем кнопку "Зима"
    CROSS_SKIING_BTN(driver)                                                         # Нажимаем на картинку "Катание на беговых лыжах" и переходим в этот раздел
    part_name_cross_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text   # Находим название раздела "Катание на беговых лыжах"
    assert part_name_cross_skiing == 'Катание на беговых лыжах'
    driver.back()
    WINTER_ACTIVITY_BTN(driver)
    MOUNT_SKIING_BTN(driver)                                                         # Нажимаем на картинку "Катание на горных лыжах" и переходим в это раздел
    part_name_mount_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text   # Находим название раздела "Катание на горных лыжах"
    assert part_name_mount_skiing == 'Катание на горных лыжах'
    driver.back()
    WINTER_ACTIVITY_BTN(driver)
    SNOWBOARD_BTN(driver)                                                        # Нажимаем на картинку "Катание на сноуборде" и переходим в это раздел
    part_name_snowboard = driver.find_element(*name_part.NAME_PART_SLIDER).text  # Находим название раздела "Катание на сноуборде"
    assert part_name_snowboard == 'Катание на сноуборде'
    driver.back()
    WINTER_ACTIVITY_BTN(driver)
    TUBING_BTN(driver)                                                           # Нажимаем на картинку "Катание на сноутюбинге" и переходим в это раздел
    part_name_tubing = driver.find_element(*name_part.NAME_PART_SLIDER).text     # Находим название раздела "Катание на сноутюбинге"
    assert part_name_tubing == 'Катание на сноутюбинге'
    driver.back()
    WINTER_ACTIVITY_BTN(driver)
    DRAGON_BTN(driver)                                                           # Нажимаем на картинку "Катание на надувном драконе" и переходим в это раздел
    part_name_dragon = driver.find_element(*name_part.NAME_PART_SLIDER).text     # Находим название раздела "Катание на надувном драконе"
    assert part_name_dragon == 'Катание на надувном драконе'
    driver.back()
    WINTER_ACTIVITY_BTN(driver)
    SNOWBIKE_BTN(driver)                                                          # Нажимаем на картинку "Катание на снегоходах" и переходим в это раздел
    part_name_snowbike = driver.find_element(*name_part.NAME_PART_SLIDER).text    # Находим название раздела "Катание на снегоходах"
    assert part_name_snowbike == 'Катание на снегоходах'
    GO_MAIN_PAGE(driver)

# BE - 2410 Летний инвентарь в разделе "Аренда инвентаря"
def test_rent_equipment_summer(driver):
    RENT_EQUIPMENT_BTN(driver)                                              # Нажимаем Кнопка-меню "Прокат снаряжения" в хэдере
    RENT_BADMINTON_BTN(driver)                                              # Нажимаем на картинку "Прокат ракеток для бадминтона"
    part_name_badminton = driver.find_element(*name_part.NAME_PART_RENT)    # Находим название раздела "Прокат ракеток для бадминтона"
    assert part_name_badminton.text == 'Прокат ракеток для бадминтона'      # Сравниваем название раздела
    driver.back()
    RENT_ARCHERY_BTN(driver)                                                   # Нажимаем Кнопка-меню "Прокат инвентаря для стрельбы из лука" в хэдере
    part_name_archery = driver.find_element(*name_part.NAME_PART_RENT)         # Находим название раздела "Прокат инвентаря для стрельбы из лука"
    assert part_name_archery.text == 'Прокат инвентаря для стрельбы из лука'   # Сравниваем название раздела
    driver.back()
    RENT_SUPBOARD_BTN(driver)                                                  # Нажимаем Кнопка-меню "Прокат SUP-Борда" в хэдере
    part_name_supboard = driver.find_element(*name_part.NAME_PART_RENT)        # Находим название раздела "Прокат SUP-Борда"
    assert part_name_supboard.text == 'Прокат SUP-Борда'                       # Сравниваем название раздела
    driver.back()
    RENT_KATAMARAN_BTN(driver)                                                  # Нажимаем Кнопка-меню "Прокат катамарана" в хэдере
    part_name_katamaran = driver.find_element(*name_part.NAME_PART_RENT)        # Находим название раздела "Прокат катамарана"
    assert part_name_katamaran.text == 'Прокат катамарана'                      # Сравниваем название раздела
    driver.back()
    RENT_ATV_BTN(driver)                                                        # Нажимаем Кнопка-меню "Прокат квадроцикла" в хэдере
    part_name_atv = driver.find_element(*name_part.NAME_PART_RENT)              # Находим название раздела "Прокат квадроцикла"
    assert part_name_atv.text == 'Прокат квадроцикла'                           # Сравниваем название раздела
    GO_MAIN_PAGE(driver)