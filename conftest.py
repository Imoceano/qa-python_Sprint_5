import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from locators import TestLocators



@pytest.fixture
def driver(): 
    
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(service = service, options = options)
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    go_to_authorization_page = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_MAIN)
    go_to_authorization_page.click()

    input_email = driver.find_element(*TestLocators.INPUT_EMAIL_AUTHORIZATION)
    input_email.send_keys('konstantin_golovin_5_000@gmail.com')

    input_password = driver.find_element(*TestLocators.INPUT_PASSWORD_AUTHORIZATION)
    input_password.send_keys('qwerty1')

    authorization_button = driver.find_element(*TestLocators.SUBMIT_BUTTON_AUTHORIZATION)
    authorization_button.click()
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((TestLocators.SELECTOR_BURGER)))
