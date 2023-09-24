import time
from itertools import count
import time
from itertools import count

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class btn_menu_about:    # Локаторы кнопок в меню "О нас" + кнопки панели навигации (хэддер)
    BTN_ABOUT = (By.CSS_SELECTOR, '*[href="javascript:void(0)"]')                        # Кнопка меню "О нас" (хеддер)
    # Кнопки в меню "О НАС"
    BTN_HOTEL = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/about-us"]')    # Кнопка "О базе отдыха" в меню "О нас" (хеддер)
    BTN_SKI = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/ski-resort"]')    # Кнопка "Горнолыжный комплекс" в меню О нас
    BTN_CAFE = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/cafe"]')         # Кнопка "Питание" в меню О нас
    BTN_SALE = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/action"]')       # Кнопка "Акции" в меню О нас
    BTN_NEWS = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/blog"]')         # Кнопка "Новости" в меню О нас
    BTN_FAQ = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/faq"]')           # Кнопка "Ответы на вопросы" в меню О нас
    # Кнопки хэддера области навигации
    BTN_MAP = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/map-belogorye"]')   # Кнопка "Карта" в меню О нас
    BTN_HOUR_WORK = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/schedule"]')  # Кнопка "График работы"
    BTN_GALLERY = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/gallery"]')     # Кнопка "Галлерея"
    BTN_CONTACTS = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/kontakty"]')   # Кнопка "Контакты"



class btn_menu_what_to:    # Все кнопки в меню "Чем заняться"
    BTN_WHAT_TO_DO = (By.CSS_SELECTOR, '*[href="/chem-zanyatsya"]')               # Кнопка-меню "Чем заняться"
    BTN_WINTER = (By.CSS_SELECTOR, '.item__has_submenu_l--2')                 # Кнопка "Зимний сезон" в меню "Чем заняться"
    BTN_CROSS_SKIING = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-begovyh-lyzhah"]') # Кнопка "катание беговые лыжи" в меню "Чем заняться"
    BTN_MOUNT_SKIING = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-gornyh-lyzhah"]')  # Кнопка "катание на горных лыжах" в меню "Чем заняться"


class btn_menu_rent:
    BTN_MENU_RENT = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prozhivanie"]')     # Кнопка-меню "Проживание"
    BTN_SUBMENU = (By.CSS_SELECTOR, '.item__has_submenu_l--2')                             # локатор на вызов подменю

class btn_rent_equipment:
    BTN_MENU_EQUIPMENT = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat"]')       # Кнопка-меню "Прокат снаряжения"
    BTN_SUBMENU = (By.CSS_SELECTOR, '.item__has_submenu_l--2')
    BTN_MOUNT_SKI = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-gornyh-lyzh"]')    # Кнопка прокат горных лыж  в меню
    BTN_CROSS_SKI = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-begovyh-lyzh"]')   # Кнопка прокат беговых лыж  в меню
    BTN_SNOWBORD = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-snouborda"]')       # Кнопка прокат сноуборда  в меню
    BTN_DRAGON = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-naduvnogo-drakona"]')       # Кнопка прокат Прокат надувного дракона  в меню
    BTN_TUBING = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-snoutyubinga"]')      # Кнопка прокат сноутюбинга  в меню
    BTN_SNOWBIKE = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-snegohoda"]')       # Кнопка Прокат снегохода  в меню
    BTN_ATV = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-kvadrocikla"]')          # Кнопка Прокат квадроцикла  в меню
    BTN_CATAMARAN = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-katamarana"]')     # Кнопка Прокат катамарана  в меню
    BTN_SUPBOARD = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-sup-borda"]')       # Кнопка Прокат SUP-Борда  в меню
    BTN_ARCHERY = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-inventarya-dlya-strelby-iz-luka"]')  # Кнопка Прокат инвентаря для стрельбы из лука  в меню
    BTN_BADMINTON = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat/prokat-raketok-dlya-badmintona"]')    # Кнопка ППрокат ракеток для бадминтона  в меню


class name_part:
    NAME_PART_RESORT = (By.CLASS_NAME, 'home_promo__slide__title')   # Название Раздела "Всесезонный курорт «Белогорье»"
    NAME_PART_SKI = (By.CLASS_NAME, 'home_promo__slide__title')      # Название Раздела "Горнолыжный комплекс"
    # NAME_PART_CAFE = (By.CLASS_NAME, 'title_x')                      # Название Раздела "Питание"
    # NAME_PART_SALE = (By.CLASS_NAME, 'title_x')                      # Название Раздела "Акции"
    # NAME_PART_NEWS = (By.CLASS_NAME, 'title_x')                      # Название Раздела "Новости"
    # NAME_PART_FAQ = (By.CLASS_NAME, 'title_x')                       # Название Раздела "Ответы на вопросы"
    # NAME_PART_MAP = (By.CLASS_NAME, 'title_x')                       # Название Раздела "Карта курорта «Белогорье»"
    # NAME_PART_HOUR_WORK = (By.CLASS_NAME, 'title_x')                 # Название Раздела "Часы работы"
    # NAME_PART_GALLERY = (By.CLASS_NAME, 'title_x')                   # Название Раздела "Галерея"
    # NAME_PART_CONTACTS = (By.CLASS_NAME, 'title_x')                  # Название Раздела "Контакты"
    # NAME_PART_ACTIVITY = (By.CLASS_NAME, 'title_x')                  # Название Раздела "Активности"
    NAME_PART_CROSS_SKIING = (By.CLASS_NAME, 'home_promo__slide__title')    # Название Раздела "Катание на беговых лыжах"
    NAME_PART_MOUNT_SKIING = (By.CLASS_NAME, 'home_promo__slide__title')    # Название Раздела "Катание на беговых лыжах"

    NAME_PART_SLIDER = (By.CLASS_NAME, 'home_promo__slide__title')
    NAME_PART = (By.CLASS_NAME, 'title_x')
    NAME_PART_RENT = (By.CLASS_NAME, 'rent_section__title.title_y')

def click_btn_menu_about(driver):
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()