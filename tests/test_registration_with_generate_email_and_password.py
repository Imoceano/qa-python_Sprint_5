from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.chrome.service import Service
from generate_email import GeneratorEmail
from generate_password import GeneratorPassword
from generate_name import GeneratorName

class TestRegistrationWithGenerate:
    def test_register_sucsessfull(self,driver):
        

        go_to_account_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        go_to_account_button.click()

        go_to_registration_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')
        go_to_registration_button.click()

        name_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        random_name = GeneratorName.random_name()
        name_input.send_keys(random_name)

        email_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        random_email = GeneratorEmail.random_email()
        email_input.send_keys(random_email)

        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
        random_password = GeneratorPassword.random_password()
        password_input.send_keys(random_password)

        submit_button_registration = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        submit_button_registration.click()

       
        WebDriverWait(driver, 10).until(
            expected_conditions .visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a'))
        )

        
        authorization_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]')
        assert authorization_page.text == 'Вы — новый пользователь? Зарегистрироваться'

       
        driver.quit()
    

    
