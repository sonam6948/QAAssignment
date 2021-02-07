from selenium import webdriver
from Pages.SprintBoard import MainPage
from Config.config import TestData


def set_up():
    global driver
    driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
    base_url = TestData.BASE_URL
    driver.get(base_url)
    driver.maximize_window()

def test_main_page():
    mp = MainPage(driver)
    mp.do_login()
    mp.do_create_board()
    mp.click_card_green()
    mp.click_card_red()
    mp.click_thumps_up()
    mp.click_delete_red_card()
    print("All test case passed, if no assertion error")

set_up()
test_main_page()
