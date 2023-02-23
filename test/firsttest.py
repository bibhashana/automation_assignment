from selenium import webdriver

from pages.login import LoginPage
from pages.search import fieldsearch
import time


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login = LoginPage(driver)
    search = fieldsearch(driver)


    login.enter_username()
    login.enter_password()
    time.sleep(10)
    login.click_login()
    time.sleep(10)

    search.click_leave()
    time.sleep(10)
    search.employeee()
    time.sleep(15)
    search.click_view()
    time.sleep(10)

    driver.quit()

test_login()



