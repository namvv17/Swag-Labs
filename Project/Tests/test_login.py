from pages.login_page import LoginPage
import time
def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful(), "Login failed!"    

def test_login_invalid_user(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("12345", "secret_sauce")
    assert not login_page.is_login_successful(), "Login should have failed but didn't!"
    error_text = login_page.get_error_message()
    print(error_text)
    assert "Epic sadface" in error_text, "Thông báo lỗi không xuất hiện đúng!"

def test_login_wrong_passwword(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "dasdsa32131@")
    assert not login_page.is_login_successful(), "Login should have failed but didn't!"
    error_text = login_page.get_error_message()
    print(error_text)
    assert "Epic sadface" in error_text, "Thông báo lỗi không xuất hiện đúng!"

def test_login_invalid_user_and_password(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("asdasd", "dasdsa32131@")
    assert not login_page.is_login_successful(), "Login should have failed but didn't!"
    error_text = login_page.get_error_message()
    print(error_text)
    assert "Epic sadface" in error_text, "Thông báo lỗi không xuất hiện đúng!"

def test_login_empty_username(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("","secret_sauce")
    assert not login_page.is_login_successful(), "Login should have failed but didn't!"
    error_text = login_page.get_error_message()
    print(error_text)
    assert "Epic sadface" in error_text, "Thông báo lỗi không xuất hiện đúng!"

def test_login_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user","")
    assert not login_page.is_login_successful(), "Login should have failed but didn't!"
    error_text = login_page.get_error_message()
    print(error_text)
    assert "Epic sadface" in error_text, "Thông báo lỗi không xuất hiện đúng!"

def test_login_empty_username_and_password(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("","")
    assert not login_page.is_login_successful(), "Login should have failed but didn't!"
    error_text = login_page.get_error_message()
    print(error_text)
    assert "Epic sadface" in error_text, "Thông báo lỗi không xuất hiện đúng!"
    time.sleep(2)

def test_login_refresh_page(driver):
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.refresh_page()
    assert login_page.refresh_page(), "Login page should be displayed after refresh, but it was not!"
