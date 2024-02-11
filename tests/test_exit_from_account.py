from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestExit:
    def test_exit_from_account(self,driver,authorization):

        
        personal_account_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
        personal_account_button.click()
        WebDriverWait(driver, 10).until(expected_conditions .visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))
        
        exit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
        exit_button.click()
        
        
        WebDriverWait(driver, 10).until(expected_conditions .visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a'))
        )
        authorization_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]')
        assert authorization_page.text == 'Вы — новый пользователь? Зарегистрироваться'

       
        driver.quit()

    