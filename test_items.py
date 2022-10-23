link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
  
def test_Basket_button_is_dispalyed_for_any_language(browser,user_lang):
    browser.get(link)
    button_basket = browser.find_element("class name", "btn-add-to-basket")
    assert button_basket.is_displayed(), f"Кнопка добавления товара в корзину отсутсвует, язык страницы - {user_lang}"
 
