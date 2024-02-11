from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions

class TestAuthorization:
    def test_go_to_authorization_from_main_page(self,driver):

        authorization_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        authorization_page_button.click()
        
        input_email = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')

        input_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        input_password.send_keys('qwerty1')

        authorization_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        authorization_button.click()

        account = driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a/p')
        assert account.text == 'Личный Кабинет', 'Вы не зашли в свой аккаунт'
        driver.quit()
    
    def test_go_to_authorization_from_personal_account_page(self,driver):

        personal_account_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
        personal_account_button.click()

        input_email = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')

        input_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        input_password.send_keys('qwerty1')

        authorization_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        authorization_button.click()

        account = driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a/p')
        assert account.text == 'Личный Кабинет', 'Вы не зашли в свой аккаунт'
        driver.quit()
    
    def test_go_to_authorization_from_password_recovery_page(self,driver):

        authorization_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
        authorization_page_button.click()

        recovery_password_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')
        recovery_password_page_button.click()

        authorization_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')
        authorization_page_button.click()

        input_email = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')

        input_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        input_password.send_keys('qwerty1')
    
        authorization_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        authorization_button.click()

        account = driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a/p')
        assert account.text == 'Личный Кабинет', 'Вы не зашли в свой аккаунт'
        driver.quit()

    def test_go_to_authorization_from_registration_page(self,driver):

        authorization_page_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
        authorization_page_button.click()

        registration_page_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/p[1]/a')
        registration_page_button.click()

        authorization_page_button = driver.find_element(By.XPATH,'//*[@id="root"]/div/main/div/div/p/a')
        authorization_page_button.click()

        input_email = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')

        input_password = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
        input_password.send_keys('qwerty1')
        authorization_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/form/button')
        authorization_button.click()
        account = driver.find_element(By.XPATH,'//*[@id="root"]/div/header/nav/a/p')
        assert account.text == 'Личный Кабинет', 'Вы не зашли в свой аккаунт'
        driver.quit()