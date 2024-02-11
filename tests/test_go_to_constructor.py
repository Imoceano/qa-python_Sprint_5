
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 


class TestWayToConstructor:
    def test_way_from_account_to_constructor_by_button(self,driver,authorization):

        
        
        button_personal_account = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
        button_personal_account.click()
        
        button_constructor = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')
        button_constructor.click()
        
        burger = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert burger.text == 'Соберите бургер'

        driver.quit()
    
    def test_way_from_account_to_contructor_by_logo(self,driver,authorization):
        
        
        button_personal_account = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
        button_personal_account.click()
        
        button_logo = driver.find_element(By.TAG_NAME, "svg")
        button_logo.click()
    
        burger = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')
        assert burger.text == 'Соберите бургер'