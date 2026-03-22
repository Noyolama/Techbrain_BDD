from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LessonList:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 

          # Locators
        self.FIRST_COURSE_START = (By.XPATH, '(//span[text()="Start"])[1]')
        self.LESSON_LIST_BUTTON = (By.XPATH, "//a/span[text()='Lesson list']")
        self.LESSONS =(By.XPATH,'//div/h3/a')
 # Adjust based on actual HTML

    def start_first_course(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_COURSE_START)).click()

    def click_lessonlist(self):
        self.wait.until(EC.element_to_be_clickable(self.LESSON_LIST_BUTTON)).click()

    def get_lessonlist(self):
        # Returns all lesson items
        return self.wait.until(EC.visibility_of_all_elements_located(self.LESSONS))