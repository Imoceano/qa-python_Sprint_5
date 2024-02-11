from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 

class TestProfile:
    def test_go_to_profile_sucseed(self,driver,authorization):
        
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/section[2]/div/button')))
        go_to_personal_profile_page = driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
        go_to_personal_profile_page.click()

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/div/nav/ul/li[3]/button')))
        exit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
        
        assert exit_button.text == 'Выход'
        driver.quit()
    