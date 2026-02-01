from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.XPATH, "//button[@id='continue-shopping']")
        self.remove_buttons = (By.XPATH, "//button[contains(@id, 'remove-')]")
    
    def get_product_item(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.cart_items)
            )
            return self.driver.find_elements(*self.cart_items)
        except TimeoutException:
            return []
    
    def click_inventory_items_name(self, item_name):
        try:
            inventory_items_name =WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, item_name))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", inventory_items_name)
            self.driver.execute_script("arguments[0].click();", inventory_items_name)
        except TimeoutException:
            print(f"Item with name {item_name} not found in cart.")