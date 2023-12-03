from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time
def test_find_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    num_of_elements = len(browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary"))
    assert num_of_elements > 0

