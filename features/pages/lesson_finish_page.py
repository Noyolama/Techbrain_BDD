from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LessonFinishPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        
       
        self.LESSONS = (By.XPATH, '(//div/h3/a)[25]')  # Adjust based on actual HTML
        self.FINISH_BUTTON = (By.XPATH, "//button/span[text()='Finish']")
        self.DASHBOARD_TITLE = (By.XPATH, '//h1[contains(text(),"Courses")]')  # Assuming dashboard header



    def click_last_lesson(self):
        lessons = self.wait.until(EC.visibility_of_all_elements_located(self.LESSONS))
        # Scroll and click the last lesson
        last_lesson = lessons[-1]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", last_lesson)
        last_lesson.click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def is_dashboard_opened(self):
        return self.wait.until(EC.visibility_of_element_located(self.DASHBOARD_TITLE))
