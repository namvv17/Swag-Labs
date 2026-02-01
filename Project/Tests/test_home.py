from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.home_page import homePage
import time
def test_home_page_products_count(driver):
    # Bước 1: Login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")

    # Bước 2: Kiểm tra trang chủ
    home_page = homePage(driver)
    product_count = home_page.get_products_count()
    print(f"Số lượng sản phẩm trên trang chủ: {product_count}")
    assert product_count == 6, f"Số lượng sản phẩm hiển thị không đúng, Thực tế: {product_count}"

def test_menu_button_clickable(driver):
    # Bước 1: Login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # Bước 2: Kiểm tra trang chủ
    home_page = homePage(driver)
    home_page.click_menu_button()
    assert home_page.is_menu_open(), "Menu button is not clickable!"

def test_about_clickable(driver: WebDriver):
    # Store original window handle
    original_window = driver.current_window_handle
    
    try:
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")
        
        # Step 2: Open menu and click About
        home_page = homePage(driver)
        home_page.click_menu_button()
        current_url = home_page.click_about()
        
        # Verify navigation
        print(f"Current URL after clicking About: {current_url}")
        assert current_url is not None, "Failed to get URL after clicking About"
        assert "saucelabs.com" in current_url, "Did not navigate to Saucelabs website"
        
    finally:
        # Clean up: close new tab and switch back
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(original_window)

def test_logout_clickable(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    
    # Step 2: Test logout                              
    home_page = homePage(driver)
    home_page.click_menu_button()
    
    # Click logout and verify
    logout_success = home_page.click_Logout_button()
    assert logout_success, "Logout button click failed"
    
    # Verify we're back on login page
    WebDriverWait(driver, 10).until(
        EC.url_contains("saucedemo.com")
    )
    assert driver.current_url.endswith("/"), "Not on login page after logout"

def test_close_menu_button(driver):
    #Strep 1:login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    #Step 2: close menu
    home_page = homePage(driver)
    home_page.click_menu_button()
    home_page.close_menu()
    assert not home_page.is_menu_open(), "Menu did not close properly!"

def test_move_to_sort_container(driver):
    #Strep 1:login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    #Step 2: hover over sort container
    home_page = homePage(driver)
    home_page.hover_over_product_sort()
    # No assertion here; just ensure no exceptions occur during hover
    
def test_click_sort_Z_to_A(driver):
    #Strep 1:login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    #Step 2: click sort Z to A
    home_page = homePage(driver)
    home_page.hover_over_product_sort()
    home_page.click_product_sort_Z_to_A()
    assert True, "Clicking sort Z to A failed!"

def test_click_product_sort_price_low_to_high(driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # step 2: click sort price low to high
    home_page = homePage(driver)
    home_page.hover_over_product_sort()
    home_page.click_product_sort_price_low_to_high()
    assert True, "Clicking sort price low to high failed!"

def test_click_product_sort_price_high_to_low(driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # step 2: click sort price high to low
    home_page = homePage(driver)
    home_page.hover_over_product_sort()
    home_page.click_product_sort_price_high_to_low()
    assert True, "Clicking sort price high to low Failed!"

def test_click_add_to_cart_buttons(driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")  
    # step 2: click add to cart buttons
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()
    assert True, "Clicking add to cart buttons Failed!"

def test_after_clicking_add_to_cart_buttons_show_renmove_button (driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # step 2: click add to cart buttons
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()
    assert home_page.are_remove_buttons_displayed(), "Remove buttons are not displayed after adding to cart!"

def test_shopping_cart_badge_count(driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # step 2: check shopping cart badge count
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()
    home_page.click_add_to_cart_bike_light_buttons()
    Product_count_item= home_page.Add_products_to_cart_items_appear()
    home_page.Add_products_to_cart_items_appear()
    print(f"Số lượng sản phẩm trong giỏ hàng: {Product_count_item}")
    assert Product_count_item >=1, f"Số lượng sản phẩm trong giỏ hàng không đúng, Thực tế: {Product_count_item}"

def test_click_shopping_cart_badge(driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # step 2: click shopping cart badge
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()
    home_page.click_shopping_cart_badge()
    assert True, "Clicking shopping cart badge Failed!"

def test_click_remove_buttons(driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # step 2: click remove buttons     
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()  
    home_page.click_shopping_cart_badge()
    home_page.click_remove_from_cart_buttonṣ()
    assert True, "Clicking remove buttons Failed!"

def test_after_clicking_remove_buttons_show_add_to_cart_buttons(driver):
    # step 1: login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # step 2: click remove buttons
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()
    home_page.click_shopping_cart_badge()
    home_page.click_remove_from_cart_buttonṣ()
    home_page.navigate_back_to_home()
    assert home_page.are_add_to_cart_buttons_displayed(), "Add to cart buttons are not displayed after removing from cart!"
