from selenium.webdriver.common.by import By

class DashboardPage:
   #locator
    DASHBOARD = (By.XPATH, "//h1[contains(text(),'Courses')]")

    def __init__(self, driver):
        self.driver = driver

    #action
    def get_dashboard_text(self):
        return self.driver.find_element(*self.DASHBOARD).text

    def is_dashboard_visible(self):
        return self.driver.find_element(*self.DASHBOARD).is_displayed()
