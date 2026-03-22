from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 

      
    DASHBOARD = (By.XPATH,"//h1[contains(text(),'Courses')]")
    SIGNIN_LINK = (By.XPATH, "//nav//a[2]/span")
    SIGNUP_LINK =  (By.XPATH, "//div/a[text()='Sign up']")
    EMAIL_FIELD =  (By.XPATH, '//*[@id="user_email"]')
    PASSWORD_FIELD =(By.XPATH, '//*[@id="user_password"]')
    CONFIRM_PASSWORD_FIELD =  (By.XPATH, '//*[@id="user_password_confirmation"]')
    SIGNUP_BUTTON = (By.XPATH, '//*[@id="new_user"]/div[2]/input')
    CONFIRMATION_TEXT = (By.XPATH, "//p[contains(text(),'Woops')]")
    
    def get_dashboard(self):
     return self.driver.find_elements(*self.DASHBOARD)
    
    def click_login(self):
        self.driver.find_element(*self.SIGNIN_LINK).click()
    
    def click_signup_link(self):
        self.driver.find_element(*self.SIGNUP_LINK).click()

    def enter_credentials(self,email,password,confirm_password):
      self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)
      self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
      self.wait.until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD_FIELD)).send_keys(confirm_password)

    def click_signup_button(self):
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    def confirmation(self):
       self.driver.find_element(*self.CONFIRMATION_TEXT)    