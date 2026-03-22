from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SigninPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 

      
    EMAIL_FIELD =  (By.XPATH, '//*[@id="user_email"]')
    LOGIN_BUTTON= (By.XPATH, '//*[@name="commit"]')
    PASSWORD_FIELD =(By.XPATH, '//*[@id="user_password"]')
    
   
    
    def enter_login_credentials(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

