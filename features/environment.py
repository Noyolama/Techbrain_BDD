from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    chrome_options = Options()
    
    # Headless mode (required for GitHub Actions)
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Optional (good for stability)
    chrome_options.add_argument("--window-size=1920,1080")

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    context.driver.quit()
