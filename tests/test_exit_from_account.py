from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestExit:
    def test_exit_from_account(self,driver,authorization):

        
        personal_account_button = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        personal_account_button.click()
        WebDriverWait(driver, 10).until(expected_conditions .visibility_of_element_located((TestLocators.PROFILE_BUTTON)))
        
        exit_button = driver.find_element(*TestLocators.EXIT_FROM_ACCOUNT)
        exit_button.click()
        
        
        WebDriverWait(driver, 10).until(expected_conditions .visibility_of_element_located((TestLocators.ENTER_TEXT))
        )
        authorization_page = driver.find_element(*TestLocators.ENTER_TEXT)
        assert authorization_page.text == 'Вход'

       

    