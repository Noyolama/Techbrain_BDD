from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AssignmentListPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    THIRD_COURSE_LIST =(By.XPATH,"(//span[text()='Lists'])[3]")
    FIRST_LESSON = (By.XPATH,"//h3/a[contains(text(),' 1. Practice, Practice, Practice')]")
    FIRST_ASSIGNMENT = (By.XPATH,"//p/a[contains(text(),'Remove Duplicates')]")

    def click_third_course_list(self):
        self.wait.until(EC.element_to_be_clickable(self.THIRD_COURSE_LIST)).click()

    def click_first_lesson(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_LESSON)).click()

    def scroll_and_click_assignment(self):
        assignment = self.wait.until(EC.presence_of_element_located(self.FIRST_ASSIGNMENT))
        
        # scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", assignment)
        
        # click assignment
        assignment.click()

        # switch to new window/tab
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def is_assignment_opened(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: "assignment" in d.current_url.lower() or "assignment" in d.title.lower()
        )
