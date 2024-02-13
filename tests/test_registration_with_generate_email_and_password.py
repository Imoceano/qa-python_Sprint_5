from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from generators.generate_email import GeneratorEmail
from generators.generate_password import GeneratorPassword
from generators.generate_name import GeneratorName
from locators import TestLocators
class TestRegistrationWithGenerate:
    def test_register_sucsessfull_with_generate(self,driver):
        

        account_page_button = driver.find_element(*TestLocators.GO_TO_AUTHORIZATION_PAGE_FROM_MAIN)
        account_page_button.click()

        go_to_registration_button = driver.find_element(*TestLocators.GO_TO_REGISTRATION_PAGE)
        go_to_registration_button.click()
      

        name_input = driver.find_element(*TestLocators.INPUT_NAME_REGISTRATION)
        random_name = GeneratorName.random_name()
        name_input.send_keys(random_name)

        email_input = driver.find_element(*TestLocators.INPUT_EMAIL_REGISTRATION)
        random_email = GeneratorEmail.random_email()
        email_input.send_keys(random_email)

        password_input = driver.find_element(*TestLocators.INPUT_PASSWORD_REGISTRATION)
        random_password = GeneratorPassword.random_password()
        password_input.send_keys(random_password)

        submit_button_registration = driver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION)
        submit_button_registration.click()

       
        WebDriverWait(driver, 10).until(
            expected_conditions .visibility_of_element_located((TestLocators.ENTER_TEXT))
        )

        
        authorization_page = driver.find_element(*TestLocators.ENTER_TEXT)
        assert authorization_page.text == 'Вход'
       
        
    

    
