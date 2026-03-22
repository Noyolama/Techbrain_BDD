from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QuizPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.FIRST_COURSE_START = (By.XPATH, '(//span[text()="Start"])[1]')
        self.NEXT_BUTTON = (By.XPATH, '//span[text()="Next lesson"]')
        self.GO_TO_QUIZ = (By.XPATH, '//span[text()="Go to Quiz"]')
        self.QUESTION_OPTIONS = (By.XPATH,".//input[@type='checkbox']")
        self.SUBMIT_BUTTON = (By.XPATH, '//button[text()="Submit"]')

    def start_first_course(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_COURSE_START)).click()

    def click_next_until_quiz(self):
        # Keep clicking NEXT until "Go to Quiz" is visible
        while True:
            try:
                go_quiz = self.driver.find_element(*self.GO_TO_QUIZ)
                if go_quiz.is_displayed():
                    break
            except:
                self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON)).click()

    def go_to_quiz(self):
        self.wait.until(EC.element_to_be_clickable(self.GO_TO_QUIZ)).click()

    def choose_options(self):
        options = self.wait.until(EC.visibility_of_all_elements_located(self.QUESTION_OPTIONS))
        for opt in options:
            opt.click()  # choose first option of each question

    def submit_quiz(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()
