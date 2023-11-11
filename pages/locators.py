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



class btn_menu_what_to_do:    # Все кнопки в меню "Чем заняться"
    BTN_WHAT_TO_DO = (By.CSS_SELECTOR, '*[href="/chem-zanyatsya"]')               # Кнопка-меню "Чем заняться"
    BTN_PART_MENU = (By.CSS_SELECTOR, '.item__has_submenu_l--2')                     # Разделю в меню "Чем заняться"
    BTN_CROSS_SKIING = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-begovyh-lyzhah"]') # Кнопка "катание беговые лыжи" в меню "Чем заняться"
    BTN_MOUNT_SKIING = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-gornyh-lyzhah"]')  # Кнопка "катание на горных лыжах" в меню "Чем заняться"
    BTN_SNOWBOARD = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-snouborde"]')         # Кнопка "Катание на сноуборде" в меню "Чем заняться"
    BTN_TUBING = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-snoutyubinge"]')         # Кнопка "Катание на сноутюбинге" в меню "Чем заняться"
    BTN_DRAGON = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-naduvnom-drakone"]')     # Кнопка "Катание на сноутюбинге" в меню "Чем заняться"
    BTN_SNOWBIKE = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-snegohodah"]')         # Кнопка "Катание на снегоходах" в меню "Чем заняться"
    BTN_ATV = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-kvadrocikle"]')             # Кнопка "Катание на квадроцикле" в меню "Чем заняться"
    BTN_BADMINTON = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/badminton"]')                    # Кнопка "Бадминтон" в меню "Чем заняться"
    BTN_CATAMARAN = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-katamarane"]')        # Кнопка "Катание на катамаране" в меню Чем заняться"
    BTN_SUPBOARD = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/katanie-na-sup-doske"]')          # Кнопка "Катание на SUP-Доске" в меню Чем заняться"
    BTN_ARCHERY = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya/strelba-iz-luka"]')                # Кнопка "Стрельба из лука" в меню Чем заняться"
    BTN_BATH = (By.CSS_SELECTOR, '*[href = "/chem-zanyatsya/poseschenie-bani"]')                                       # Кнопка "Баня" в меню Чем заняться"
    BTN_SAUNA = (By.CSS_SELECTOR, '*[href="/chem-zanyatsya/poseschenie-sauny"]')                                       # Кнопка "Сауна" в меню Чем заняться"
    BTN_MONASTYR = (By.CSS_SELECTOR, '*[href="/chem-zanyatsya/poseschenie-belogorskogo-monastyrya"]')                  # Кнопка "Белогорский монастырь" в меню Чем заняться"
    BTN_PARTY = (By.CSS_SELECTOR, '*[href="/chem-zanyatsya/provedenie-banketov-vypusknyh-korporativov"]')              # Кнопка "Проведение банкетов" в меню Чем заняться"
    BTN_CONFERENCE = (By.CSS_SELECTOR, '*[href="/chem-zanyatsya/provedenie-prezentaciy-i-press-konferenciy"]')         # Кнопка "Проведение конференций" в меню Чем заняться"
    BTN_PAVILION = (By.CSS_SELECTOR, '*[href="/chem-zanyatsya/provedenie-meropriyatiy-v-zakrytoy-besedke"]')           # Кнопка "Мероприятия в беседках" в меню Чем заняться"
    BTN_PRICE = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/price"]')                                           # Кнопка "Цены"


class btn_menu_rent:
    BTN_MENU_RENT = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prozhivanie"]')     # Кнопка-меню "Проживание"
    BTN_SUBMENU = (By.CSS_SELECTOR, '.item__has_submenu_l--2')                             # локатор на вызов подменю


"""Локаторы для кнопок меню хеддера "Прокат снаряжения"     """
class btn_rent_equipment:
    BTN_MENU_EQUIPMENT = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/prokat"]')                  # Кнопка-меню "Прокат снаряжения"
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


class btn_right_side: # нопки правой части хэдера
    BTN_EMAIL = (By.CSS_SELECTOR, '*[href="mailto:ecobelogorieperm@gmail.com"]')        # Кнопка ecobelogorieperm@gmail.com
    BTN_PHONE = (By.CSS_SELECTOR, '*[href="tel:+7 950 476-00-06"]')                     # Кнопка +7 950 476-00-06
    BTN_VK = (By.CSS_SELECTOR, '*[href="https://vk.com/ecobelogorie"]')                 # Кнопка BK
    BTN_CALLBACK = (By.CLASS_NAME, 'btn_default.btn_ghost.header__bottom__btn_1.js_show_modal')    # Кнопка обратный звонок
    BTN_RENT_ROOM = (By.CLASS_NAME, 'btn_default.btn_x.header__bottom__btn_2')          # Кнопка "Забронировать номер"



class name_part:   # Локаторы названия разделов
    NAME_PART_SLIDER = (By.CLASS_NAME, 'home_promo__slide__title')
    NAME_PART = (By.CLASS_NAME, 'title_x')
    NAME_PART_RENT = (By.CLASS_NAME, 'rent_section__title.title_y')
    NAME_PART_PRICE = (By.CLASS_NAME, 'price__content__title.title_y.title_y--left')

    NAME_GROUP_VK = (By.CLASS_NAME, 'page_name')
    NAME_CALLBACK = (By.CLASS_NAME, 'modal__title')


class callback:  # Кнопки и поля ввода в окне "Обратный звонок"
    INPUT_NAME = (By.ID, 'name')                                # Поле ввода "ИМЯ"
    INPUT_PHONE = (By.ID, 'phone')                              # Поле ввода "Ваш телефон"
    BTN_SEND = (By.CSS_SELECTOR, '*[onclick="BackCall()"]')     # Кнопка "Отправить"
    NAME_ERROR = (By.ID, 'nameError')                           # Сообщение об ошибке ввода "Укажите имя"
    PHONE_ERROR = (By.ID, 'phoneError')                         # Сообщение об ошибке ввода Номера телефона


class main_page:
    NAME_MODUL_GALLERY = (By.CLASS_NAME, 'title_y.title_y--gallery.title_y--gallery__home')                # Локатор блока "Галерея" на главной странице.
    NAME_MODUL_HOME = (By.CLASS_NAME, 'title_y.title_y--living_block.title_y--living_block__home')         # Локатор блока "Проживание" на главной странице.
    NAME_MODUL_ACTIVITY = (By.CLASS_NAME, 'title_y.title_y--activity_block.title_y--activity_block__home') # Локатор блока "Активности на курорте" на главной странице.
    NAME_MODUL_NEWS = (By.CLASS_NAME, 'title_y--news_block__home')                                         # Локатор блока "Новости" на главной странице.

class footer_btn:   # Кнопки футера
    BTN_ACTIVITY = (By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/chem-zanyatsya"]')         # Локатор кнопки "Развлечения" в футере

def click_btn_menu_about(driver):
    driver.find_element(*btn_menu_about.BTN_ABOUT).click()