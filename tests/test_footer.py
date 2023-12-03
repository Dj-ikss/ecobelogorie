import time
from itertools import count
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from pages.base_page import SKI_RESORT_BTN
from pages.locators import name_part

def test_copyright(driver):     # все права защищены
    text_copyright = driver.find_element(By.CLASS_NAME, 'main_footer__copyright').text      # Находим текст
    assert text_copyright == '2023 все права защищены'

def test_privacy_policy(driver):     # Политика конфиденциальности
    btn_policy = driver.find_element(By.CSS_SELECTOR, '*[href="https://ecobelogorie.ru/privacy-policy"]').text   # находим кнопку по гиперссылке
    driver.get("https://ecobelogorie.ru/privacy-policy")                                                         # переходим по гиперссылке
    document_policy = driver.find_element(*name_part.NAME_PART).text                                         # сверяем открышийся раздел
    parts_policy = driver.find_elements(By.XPATH, '//h2')                                                        # находим все пункты в Политика конфиденциальности
    driver.back()
    assert btn_policy == 'Политика конфиденциальности'           # сверяем текст на кнопке
    assert document_policy == 'Политика конфиденциальности'      # сверяем открывшийся документ
    assert len(parts_policy) == 12                               # сверяем количество пунктов в политике конфиденциальности (12 пунктов)

def test_main_title(driver):        # наличие блока Основная информация
    name_main_title = driver.find_elements(By.CLASS_NAME, 'footer__col__title')    # находим название блока
    name_main_title1 = ''.join(name_main_title[0].text.split('\n'))                # объеденяем найденное название в одну строку
    # print(name_main_title1)
    assert name_main_title1 == 'Основнаяинформация'

def test_about_info_from_maintitle(driver):    # раздел О курорте
    btn_about_info = driver.find_element(By.LINK_TEXT, 'О курорте')             # Находим кнопку О курорте
    link_btn_about_info = btn_about_info.get_attribute('href')                  # Получаем ссылку из этой кнопки
    driver.get(link_btn_about_info)                                             # Переходим по ссылке
    promo_slide = driver.find_element(*name_part.NAME_PART_SLIDER).text                     # Находим название раздела
    img_promo_slide = driver.find_element(By.CSS_SELECTOR, '*[src="/images/__content/pages/about/1.jpg"]').is_displayed()   # Находим картинку
    assert promo_slide == 'Всесезонный курорт «Белогорье»'
    assert img_promo_slide == True

def test_info_rent(driver):    # Проживание
    btn_rent = driver.find_element(By.LINK_TEXT, 'Проживание')        # Находим кнопку Проживание
    link_btn_rent = btn_rent.get_attribute('href')                    # Получаем ссылку из этой кнопки
    driver.get(link_btn_rent)                                         # Переходим по ссылке
    info_rent_title = driver.find_elements(*name_part.NAME_PART_SLIDER)            # Находим название раздела
    part1_living = driver.find_element(By.CLASS_NAME, 'title_y--living_block__live').text        # Находим подраздел Проживание
    part2_eat = driver.find_element(By.CLASS_NAME, 'live_page__eat__title').text                 # Находим подраздел Питание
    part3_activity = driver.find_element(By.CLASS_NAME, 'title_y--activity_block__home').text    # Находим подраздел Активности на курорте
    assert info_rent_title[1].text == 'Проживание на курорте Белогорье'
    assert part1_living == 'Проживание'
    assert part2_eat == 'Питание'
    assert part3_activity == 'Активности на курорте'

def test_info_activity(driver):   # Развлечения
    btn_activity = driver.find_element(By.LINK_TEXT, 'Развлечения')      # Находим кнопку Развлечения
    link_btn_activity = btn_activity.get_attribute('href')               # Получаем ссылку из этой кнопки
    driver.get(link_btn_activity)                                        # Переходим по ссылке
    info_activity = driver.find_element(By.CLASS_NAME, 'title_x').text   # Находим название раздела
    assert info_activity == 'Активности'

def test_info_rent_equipment(driver):   # Прокат снаряжения
    btn_rent_equipment = driver.find_element(By.LINK_TEXT, 'Прокат снаряжения')      # Находим кнопку Прокат снаряжения
    link_btn_rent_equipment = btn_rent_equipment.get_attribute('href')               # Получаем ссылку из этой кнопки
    driver.get(link_btn_rent_equipment)                                              # Переходим по ссылке
    info_rent_equipment = driver.find_element(*name_part.NAME_PART).text         # Находим название раздела
    assert info_rent_equipment == 'Аренда инвентаря'

def test_info_contacts(driver):        # Контакты
    btn_contacts = driver.find_element(By.LINK_TEXT, 'Контакты')          # Находим кнопку Контакты
    link_btn_contacts = btn_contacts.get_attribute('href')                # Получаем ссылку из этой кнопки
    driver.get(link_btn_contacts)                                         # Переходим по ссылке
    info_contacts = driver.find_element(*name_part.NAME_PART).text    # Находим название раздела
    assert info_contacts == 'Контакты'

def test_additional_title(driver):    # блок Дополнительная информация
    name_additional_title = driver.find_elements(By.CLASS_NAME, 'footer__col__title')        # находим название блока
    name_additional_title1 = ''.join(name_additional_title[1].text.split('\n'))              # объеденяем в одну строку
    # print(name_additional_title1)
    assert name_additional_title1 == 'Дополнительнаяинформация'

def test_info_mountain_ride(driver):        # Горнолыжка
    SKI_RESORT_BTN(driver)                                                            # Нажимаем на кнопку "Горнолыжка" в футере
    name_part_ski = driver.find_element(*name_part.NAME_PART_SLIDER).text             # Находим название раздела
    assert name_part_ski == 'Горнолыжный комплекс Белогорье'

def test_info_hour_work(driver):        # Часы работы
    btn_hour_work = driver.find_element(By.LINK_TEXT, 'Часы работы')          # Находим кнопку Часы работы
    link_btn_hour_work = btn_hour_work.get_attribute('href')                  # Получаем ссылку из этой кнопки
    driver.get(link_btn_hour_work)                                            # Переходим по ссылке
    info_hour_work = driver.find_element(*name_part.NAME_PART).text       # Находим название раздела
    assert info_hour_work == 'Часы работы'

def test_info_map(driver):        # Карта
    btn_map = driver.find_element(By.LINK_TEXT, 'Карта')                # Находим кнопку Карта
    link_btn_map = btn_map.get_attribute('href')                        # Получаем ссылку из этой кнопки
    driver.get(link_btn_map)                                            # Переходим по ссылке
    info_map = driver.find_element(*name_part.NAME_PART).text       # Находим название раздела
    img_map = driver.find_element(By.XPATH, '//img[contains(@src, ".jpg")]').is_displayed()
    assert info_map == 'Карта курорта «Белогорье»'
    assert img_map == True

# @pytest.mark.skip('Раздел в разработке')
def test_info_price(driver):        # Цена
    btn_price = driver.find_element(By.LINK_TEXT, 'Цена')                 # Находим кнопку Цена
    link_btn_price = btn_price.get_attribute('href')                      # Получаем ссылку из этой кнопки
    driver.get(link_btn_price)                                            # Переходим по ссылке
    info_price = driver.find_element(*name_part.NAME_PART_PRICE).text       # Находим название раздела
    assert info_price == 'Цены'

def test_gallery(driver):        # Галерея
    btn_gallery = driver.find_element(By.LINK_TEXT, 'Галерея')                 # Находим кнопку Галерея
    link_btn_gallery = btn_gallery.get_attribute('href')                       # Получаем ссылку из этой кнопки
    driver.get(link_btn_gallery)                                               # Переходим по ссылке
    info_gallery = driver.find_element(*name_part.NAME_PART).text          # Находим название раздела
    images_gallary = driver.find_elements(By.CLASS_NAME, 'gallery__page__item')   # Находим все изображения
    assert info_gallery == 'Галерея'
    assert len(images_gallary) != 0              # Проверяем, что изображения еть на сайте и кол-во не равно нулю

def test_contact_phone(driver):        # Номер телефона
    btn_contact_phone = driver.find_element(By.LINK_TEXT, '+7 950 476-00-06')             # Находим кнопку Номер телефона
    link_btn_contact_phone = btn_contact_phone.get_attribute('href')                      # Получаем ссылку из этой кнопки
    assert link_btn_contact_phone == 'tel:+7 950 476-00-06'                               # сравниваем ссылку на номер телефона

def test_contact_email(driver):        # электронная почта
    btn_contact_email = driver.find_element(By.LINK_TEXT, 'ecobelogorieperm@gmail.com')   # Находим кнопку эл.почты
    link_btn_contact_email = btn_contact_email.get_attribute('href')                      # Получаем ссылку из этой кнопки
    assert link_btn_contact_email == 'mailto:ecobelogorieperm@gmail.com'                  # сравниваем ссылку на электронку

def test_contact_vk(driver):          # переход на страницу ВК
    btn_vk = driver.find_element(By.CSS_SELECTOR, '*[target="_blank"]').click()       # Находим кнопку и переходим в ВК
    driver.switch_to.window(driver.window_handles[1])                                 # Вкладку ВК делаем активной
    vk_link = driver.current_url                                                      # получаем URL новой вкладки
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    assert vk_link == 'https://vk.com/ecobelogorie'

def test_contact_address(driver):      # наличие адреса курорта
    info_contact_address = driver.find_element(By.CLASS_NAME, 'footer__contact__adress').text         # Находим отображение адреса
    assert info_contact_address == '617442, Пермский край, Кунгурский м.о, Тер. парка отдыха Белогорье, стр. 1'