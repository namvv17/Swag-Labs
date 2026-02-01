import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    time.sleep(10)
    driver.close()
