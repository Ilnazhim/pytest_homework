from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button(browser):
    browser.get(link)
    a = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert a == "button.btn-add-to-basket"

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