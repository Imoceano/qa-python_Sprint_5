from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from locators import TestLocators

class TestProfile:
    def test_go_to_profile_sucseed(self,driver,authorization):
        
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)))
        go_to_personal_profile_page = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        go_to_personal_profile_page.click()

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((TestLocators.PROFILE_BUTTON)))
        profile_button = driver.find_element(*TestLocators.PROFILE_BUTTON)
        
        assert profile_button.text == 'Профиль'
    