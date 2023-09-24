import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_driver = webdriver.Chrome()
link = 'https://vk.com/ecobelogorie'
chrome_driver.get(link)
chrome_driver.maximize_window()  # макс размер экрана


time.sleep(3)
# chrome_driver.find_element(By.CLASS_NAME, 'header__top__menu--has_submenu').click()
# time.sleep(3)
# chrome_driver.find_element(By.XPATH, '(//*[text() = "Новости"])[1]').click()
# chrome_driver.find_element(By.XPATH, '/html/body/div/footer/div/div[2]/div[2]').click()
i = chrome_driver.current_url




# chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
chrome_driver.quit()