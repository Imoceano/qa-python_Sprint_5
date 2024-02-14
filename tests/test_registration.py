from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from locators import TestLocators


class TestRegistration:
    def test_register_sucsessfull(self,driver):
        

        account_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_MAIN)
        account_page_button.click()

        go_to_registration_button = driver.find_element(*TestLocators.GO_TO_REGISTRATION_PAGE)
        go_to_registration_button.click()
      

        name_input = driver.find_element(*TestLocators.INPUT_NAME_REGISTRATION)
        name_input.send_keys('Константин')

        password_input = driver.find_element(*TestLocators.INPUT_PASSWORD_REGISTRATION)
        password_input.send_keys('qwerty')

        email_input = driver.find_element(*TestLocators.INPUT_EMAIL_REGISTRATION)
        email_input.send_keys('konstantin_golovin_5_355@gmail.com')

        

        submit_button_registration = driver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION)
        submit_button_registration.click()

       
        WebDriverWait(driver, 10).until(
            expected_conditions .visibility_of_element_located((TestLocators.ENTER_TEXT))
        )

        
        authorization_page = driver.find_element(*TestLocators.ENTER_TEXT)
        assert authorization_page.text == 'Вход'

       


    def test_register_incorrect_password(self,driver):
        
        

        
        account_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_MAIN)
        account_page_button.click()

        go_to_registration_button = driver.find_element(*TestLocators.GO_TO_REGISTRATION_PAGE)
        go_to_registration_button.click()

        name_input = driver.find_element(*TestLocators.INPUT_NAME_REGISTRATION)
        name_input.send_keys('Константин')
        
        password_input = driver.find_element(*TestLocators.INPUT_PASSWORD_REGISTRATION)
        password_input.send_keys('qwert')

        email_input = driver.find_element(*TestLocators.INPUT_EMAIL_REGISTRATION)
        email_input.send_keys('konstantin_golovin_5_991@gmail.com')

        

        submit_button_registration = driver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION)
        submit_button_registration.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((TestLocators.INCORRECT_PASSWORD_TEXT)))

        incorrect_password_text = driver.find_element(*TestLocators.INCORRECT_PASSWORD_TEXT)

        
        assert incorrect_password_text.text == "Некорректный пароль","Пароль нормас"
    

