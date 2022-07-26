from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REG_EMAIL = (By.NAME, 'registration-email')
    REG_PASS_1 = (By.NAME, 'registration-password1')
    REG_PASS_2 = (By.NAME, 'registration-password2')
    REG_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini .btn-group .btn')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '.container-fluid .content>#content_inner>p')
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, '#content_inner>.basket_summary>.basket-items')
