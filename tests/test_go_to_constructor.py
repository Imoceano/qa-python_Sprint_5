from locators import TestLocators

class TestWayToConstructor:
    def test_way_from_account_to_constructor_by_button(self,driver,authorization):

        
        
        go_to_personal_account = button_personal_account = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        go_to_personal_account.click()
       
        
        button_constructor = driver.find_element(*TestLocators.GO_TO_CONSTRUCTOR)
        button_constructor.click()
        
        selector = driver.find_element(*TestLocators.SELECTOR_BURGER)
        assert selector  is not None


    
    def test_way_from_account_to_contructor_by_logo(self,driver,authorization):
        
        
        button_personal_account = driver.find_element(*TestLocators.GO_TO_PERSONAL_ACCOUNT_PAGE)
        button_personal_account.click()
        
        button_logo = driver.find_element(*TestLocators.LOGO_MAIN_PAGE)
        button_logo.click()
        
        selector = driver.find_element(*TestLocators.SELECTOR_BURGER)
        assert selector  is not None