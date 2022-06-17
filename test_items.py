from selenium.webdriver.common.by import By
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_language(browser):
    browser.get(link)
    assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "Кнопка не найдена"
    time.sleep(10)
    # assert a == "button.btn-add-to-basket"

    # чтобы
    # заработало
    # надо
    # использовать
    # find_elementS
    # 
    # т.к.данная
    # конструкция
    # не
    # дает
    # тесту
    # просто
    # упасть, а
    # возвращает
    # пустое
    # множество, что
    # позволяет
    # сработать
    # ассерту
    # 
    # assert browser.find_elements_by_css_selector("***"), 'basket button not found'