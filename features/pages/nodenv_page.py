from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class NodenvPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
         # Locators
        self.SECOND_COURSE_START = (By.XPATH, '(//a/span[text()="Start"])[2]')
        self.NODENV_LINK = (By.XPATH, "//a[text()='nodenv']")  # You can also use XPath if needed

    def start_second_course(self):
        self.wait.until(EC.element_to_be_clickable(self.SECOND_COURSE_START)).click()

    def scroll_to_nodenv_and_click(self):
       nodenv_element = self.wait.until(EC.presence_of_element_located(self.NODENV_LINK))
    
    # Scroll it into view
       self.driver.execute_script("arguments[0].scrollIntoView(true);", nodenv_element)
       nodenv_element.click()
       time.sleep(2)
     # Switch to the new window/tab
       self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_nodenv_opened(self):
        # Check if the URL or page title contains 'nodenv'
        return 'nodenv' in self.driver.current_url or 'nodenv' in self.driver.title.lower()
