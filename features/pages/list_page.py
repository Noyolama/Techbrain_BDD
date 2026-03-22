from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 

    LIST_LINK = (By.XPATH,'(//div/a/span)[3]')
    LESSONS_LIST = (By.XPATH,'//a[contains(@href,"goals")]')

    def lists(self):
       self.driver.find_element(*self.LIST_LINK).click()   

    def get_lessons(self):
        # Wait until at least one lesson item is visible
        return self.wait.until(EC.visibility_of_all_elements_located(self.LESSONS_LIST)) 

    

    