from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.chrome.service import Service


class TestRegistrationWithGenerate:
    def test_register_sucsessfull(self,driver):
        

        account_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        account_page_button.click()

        go_to_registration_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')
        go_to_registration_button.click()

        name_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_input.send_keys('Константин')

        email_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        email_input.send_keys('konstantin_golovin_5_991@gmail.com')

        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
        password_input.send_keys('qwerty')

        submit_button_registration = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        submit_button_registration.click()

       
        WebDriverWait(driver, 10).until(
            expected_conditions .visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a'))
        )

        
        authorization_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]')
        assert authorization_page.text == 'Вы — новый пользователь? Зарегистрироваться'

       
        driver.quit()


    def test_register_incorrect_password(self,driver):
        
        

        account_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        account_page_button.click()

        go_to_registration_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')
        go_to_registration_button.click()

        name_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        name_input.send_keys('Константин')

        email_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        email_input.send_keys('konstantin_golovin_5_764@gmail.com')

        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
        password_input.send_keys('qwert')

        submit_button_registration = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        submit_button_registration.click()


        incorrect_password_text = driver.find_element(By.CLASS_NAME, 'input__error')
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'input__error')))
        
        assert incorrect_password_text.text == "Некорректный пароль","Пароль нормас"
        driver.quit()
    

