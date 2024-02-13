from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from locators import TestLocators



class TestAuthorization:
    def test_go_to_authorization_from_main_page(self,driver):

        authorization_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_MAIN)
        authorization_page_button.click()
    
        
        input_email = driver.find_element(*TestLocators.INPUT_EMAIL_AUTHORIZATION)
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')


        input_password = driver.find_element(*TestLocators.INPUT_PASSWORD_AUTHORIZATION)
        input_password.send_keys('qwerty1')

        authorization_button = driver.find_element(*TestLocators.SUBMIT_BUTTON_AUTHORIZATION)
        authorization_button.click()

        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE))
    

        personal_account_button = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        personal_account_button.click()
        
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        
        account = driver.find_element(*TestLocators.PROFILE_BUTTON)
        assert account.text == 'Профиль', 'Вы не зашли в свой аккаунт'
    
    def test_go_to_authorization_from_personal_account_page(self,driver):

        personal_account_button = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        personal_account_button.click()

        input_email = driver.find_element(*TestLocators.INPUT_EMAIL_AUTHORIZATION)
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')
        
        input_password = driver.find_element(*TestLocators.INPUT_PASSWORD_AUTHORIZATION)
        input_password.send_keys('qwerty1')
        
        authorization_button = driver.find_element(*TestLocators.SUBMIT_BUTTON_AUTHORIZATION)
        authorization_button.click()
        
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE))
    
        personal_account_button = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        personal_account_button.click()
        
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
       
        account = driver.find_element(*TestLocators.PROFILE_BUTTON)
        assert account.text == 'Профиль', 'Вы не зашли в свой аккаунт'
    
    def test_go_to_authorization_from_password_recovery_page(self,driver):

        authorization_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_MAIN)
        authorization_page_button.click()
        
        recovery_password_page_button = driver.find_element(*TestLocators.GO_TO_RECOVERY_PASSWORD_PAGE)
        recovery_password_page_button.click()
        
        authorization_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_RECOVERY_PASSWORD_PAGE)
        authorization_page_button.click()
        
        input_email = driver.find_element(*TestLocators.INPUT_EMAIL_AUTHORIZATION)
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')
        
        input_password = driver.find_element(*TestLocators.INPUT_PASSWORD_AUTHORIZATION)
        input_password.send_keys('qwerty1')
       
        authorization_button = driver.find_element(*TestLocators.SUBMIT_BUTTON_AUTHORIZATION)
        authorization_button.click()

        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE))
    
        personal_account_button = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        personal_account_button.click()
        
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        
        account = driver.find_element(*TestLocators.PROFILE_BUTTON)
        assert account.text == 'Профиль', 'Вы не зашли в свой аккаунт'

    def test_go_to_authorization_from_registration_page(self,driver):

        authorization_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_MAIN)
        authorization_page_button.click()
        
        registration_page_button = driver.find_element(*TestLocators.GO_TO_REGISTRATION_PAGE)
        registration_page_button.click()
        
        authorization_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_REGISTRATION_PAGE)
        authorization_page_button.click()
        
        input_email = driver.find_element(*TestLocators.INPUT_EMAIL_AUTHORIZATION)
        input_email.send_keys('konstantin_golovin_5_000@gmail.com')
        
        input_password = driver.find_element(*TestLocators.INPUT_PASSWORD_AUTHORIZATION)
        input_password.send_keys('qwerty1')
       
        authorization_button = driver.find_element(*TestLocators.SUBMIT_BUTTON_AUTHORIZATION)
        authorization_button.click()
        
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE))
    
        personal_account_button = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        personal_account_button.click()
        
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(TestLocators.PROFILE_BUTTON))
        
        account = driver.find_element(*TestLocators.PROFILE_BUTTON)
        assert account.text == 'Профиль', 'Вы не зашли в свой аккаунт'