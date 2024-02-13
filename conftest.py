import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver(): 
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = service, options = options)
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):
    go_to_authorization_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    go_to_authorization_page.click()

    input_email = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    input_email.send_keys('konstantin_golovin_5_000@gmail.com')

    input_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    input_password.send_keys('qwerty1')

    authorization_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    authorization_button.click()
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button')))
