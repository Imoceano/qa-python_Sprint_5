from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from locators import TestLocators


class TestTabsContructor:
    def test_go_to_tab_toppings(self, driver,authorization):

        go_to_tab_toppings = driver.find_element(*TestLocators. GO_TO_TAB_TOPPINGS)
        go_to_tab_toppings.click()
       

        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((TestLocators.CARD_OF_TOPPINGS)))

        check_toppings = driver.find_element(*TestLocators.CHECK_OF_TOPPINGS)
        assert check_toppings is not None
    
    def test_go_to_tab_souses(self, driver,authorization):

        go_to_tab_souses = driver.find_element(*TestLocators. GO_TO_TAB_SOUSES)
        go_to_tab_souses.click()
        
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((TestLocators.CARD_OF_SAUCE)))

        check_sauce = driver.find_element(*TestLocators.CHECK_OF_OF_SAUCE)
        assert check_sauce is not None

    def test_go_to_tab_buns(self, driver,authorization):

        go_to_tab_souses = driver.find_element(*TestLocators.GO_TO_TAB_SOUSES)
        go_to_tab_souses.click()
        
        WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((TestLocators.CARD_OF_SAUCE)))

        go_to_tab_buns = driver.find_element(*TestLocators.GO_TO_TAB_BUNS)
        go_to_tab_buns.click()
        
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((TestLocators.CARD_OF_BUN)))
        check_bun = driver.find_element(*TestLocators.CHECK_OF_BUNS)
        assert check_bun is not None