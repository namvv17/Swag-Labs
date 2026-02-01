from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import  ActionChains
import time
class homePage:
    def __init__(self,driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME, "inventory_item")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.product_sort_container = (By.CLASS_NAME, "product_sort_container")
        self.Twitter_link = (By.LINK_TEXT, "social_twitter")
        self.Facebook_link = (By.LINK_TEXT, "social_facebook")
        self.LinkedIn_link = (By.LINK_TEXT, "social_linkedin")
        self.about_sidebar_link = (By.ID, "about_sidebar_link")
        self.Logout_button = (By.ID, "logout_sidebar_link")
        self.button_close_menu = (By.ID, "react-burger-cross-btn")
        self.product_sort_container_A_to_Z = (By.XPATH, "//option[@value='az']")
        self.product_sort_container_Z_to_A = (By.XPATH, "//option[@value='za']")
        self.product_sort_container_Low_to_High = (By.XPATH, "//option[@value='lohi']")
        self.product_sort_container_High_to_Low = (By.XPATH, "//option[@value='hilo']")
        # Use a CSS selector for multiple classes (CLASS_NAME cannot contain spaces)
        self.shopping_cart_badge = (By.CSS_SELECTOR,"span.shopping_cart_badge")
        self.Add_to_cart_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Add_to_cart_bike_light = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.clicking_checkout_button = (By.ID, "checkout")
    
    def get_products_count(self):
        products = self.driver.find_elements(*self.inventory_item)
        return len(products)
    
    def click_menu_button(self):
        try:
            self.driver.find_element(*self.menu_button).click()
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu-wrap"))   
            )
        except Exception as e:
            print(f"Error clicking menu button: {e}")
    
    def is_menu_open(self):
        menu_container = (By.CLASS_NAME, "bm-menu-wrap")
        try:
            # Nếu tìm thấy element và nó đang hiển thị → menu mở
            element = self.driver.find_element(*menu_container)
            return element.is_displayed()
        except:
            # Nếu không tìm thấy → menu đã đóng
            return False
    
    def click_about(self):
        try:
            menu_container = (By.CLASS_NAME, "bm-menu-wrap")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(menu_container)
            )
            
            # Wait for about link to be ready and click it
            about_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.about_sidebar_link)
            )
            
            # Store current URL and handles before clicking
            original_url = self.driver.current_url
            original_handles = set(self.driver.window_handles)
            
            # Click the link
            about_link.click()
            
            try:
                # First, check if a new window appears
                WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > len(original_handles))
                
                # Get the new window handle
                new_handles = set(self.driver.window_handles) - original_handles
                new_handle = next(iter(new_handles))
                
                # Switch to the new window
                print(f"Switching to new window: {new_handle}")
                self.driver.switch_to.window(new_handle)
                
            except Exception as e:
                print(f"No new window appeared: {e}")
                print("Checking if URL changed in current window...")
            
            # Wait for and verify the target URL
            WebDriverWait(self.driver, 10).until(EC.url_contains("saucelabs.com"))
            url = self.driver.current_url
            print(f"Final URL: {url}")
            return url
            
        except Exception as e:
            print(f"Error in click_about: {e}")
            import traceback
            print(f"Stack trace:\n{traceback.format_exc()}")
            return None
        
    def click_Logout_button(self):
        try:
            # Wait for menu to be fully visible
            menu_container = (By.CLASS_NAME, "bm-menu-wrap")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(menu_container)
            )
            
            # Wait for logout link to be clickable and click it
            logout = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.Logout_button)
            )
            logout.click()
            
            # Wait for URL to change to login page
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/")
            )
            
            # Take screenshot after successful logout
            self.driver.save_screenshot("logout_success.png")
            
            return True
        except Exception as e:
            print(f"Error in click_Logout_button: {e}")
            self.driver.save_screenshot("logout_error.png")
            return False

    def close_menu(self):
        try:
            close_button_menu = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.button_close_menu)
            )
            close_button_menu.click()
            menu_container = (By.CLASS_NAME, "bm-menu-wrap")
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(menu_container)
            )
        except Exception as e:
            print(f"Error in close_menu: {e}")

    def hover_over_product_sort(self):
        try:
            # Wait for the sort select to be present and clickable, then move and click
            product_sort = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.product_sort_container)
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(product_sort).perform()
            product_sort.click()
        except Exception as e:
            print(f"Error in hover_over_product_sort: {e}")

    def click_product_sort_Z_to_A(self):
        try:
            # Use the Select helper to reliably change the dropdown value
            select_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.product_sort_container)
            )
            dropdown = Select(select_elem)
            # select by value is more reliable than clicking the option element
            dropdown.select_by_value('za')
        except Exception as e:
            print(f"Error in click_product_sort_Z_to_A: {e}")

    def click_product_sort_price_low_to_high(self):
        try:
            select_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.product_sort_container))
            dropdown = Select(select_elem)
            dropdown.select_by_visible_text('Price (low to high)')
        except Exception as e:
            print(f"Error in click_producr_sort_price_low_to_high: {e}")

    def click_product_sort_price_high_to_low(self):
        try:
            select_elem = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.product_sort_container))
            dropdown = Select(select_elem)
            dropdown.select_by_index('3')
        except Exception as e:
            print(f"Error in click_producr_sort_price_high_to_low: {e}")
    
    def click_add_to_cart_Backpack_buttons(self):
        try:
            # Wait for the add-to-cart button to be present
            btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.Add_to_cart_Backpack))

            # Click the button safely
            # Ensure the element is displayed and enabled before clicking
            WebDriverWait(self.driver, 5).until(lambda d: btn.is_displayed() and btn.is_enabled())
            # Scroll into view then click
            self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
            btn.click()
            time.sleep(0.1)
        except Exception as e:
            print(f"Error in click_add_to_cart_buttons: {e}")
    
    def click_add_to_cart_bike_light_buttons(self):
        try:
            # Wait for the add-to-cart button to be present
            btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.Add_to_cart_bike_light))

            # Click the button safely
            # Ensure the element is displayed and enabled before clicking
            WebDriverWait(self.driver, 5).until(lambda d: btn.is_displayed() and btn.is_enabled())
            # Scroll into view then click
            self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
            btn.click()
            time.sleep(0.1)
        except Exception as e:
            print(f"Error in click_add_to_cart_buttons: {e}")

    def Add_products_to_cart_items_appear(self):
        try:
            badge = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.shopping_cart_badge))
            return int(badge.text)
        except Exception as e:
            print(f"Error in Add_products_to_cart_items_appear: {e}")
            return 0
        
    def are_remove_buttons_displayed(self):
        try:
            remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[id^='remove-']")
            for btn in remove_buttons:
                if not btn.is_displayed():
                    return False
            return len(remove_buttons) > 0
        except Exception as e:
            print(f"Error in are_remove_buttons_displayed: {e}")
            return False
         
    def click_shopping_cart_badge(self):
        try:
            badge = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.shopping_cart_badge)
            )
            badge.click()
        except Exception as e:
            print(f"Error in click_shopping_cart_badge: {e}")
            
    def click_remove_from_cart_buttonṣ(self):
        try:
            # Wait for all remove buttons to be present
            remove_buttons = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button#remove-sauce-labs-backpack"))
            )

            # Click each visible & enabled button safely
            for btn in remove_buttons:
                try:
                    # Ensure the element is displayed and enabled before clicking
                    WebDriverWait(self.driver, 5).until(lambda d, el=btn: el.is_displayed() and el.is_enabled())
                    # Scroll into view then click
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                    btn.click()
                    time.sleep(0.1)
                except Exception:
                    # If clicking one button fails, continue with others
                    print("Warning: failed to click one remove button; continuing")
        except Exception as e:
            print(f"Error in click_remove_from_cart_buttons: {e}")

    def navigate_back_to_home(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "continue-shopping"))).click()
        except Exception as e:
            print(f"Error in navigate_back_to_home: {e}")
            
    def are_add_to_cart_buttons_displayed(self):
        try:
            add_to_cart_buttons = self.driver.find_elements(*self.Add_to_cart_buttons)
            for btn in add_to_cart_buttons:
                if not btn.is_displayed():
                    return False
            return len(add_to_cart_buttons) > 0
        except Exception as e:
            print(f"Error in are_add_to_cart_buttons_displayed: {e}")
            return False
        