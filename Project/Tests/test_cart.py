from pages.login_page import LoginPage
from pages.home_page import homePage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart_page_products_count(driver):
    # Bước 1: Login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # Bước 2: Thêm sản phẩm vào giỏ hàng
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()
    home_page.click_add_to_cart_bike_light_buttons()
    # Bước 3: Mở trang giỏ hàng
    home_page.click_shopping_cart_badge()
    cart_page = CartPage(driver)
    products_in_cart = cart_page.get_product_item()
    assert len(products_in_cart) >= 1, f"Số lượng sản phẩm trong giỏ hàng không đúng, Thực tế: {len(products_in_cart)}"

def test_click_inventory_item_name_in_cart(driver):
    # Bước 1: Login
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    # Bước 2: Thêm sản phẩm vào giỏ hàng
    home_page = homePage(driver)
    home_page.click_add_to_cart_Backpack_buttons()
    home_page.click_add_to_cart_bike_light_buttons()
    # Bước 3: Mở trang giỏ hàng
    home_page.click_shopping_cart_badge()
    cart_page = CartPage(driver)
    cart_page.click_inventory_items_name("Sauce Labs Bike Light")
    assert "inventory-item.html?id=4" in driver.current_url, "Không chuyển đến trang chi tiết sản phẩm đúng!"