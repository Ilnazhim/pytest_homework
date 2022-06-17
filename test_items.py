from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_language(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Кнопка не найдена"
    time.sleep(10)
  