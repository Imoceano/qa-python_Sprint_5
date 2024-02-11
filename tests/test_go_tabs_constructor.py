from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
import time

class TestTabsContructor:
    def test_go_to_tab_toppings(self, driver,authorization):

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span').click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]')))
        toppings = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]/p')
        assert toppings.text == 'Говяжий метеорит (отбивная)'
        driver.quit()
    
    def test_go_to_tab_souses(self, driver,authorization):

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]')))
        sauce = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]/p')
        assert sauce.text == 'Соус с шипами Антарианского плоскоходца'
        driver.quit()

    def test_go_to_tab_buns(self, driver,authorization):

        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span').click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[4]')))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span').click()
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]')))
        bun = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/p')
        assert bun.text == 'Краторная булка N-200i'
        driver.quit()