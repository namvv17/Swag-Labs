from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[@id='login-button']")
        self.error_message = (By.CSS_SELECTOR, "div.error-message-container h3")

    def login(self, username, password):
        # self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        # self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.url_contains("inventory"))
            return True
        except:
            return False

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.error_message).text
        except:
            return None

    def refresh_page(self):
        self.driver.refresh()
        return "The Internet" in self.driver.title
        