import time
from itertools import count

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from pages.locators import btn_menu_about, click_btn_menu_about, name_part, btn_menu_what_to_do, btn_menu_rent, \
    btn_rent_equipment, btn_right_side, callback
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BE - 1001 Лого "Белогорье экокурорт"
def test_main_logo(driver):       # Лого
    main_logo = driver.find_element(By.CSS_SELECTOR, '*[alt="main logo"]').size                # Находим лого и размер картинки
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/price"]').click()    # Переходим в раздел цена
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru"]').click()          # Пееходим на главную страницу по Лого
    main_slogan = driver.find_element(By.CLASS_NAME, 'home_promo__slide__title').text          # Находим слоган на главной странице
    assert main_logo == {'height': 89, 'width': 83}     # Сравниваем размер картинки Лого
    assert main_slogan == 'Экокурорт Белогорье'         # Сверяем, что главная страница загрузилась и слоган совпадает

# BE - 1002 Кнопка "О нас"
def test_menu_about_us(driver):   # Кнопка меню "О нас"
    btn_menu_about_us = driver.find_element(*btn_menu_about.BTN_ABOUT).text       # Находим название кнопки
    assert btn_menu_about_us == 'О нас'                                           # Проверяем название кнопки

# BE - 1003 Раздел "О базе отдыха" в меню "О нас"
def test_menu_about_us_about_hotel(driver):     # Кнопка "О базе отдыха" в меню "О нас"
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()                        # Нажимаем кнопку меню "О нас"
    btn_about_hotel = driver.find_element(*btn_menu_about.BTN_HOTEL).text         # Находим кнопку "О базе отдыха", получаем название
    driver.find_element(*btn_menu_about.BTN_HOTEL).click()                        # Нажимаем кнопку "О базе отдыха"
    promo_slide = driver.find_element(*name_part.NAME_PART_RESORT).text          # Находим название раздела
    assert btn_about_hotel == 'О базе отдыха'
    assert promo_slide == 'Всесезонный курорт «Белогорье»'

# BE - 1004 Раздел "Горнолыжный комплекс" в меню "О нас"
def test_menu_about_us_about_ski(driver):       # Кнопка "Горнолыжный комплекс" в меню "О нас"
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()                      # Нажимаем кнопку меню "О нас"
    btn_about_ski = driver.find_element(*btn_menu_about.BTN_SKI).text           # Находим кнопку "Горнолыжный комплекс", получаем название
    driver.find_element(*btn_menu_about.BTN_SKI).click()                        # Нажимаем кнопку "Горнолыжный комплекс"
    name_part_ski = driver.find_element(*name_part.NAME_PART_SKI).text         # Находим название раздела
    assert btn_about_ski == 'Горнолыжный комплекс'
    assert name_part_ski == 'Горнолыжный комплекс Белогорье'

# BE - 1005 Раздел "Питание" в меню "О нас"
@pytest.mark.skip('Раздел в разработке')
def test_menu_about_us_about_cafe(driver):       # Кнопка "Питание" в меню "О нас"
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()                       # Нажимаем кнопку меню "О нас"
    btn_cafe = driver.find_element(*btn_menu_about.BTN_CAFE).text                # Находим кнопку "Питание", получаем название
    driver.find_element(*btn_menu_about.BTN_CAFE).click()                        # Нажимаем кнопку "Питание"
    name_part_cafe = driver.find_element(*name_part.NAME_PART).text        # Находим название раздела
    assert btn_cafe == 'Питание'
    assert name_part_cafe == 'Питание на курорте "Белогорье"'

# BE - 1006 Раздел "Акции" в меню "О нас"
@pytest.mark.skip('Раздел в разработке')
def test_menu_about_us_sale(driver):            # Кнопка "Акции" в меню "О нас"
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()                       # Нажимаем кнопку меню "О нас"
    btn_sale = driver.find_element(*btn_menu_about.BTN_SALE).text                # Находим кнопку "Акции", получаем название
    driver.find_element(*btn_menu_about.BTN_SALE).click()                        # Нажимаем кнопку "Акции"
    name_part_sale = driver.find_element(*name_part.NAME_PART).text        # Находим название раздела
    assert btn_sale == 'Акции'
    assert name_part_sale == 'Акции  скидки'

# BE - 1007 Раздел "Новости" в меню "О нас"
def test_menu_about_us_news(driver):             # Кнопка "Новости" в меню "О нас"
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()                       # Нажимаем кнопку меню "О нас"
    btn_news = driver.find_element(*btn_menu_about.BTN_NEWS).text                # Находим кнопку "Новости", получаем название
    driver.find_element(*btn_menu_about.BTN_NEWS).click()                        # Нажимаем кнопку "Новости"
    name_part_news = driver.find_element(*name_part.NAME_PART).text         # Находим название раздела
    assert btn_news == 'Новости'
    assert name_part_news == 'Новости'

# BE - 1008 Раздел "Ответы на вопросы" в меню "О нас"
@pytest.mark.skip('Раздел в разработке')
def test_menu_about_us_faq(driver):             # Кнопка "Ответы на вопросы" в меню "О нас"
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()                   # Нажимаем кнопку меню "О нас"
    btn_faq = driver.find_element(*btn_menu_about.BTN_FAQ).text              # Находим кнопку "Ответы на вопросы", получаем название
    driver.find_element(*btn_menu_about.BTN_FAQ).click()                     # Нажимаем кнопку "Ответы на вопросы"
    name_part_faq = driver.find_element(*name_part.NAME_PART).text      # Находим название раздела
    assert btn_faq == 'Ответы на вопросы'
    assert name_part_faq == 'Ответы на вопросы'

# BE - 1009 Раздел "Карта" в меню "О нас"
def test_menu_about_us_map(driver):             # Кнопка "Карта" в меню "О нас"
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()                 # Нажимаем кнопку меню "О нас"
    btn_map = driver.find_element(*btn_menu_about.BTN_MAP).text            # Находим кнопку "Карта", получаем название
    driver.find_element(*btn_menu_about.BTN_MAP).click()                   # Нажимаем кнопку "Карта"
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'title_x'))) # Явное ожидание
    name_part_map = driver.find_element(*name_part.NAME_PART).text     # Находим название открывшегося раздела
    assert btn_map == 'Карта'
    assert name_part_map == 'Карта курорта «Белогорье»'

# BE - 1010 Кнопка "График работы"
def test_menu_hour_work(driver):
    btn_hour_work = driver.find_element(*btn_menu_about.BTN_HOUR_WORK)           # Находим кнопку "График работы"
    assert btn_hour_work.text == 'График работы'                                 # Получаем название кнопки и проверяем его
    btn_hour_work.click()                                                        # Нажимаем кнопку "График работы"
    info_hour_work = driver.find_element(*name_part.NAME_PART).text    # Находим название открывшегося раздела
    assert info_hour_work == 'Часы работы'

# BE - 1011 Кнопка "Галерея"
def test_menu_gallery(driver):        # Галерея
    btn_gallery = driver.find_element(*btn_menu_about.BTN_GALLERY)              # Находим кнопку "Галерея"
    assert btn_gallery.text == 'Галерея'                                        # Получаем название кнопки и проверяем его
    btn_gallery.click()                                                         # Нажимаем кнопку "Галерея"
    name_part_gallery = driver.find_element(*name_part.NAME_PART).text  # Находим название открывшегося раздела
    assert name_part_gallery == 'Галерея'

# BE - 1012 Кнопка "Контакты"
def test_menu_contacts(driver):        # Контакты
    btn_contacts = driver.find_element(*btn_menu_about.BTN_CONTACTS)               # Находим кнопку "Контакты"
    assert btn_contacts.text == 'Контакты'                                         # Получаем название кнопки и проверяем его
    btn_contacts.click()                                                           # Нажимаем кнопку "Контакты"
    name_part_contacts = driver.find_element(*name_part.NAME_PART).text   # Находим название открывшегося раздела
    assert name_part_contacts == 'Контакты'

# BE - 1013 Кнопка-меню "Чем заняться"
def test_menu_what_to_do(driver):    # Чем заняться
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]          # Находим кнопку-меню "Чем заняться"
    assert btn_what_to_do.text == 'Чем заняться'                                       # Получаем название кнопки и проверяем его
    btn_what_to_do.click()                                                             # Нажимаем кнопку-меню "Чем заняться"
    name_part_activity = driver.find_element(*name_part.NAME_PART).text                # Находим название открывшегося раздела
    assert name_part_activity == 'Активности'

# BE - 1015 Раздел "Катание на беговых лыжах" в меню "Чем заняться"
def test_menu_what_to_do_winter_cross_skiing(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]               # Кнопка "Чем заняться"
    btn_winter = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[0]                  # Кнопка "Зимний сезон"
    btn_cross_skiing = driver.find_elements(*btn_menu_what_to_do.BTN_CROSS_SKIING)[0]      # Кнопка "Катание на беговых лыжах"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_winter).click(btn_cross_skiing).perform()
    name_part_cross_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text
    assert name_part_cross_skiing == 'Катание на беговых лыжах'

# BE - 1016 Раздел "Катание на горных лыжах" в меню "Чем заняться"
def test_menu_what_to_do_winter_mount_skiing(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_winter = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[0]              # Кнопка "Зимний сезон"
    btn_mount_skiing = driver.find_elements(*btn_menu_what_to_do.BTN_MOUNT_SKIING)[0]  # Кнопка "Катание на горных лыжах"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_winter).click(btn_mount_skiing).perform()
    name_part_mount_skiing = driver.find_element(*name_part.NAME_PART_SLIDER).text
    assert name_part_mount_skiing == 'Катание на горных лыжах'

# BE - 1017 Раздел "Катание на сноуборде" в меню "Чем заняться"
def test_menu_what_to_do_winter_snowboard(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_winter = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[0]              # Кнопка "Зимний сезон"
    btn_snowboard = driver.find_elements(*btn_menu_what_to_do.BTN_SNOWBOARD)[0]        # Кнопка "Катание на сноуборде"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_winter).click(btn_snowboard).perform()
    name_part_snowboard = driver.find_element(*name_part.NAME_PART_SLIDER).text
    assert name_part_snowboard == 'Катание на сноуборде'

# BE - 1018 Раздел "Катание на сноутюбинге" в меню "Чем заняться"
def test_menu_what_to_do_winter_tubing(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]         # Кнопка "Чем заняться"
    btn_winter = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[0]              # Кнопка "Зимний сезон"
    btn_tubing = driver.find_elements(*btn_menu_what_to_do.BTN_TUBING)[0]        # Кнопка "Катание на сноутюбинге"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_winter).click(btn_tubing).perform()
    name_part_tubing = driver.find_element(*name_part.NAME_PART_SLIDER).text
    assert name_part_tubing == 'Катание на сноутюбинге'

# BE - 1019 Раздел "Катание на надувном драконе" в меню "Чем заняться"
def test_menu_what_to_do_winter_dragon(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]        # Кнопка "Чем заняться"
    btn_winter = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[0]              # Кнопка "Зимний сезон"
    btn_dragon = driver.find_elements(*btn_menu_what_to_do.BTN_DRAGON)[0]              # Кнопка "Катание на надувном драконе"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_winter).click(btn_dragon).perform()
    name_part_dragon = driver.find_element(*name_part.NAME_PART_SLIDER).text
    assert name_part_dragon == 'Катание на надувном драконе'

# BE - 1020 Раздел "Катание на снегоходах" в меню "Чем заняться"
def test_menu_what_to_do_winter_snowbike(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]        # Кнопка "Чем заняться"
    btn_winter = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[0]                # Кнопка "Зимний сезон"
    btn_snowbike = driver.find_elements(*btn_menu_what_to_do.BTN_SNOWBIKE)[0]            # Кнопка "Катание на снегоходах"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_winter).click(btn_snowbike).perform()
    name_part_snowbike = driver.find_element(*name_part.NAME_PART_SLIDER).text
    assert name_part_snowbike == 'Катание на снегоходах'

# BE - 1021 Раздел "Катание на квадроцикле" в меню "Чем заняться"
def test_menu_what_to_do_summer_atv(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_summer = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[1]                # Кнопка "Летнй сезон"
    btn_atv = driver.find_elements(*btn_menu_what_to_do.BTN_ATV)[0]                         # Кнопка "Катание на квадроцикле"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_summer).click(btn_atv).perform()
    name_part_atv = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим название раздела и сверяем его
    assert name_part_atv == 'Катание на квадроцикле'

# BE - 1022 Раздел "Бадминтон" в меню "Чем заняться"
def test_menu_what_to_do_summer_badminton(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_summer = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[1]                # Кнопка "Летнй сезон"
    btn_badminton = driver.find_elements(*btn_menu_what_to_do.BTN_BADMINTON)[0]             # Кнопка "Бадминтон"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_summer).click(btn_badminton).perform()
    name_part_badminton = driver.find_element(*name_part.NAME_PART_SLIDER).text          # Находим название раздела и сверяем его
    assert name_part_badminton == 'Бадминтон'

# BE - 1023 Раздел "Катание на катамаране" в меню "Чем заняться"
def test_menu_what_to_do_summer_catamaran(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_summer = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[1]                # Кнопка "Летнй сезон"
    btn_catamaran = driver.find_elements(*btn_menu_what_to_do.BTN_CATAMARAN)[0]             # Кнопка "Катание на катамаране"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_summer).click(btn_catamaran).perform()
    name_part_catamaran = driver.find_element(*name_part.NAME_PART_SLIDER).text          # Находим название раздела и сверяем его
    assert name_part_catamaran == 'Катание на катамаране'

# BE - 1024 Раздел "Катание на SUP-Доске" в меню "Чем заняться"
def test_menu_what_to_do_summer_supboard(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_summer = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[1]                # Кнопка "Летнй сезон"
    btn_supboard = driver.find_elements(*btn_menu_what_to_do.BTN_SUPBOARD)[0]               # Кнопка "Катание на SUP-Доске"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_summer).click(btn_supboard).perform()
    name_part_supboard = driver.find_element(*name_part.NAME_PART_SLIDER).text           # Находим название раздела и сверяем его
    assert name_part_supboard == 'Катание на SUP-Доске'

# BE - 1025 Раздел "Стрельба из лука" в меню "Чем заняться"
def test_menu_what_to_do_summer_archery(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_summer = driver.find_elements(*btn_menu_what_to_do.BTN_PART_MENU)[1]                # Кнопка "Летнй сезон"
    btn_archery = driver.find_elements(*btn_menu_what_to_do.BTN_ARCHERY)[0]                 # Кнопка "Стрельба из лука"
    ActionChains(driver).move_to_element(btn_what_to_do).move_to_element(btn_summer).click(btn_archery).perform()
    name_part_archery = driver.find_element(*name_part.NAME_PART_SLIDER).text            # Находим название раздела и сверяем его
    assert name_part_archery == 'Стрельба из лука'

# BE - 1026 Раздел "Баня" в меню "Чем заняться"
def test_menu_what_to_do_bath(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]           # Кнопка "Чем заняться"
    btn_bath = driver.find_elements(*btn_menu_what_to_do.BTN_BATH)[0]                       # Кнопка "Баня"
    ActionChains(driver).move_to_element(btn_what_to_do).click(btn_bath).perform()
    name_part_bath = driver.find_element(*name_part.NAME_PART_SLIDER).text               # Находим название раздела и сверяем его
    assert name_part_bath == 'Посещение бани'

# BE - 1027 Раздел "Сауна" в меню "Чем заняться"
def test_menu_what_to_do_sauna(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]             # Кнопка "Чем заняться"
    btn_sauna = driver.find_elements(*btn_menu_what_to_do.BTN_SAUNA)[0]                       # Кнопка "Сауна"
    ActionChains(driver).move_to_element(btn_what_to_do).click(btn_sauna).perform()        # Заходим в меню и выбираем раздел "Сауна"
    name_part_sauna = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим название раздела и сверяем его
    assert name_part_sauna == 'Посещение сауны'

# BE - 1028 Раздел "Белогорский монастырь" в меню "Чем заняться"
def test_menu_what_to_do_monastyr(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]                # Кнопка "Чем заняться"
    btn_monastyr = driver.find_elements(*btn_menu_what_to_do.BTN_MONASTYR)[0]                    # Кнопка "Белогорский монастырь"
    ActionChains(driver).move_to_element(btn_what_to_do).click(btn_monastyr).perform()        # Заходим в меню и выбираем раздел "Белогорский монастырь"
    name_part_monastyr = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим название раздела и сверяем его
    assert name_part_monastyr == 'Посещение белогорского монастыря'

# BE - 1029 Раздел "Проведение банкетов" в меню "Чем заняться"
def test_menu_what_to_do_party(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]             # Кнопка "Чем заняться"
    btn_party = driver.find_elements(*btn_menu_what_to_do.BTN_PARTY)[0]                       # Кнопка "Проведение банкетов"
    ActionChains(driver).move_to_element(btn_what_to_do).click(btn_party).perform()        # Заходим в меню и выбираем раздел "Проведение банкетов"
    name_part_party = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим название раздела и сверяем его
    assert name_part_party == 'Проведение банкетов, выпускных, корпоративов'

# BE - 1030 Раздел "Проведение конференций" в меню "Чем заняться"
def test_menu_what_to_do_conferency(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]                  # Кнопка "Чем заняться"
    btn_conferency = driver.find_elements(*btn_menu_what_to_do.BTN_CONFERENCE)[0]                  # Кнопка "Проведение конференций"
    ActionChains(driver).move_to_element(btn_what_to_do).click(btn_conferency).perform()        # Заходим в меню и выбираем раздел "Проведение конференций"
    name_part_conferency = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим название раздела и сверяем его
    assert name_part_conferency == 'Проведение презентаций и пресс-конференций'

# BE - 1031 Раздел "Мероприятия в беседках" в меню "Чем заняться"
def test_menu_what_to_do_pavilion(driver):
    btn_what_to_do = driver.find_elements(*btn_menu_what_to_do.BTN_WHAT_TO_DO)[0]                # Кнопка "Чем заняться"
    btn_pavilion = driver.find_elements(*btn_menu_what_to_do.BTN_PAVILION)[0]                    # Кнопка "Мероприятия в беседках"
    ActionChains(driver).move_to_element(btn_what_to_do).click(btn_pavilion).perform()        # Заходим в меню и выбираем раздел "Мероприятия в беседках"
    name_part_pavilion = driver.find_element(*name_part.NAME_PART_SLIDER).text                # Находим название раздела и сверяем его
    assert name_part_pavilion == 'Проведение мероприятий в закрытой беседке'

# XXXXXXXXXXX  Кнопка "Проживание"
def test_menu_rent(driver):
    btn_menu = driver.find_elements(*btn_menu_rent.BTN_MENU_RENT)[0]        # Кнопка-меню "проживание"
    assert btn_menu.text == 'Проживание'                                    # Кнопка-меню "проживание" - проверяем название
    btn_menu.click()                                                        # Нажимаем  Кнопка-меню "проживание"
    name_part_rent = driver.find_elements(*name_part.NAME_PART_SLIDER)[1].text     # Находим название открывшегося раздела
    assert name_part_rent == 'Проживание на курорте Белогорье'
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru"]').click()  # Переходим на главную страницу

# XXXXXXXXXXX  Раздел "Дома" в меню "Проживание"
def test_menu_rent_house(driver):
    btn_menu = driver.find_elements(*btn_menu_rent.BTN_MENU_RENT)[0]           # Кнопка-меню "проживание"
    btn_menu_house = driver.find_elements(*btn_menu_rent.BTN_SUBMENU)[2]      # Кнопка  Дома в меню "проживание"
    ActionChains(driver).move_to_element(btn_menu).click(btn_menu_house).perform()
    name_part_rent_house = driver.find_element(*name_part.NAME_PART).text     # Находим название открывшегося раздела
    assert name_part_rent_house == 'Дома для проживания'

# XXXXXXXXXXX  Раздел "Гостиница" в меню "Проживание"
def test_menu_rent_room(driver):
    btn_menu = driver.find_elements(*btn_menu_rent.BTN_MENU_RENT)[0]      # Кнопка-меню "проживание"
    btn_menu_room = driver.find_elements(*btn_menu_rent.BTN_SUBMENU)[3]   # Кнопка  Гостиница в меню "проживание"
    ActionChains(driver).move_to_element(btn_menu).click(btn_menu_room).perform()
    name_part_rent_room = driver.find_element(*name_part.NAME_PART).text  # Находим название открывшегося раздела
    assert name_part_rent_room == 'Проживание в гостинице'

#  XXXXX   Кнопка "Прокат снаряжения"
def test_menu_rent_equipment(driver):
    btn_menu_rent_equipment = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]  # Кнопка-меню "Прокат снаряжения"
    assert btn_menu_rent_equipment.text == 'Прокат снаряжения'
    btn_menu_rent_equipment.click()                                                             # Нажимаем Кнопка-меню "Прокат снаряжения"
    name_part_rent_equipment = driver.find_element(*name_part.NAME_PART).text
    assert name_part_rent_equipment == 'Аренда инвентаря'
    driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru"]').click()           # Переходим на главную страницу

# XXXX    Раздел "Прокат горных лыж" в меню "Прокат снаряжения"
def test_menu_rent_mount_ski(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]             # Кнопка-меню "Прокат снаряжения"
    btn_winter = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[4]                  # Кнопка Зимний сезон в меню "Прокат снаряжения"
    btn_mount_ski = driver.find_elements(*btn_rent_equipment.BTN_MOUNT_SKI)[0]             # Кнопка Прокат горных лыж в меню
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_winter).click(btn_mount_ski).perform()
    name_part_rent_mount_ski = driver.find_element(*name_part.NAME_PART_RENT).text        # Находим название открывшегося раздела
    assert name_part_rent_mount_ski == 'Прокат горных лыж'

# XXXX    Раздел "Прокат беговых лыж" в меню "Прокат снаряжения"
def test_menu_rent_cross_ski(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]  # Кнопка-меню "Прокат снаряжения"
    btn_winter = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[4]       # Кнопка Зимний сезон в меню "Прокат снаряжения"
    btn_cross_ski = driver.find_elements(*btn_rent_equipment.BTN_CROSS_SKI)[0]  # Кнопка Прокат беговых лыж в меню
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_winter).click(btn_cross_ski).perform()
    name_part_rent_cross_ski = driver.find_element(*name_part.NAME_PART_RENT).text    # Находим название открывшегося раздела
    assert name_part_rent_cross_ski == 'Прокат беговых лыж'

# XXXX    Раздел "Прокат сноуборда" в меню "Прокат снаряжения"
def test_menu_rent_snowbord(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]  # Кнопка-меню "Прокат снаряжения"
    btn_winter = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[4]       # Кнопка Зимний сезон в меню "Прокат снаряжения"
    btn_snowbord = driver.find_elements(*btn_rent_equipment.BTN_SNOWBORD)[0]    # Кнопка Прокат сноуборда в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_winter).click(btn_snowbord).perform()
    name_part_rent_snowbord = driver.find_element(*name_part.NAME_PART_RENT).text    # Находим название открывшегося раздела
    assert name_part_rent_snowbord == 'Прокат сноуборда'

# XXXX    Раздел "Прокат надувного дракона" в меню "Прокат снаряжения"
def test_menu_rent_dragon(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]  # Кнопка-меню "Прокат снаряжения"
    btn_winter = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[4]       # Кнопка Зимний сезон в меню "Прокат снаряжения"
    btn_dragon = driver.find_elements(*btn_rent_equipment.BTN_DRAGON)[0]        # Кнопка Прокат надувного дракона в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_winter).click(btn_dragon).perform()
    name_part_rent_dragon = driver.find_element(*name_part.NAME_PART_RENT).text    # Находим название открывшегося раздела
    assert name_part_rent_dragon == 'Прокат надувного дракона'

# XXXX    Раздел "прокат сноутюбинга" в меню "Прокат снаряжения"
def test_menu_rent_tubing(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]  # Кнопка-меню "Прокат снаряжения"
    btn_winter = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[4]       # Кнопка Зимний сезон в меню "Прокат снаряжения"
    btn_tubing = driver.find_elements(*btn_rent_equipment.BTN_TUBING)[0]        # Кнопка прокат сноутюбинга в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_winter).click(btn_tubing).perform()
    name_part_rent_tubing = driver.find_element(*name_part.NAME_PART_RENT).text    # Находим название открывшегося раздела
    assert name_part_rent_tubing == 'Прокат сноутюбинга'

# XXXX    Раздел "Прокат снегохода" в меню "Прокат снаряжения"
def test_menu_rent_snowbike(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]      # Кнопка-меню "Прокат снаряжения"
    btn_winter = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[4]           # Кнопка Зимний сезон в меню "Прокат снаряжения"
    btn_snowbike = driver.find_elements(*btn_rent_equipment.BTN_SNOWBIKE)[0]        # Кнопка Прокат снегохода в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_winter).click(btn_snowbike).perform()
    name_part_rent_snowbike = driver.find_element(*name_part.NAME_PART_RENT).text    # Находим название открывшегося раздела
    assert name_part_rent_snowbike == 'Прокат снегохода'

# XXXX    Раздел "Прокат квадроцикла" в меню "Прокат снаряжения"
def test_menu_rent_atv(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]      # Кнопка-меню "Прокат снаряжения"
    btn_summer = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[5]           # Кнопка Летний сезон в меню "Прокат снаряжения"
    btn_atv = driver.find_elements(*btn_rent_equipment.BTN_ATV)[0]                  # Кнопка Прокат снегохода в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_summer).click(btn_atv).perform()
    name_part_rent_atv = driver.find_element(*name_part.NAME_PART_RENT).text        # Находим название открывшегося раздела
    assert name_part_rent_atv == 'Прокат квадроцикла'

# XXXX    Раздел "Прокат катамарана" в меню "Прокат снаряжения"
def test_menu_rent_catamaran(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]      # Кнопка-меню "Прокат снаряжения"
    btn_summer = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[5]           # Кнопка Летний сезон в меню "Прокат снаряжения"
    btn_catamaran = driver.find_elements(*btn_rent_equipment.BTN_CATAMARAN)[0]      # Кнопка Прокат катамарана в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_summer).click(btn_catamaran).perform()
    name_part_rent_catamaran = driver.find_element(*name_part.NAME_PART_RENT).text  # Находим название открывшегося раздела
    assert name_part_rent_catamaran == 'Прокат катамарана'

# XXXX    Раздел "Прокат SUP-Борда" в меню "Прокат снаряжения"
def test_menu_rent_supboard(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]      # Кнопка-меню "Прокат снаряжения"
    btn_summer = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[5]           # Кнопка Летний сезон в меню "Прокат снаряжения"
    btn_supboard = driver.find_elements(*btn_rent_equipment.BTN_SUPBOARD)[0]      # Кнопка Прокат SUP-Борда в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_summer).click(btn_supboard).perform()
    name_part_rent_supboard = driver.find_element(*name_part.NAME_PART_RENT).text  # Находим название открывшегося раздела
    assert name_part_rent_supboard == 'Прокат SUP-Борда'

# XXXX    Раздел "Прокат инвентаря для стрельбы из лука" в меню "Прокат снаряжения"
def test_menu_rent_archery(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]      # Кнопка-меню "Прокат снаряжения"
    btn_summer = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[5]           # Кнопка Летний сезон в меню "Прокат снаряжения"
    btn_archery = driver.find_elements(*btn_rent_equipment.BTN_ARCHERY)[0]      # Кнопка Прокат инвентаря для стрельбы из лука в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_summer).click(btn_archery).perform()
    name_part_rent_archery = driver.find_element(*name_part.NAME_PART_RENT).text  # Находим название открывшегося раздела
    assert name_part_rent_archery == 'Прокат инвентаря для стрельбы из лука'

# XXXX    Раздел "Прокат ракеток для бадминтона" в меню "Прокат снаряжения"
def test_menu_rent_badminton(driver):
    btn_menu = driver.find_elements(*btn_rent_equipment.BTN_MENU_EQUIPMENT)[0]      # Кнопка-меню "Прокат снаряжения"
    btn_summer = driver.find_elements(*btn_rent_equipment.BTN_SUBMENU)[5]           # Кнопка Летний сезон в меню "Прокат снаряжения"
    btn_badminton = driver.find_elements(*btn_rent_equipment.BTN_BADMINTON)[0]      # Кнопка Прокат ракеток для бадминтона в меню "Прокат снаряжения"
    ActionChains(driver).move_to_element(btn_menu).move_to_element(btn_summer).click(btn_badminton).perform()
    name_part_rent_badminton = driver.find_element(*name_part.NAME_PART_RENT).text  # Находим название открывшегося раздела
    assert name_part_rent_badminton == 'Прокат ракеток для бадминтона'

# BE - 1049 Кнопка "Цены"
def test_price(driver):
    btn_price = driver.find_elements(*btn_menu_what_to_do.BTN_PRICE)[0]
    assert btn_price.text == 'Цены'
    btn_price.click()
    name_part_price = driver.find_element(*name_part.NAME_PART_PRICE).text    # Находим название открывшегося раздела
    assert name_part_price == 'Цены'

# BE - 1050 Электронная почта
def test_contact_email(driver):        # электронная почта
    btn_email = driver.find_elements(*btn_right_side.BTN_EMAIL)[0]            # Находим название кнопки email (ecobelogorieperm@gmail.com)
    assert btn_email.text == 'ecobelogorieperm@gmail.com'

# BE - 1051 Контактный номер телефона  +7 950 476-00-06
def test_contact_phone(driver):        # Номер телефона
    btn_phone = driver.find_elements(*btn_right_side.BTN_PHONE)[0]            # Находим название кнопки телефона  +7 950 476-00-06
    assert btn_phone.text == '+7 950 476-00-06'

# BE - 1052 Соц.сеть Вконтакте
def test_contact_vk(driver):          # переход на страницу ВК
    driver.find_elements(*btn_right_side.BTN_VK)[0].click()                   # Нажимаем кнопку ВК и переходим на сайт ВК
    driver.switch_to.window(driver.window_handles[1])                         # переключаемся на вкладку ВК (сайт ВК)
    name_group_vk = driver.find_element(*name_part.NAME_GROUP_VK).text        # получаем название группы в ВК
    assert name_group_vk == 'Всесезонный экокурорт «Белогорье»'
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# BE - 1053 Кнопка "Обратный звонок"   ,     BE - 1054 Форма "Оставьте заявку" для обратного звонка
def test_callback(driver):
    btn_callback = driver.find_elements(*btn_right_side.BTN_CALLBACK)[0]          # Находим кнопку "Обратный звонок"
    assert btn_callback.text == 'Обратный звонок'                                 # сверяем название кнопки
    btn_callback.click()                                                          # Нажимаем кнопку "Обратный звонок"
    name_part_callback = driver.find_elements(*name_part.NAME_CALLBACK)[6].text   # Находим назване формы "Оставить заявку"
    input_name = driver.find_element(By.ID, 'name')
    input_mobile = driver.find_element(By.ID, 'phone')
    btn_submit = driver.find_element(By.CSS_SELECTOR, '*[onclick="BackCall()"]').text
    assert name_part_callback == 'Оставьте заявку'
    assert input_name.get_attribute('placeholder') == 'Ваше имя'
    assert input_mobile.get_attribute('placeholder') == 'Ваш телефон'
    assert btn_submit == 'Отправить'
    driver.find_element(By.CLASS_NAME, 'carousel__button.is-close').click()       # Находим кнопку и закрываем форму "Оставить заявку"

# BE - 1056 Поля ввода в форме "Оставьте заявку" , сообщения о пустом поле ввода
def test_callback_error(driver, open_callback):
    driver.find_element(*callback.BTN_SEND).click()   # Находим кнопку "Отправить" и нажимаем
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'text-danger')))     # Явное ожидание
    error_name = driver.find_element(*callback.NAME_ERROR).text           # Находим сообщение об ошибке поля ввода Имя
    phone_error = driver.find_element(By.ID, 'phoneError').text         # Находим сообщение об ошибке поля ввода номер телефона
    assert error_name == 'Укажите имя'
    assert phone_error == 'Укажите номер телефона'

# BE - 1057 Поле ввода "Ваше имя" в форме "Оставьте заявку", невалидные значения
@pytest.mark.parametrize("name", ['n', 'н', '12345', '!@#$&*', '个人', '  '])
def test_callback_notvalid_name(driver, open_callback, name):
    driver.find_element(*callback.INPUT_NAME).send_keys(name)              # Находим поле ввода Имя и вводим данные
    driver.find_element(*callback.BTN_SEND).click()                        # Находим кнопку "Отправить" и нажимаем
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'text-danger')))     # Явное ожидание
    error_name = driver.find_element(By.ID, 'nameError').text              # Ищем сообщение ооб ошибке ввода
    driver.find_element(*callback.INPUT_NAME).clear()
    if error_name == 'Укажите имя':
        pass
    else:
        print('Валидация не пройдена')
    assert error_name == 'Укажите имя'

# BE - 1058 Поле ввода "Ваш телефон" в форме "Оставьте заявку", валидация номера
@pytest.mark.parametrize("phone", ['1', '123456789012', ' '])
def test_callback_notvalid_number_phone(driver, open_callback, phone):
    driver.find_element(*callback.INPUT_PHONE).send_keys(phone)    # Находим поле ввода Ваш телефон и вводим данные
    driver.find_element(*callback.BTN_SEND).click()                # Находим кнопку "Отправить" и нажимаем
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'text-danger')))     # Явное ожидание
    error_phone = driver.find_element(*callback.PHONE_ERROR).text  # Ищем сообщение ооб ошибке ввода "Укажите номер телефона"
    driver.find_element(*callback.INPUT_PHONE).clear()              # Очищаем поле ввода
    if error_phone == 'Укажите номер телефона':
        print('Валидация пройдена')
    else:
        print('Валидация не пройдена')
    assert error_phone == 'Укажите номер телефона'

# BE - 1059 Поле ввода "Ваш телефон" в форме "Оставьте заявку", невалидные данные
@pytest.mark.parametrize("phone1", ['R', 'ю', '个人', '!"№;%:?*'])
def test_callback_notvalid_phone(driver, open_callback, phone1):
    driver.find_element(*callback.INPUT_PHONE).send_keys(phone1)    # Находим поле ввода Ваш телефон и вводим данные
    driver.find_element(*callback.BTN_SEND).click()                # Находим кнопку "Отправить" и нажимаем
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'text-danger')))  # Явное ожидание
    error_phone1 = driver.find_element(*callback.PHONE_ERROR).text  # Ищем сообщение ооб ошибке ввода
    driver.find_element(*callback.INPUT_PHONE).clear()              # Очищаем поле ввода
    if error_phone1 == 'Разрешенно писать только цифры':
        print('Валидация пройдена')
    else:
        print('Валидация не пройдена')
    assert error_phone1 == 'Разрешенно писать только цифры'

# BE - 1062 Текстовая ссылка "Обработка персональных данных" в форме "Оставить заявку"
def test_callback_privacy_policy(driver):
    driver.find_element(*btn_right_side.BTN_CALLBACK).click()                     # Находим кнопку "Обратный звонок", нажимаем
    driver.find_element(By.LINK_TEXT, 'обработку персональных данных').click()    # Находим текстовую ссылку и нажимаем её
    document_policy = driver.find_element(*name_part.NAME_PART).text              # сверяем открышийся раздел
    parts_policy = driver.find_elements(By.XPATH, '//h2')                         # находим все пункты в Политика конфиденциальности
    driver.back()
    assert document_policy == 'Политика конфиденциальности'      # сверяем открывшийся документ
    assert len(parts_policy) == 12                               # сверяем количество пунктов в политике конфиденциальности (12 пунктов)

# BE - 1063 Кнопка "Забронировать номер"
def test_btn_rent_room(driver):
    btn_rent_room = driver.find_element(*btn_right_side.BTN_RENT_ROOM)      # Находим кнопку "Забронировать номер"
    assert btn_rent_room.text == 'Забронировать номер'                      # Сверяем название кнопки
    btn_rent_room.click()                                                   # Нажимаем кнопку "Забронировать номер"
    name_part_rent_room = driver.find_element(*name_part.NAME_PART).text    # Находим название открывшегося раздела
    assert name_part_rent_room == 'Онлайн бронирование'
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)                                               # Переключаемся на всплывающее окно
    btn_cookie = driver.find_element(By.CSS_SELECTOR, '*[href="/Пользовательское соглашение.pdf"]')  # Отобразилось всплывающее окно об использовании cookie
    assert btn_cookie.text == 'с Пользовательским соглашением.'
    driver.switch_to.default_content()                                           # Переключаемся на основную страницу сайта
    driver.back()

