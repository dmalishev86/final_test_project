from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), "No 'add to basket' message"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text + ' has been added to your basket.' == \
               self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE).text, "Incorrect 'add to basket' message"

    def product_price_should_be_equal_to_basket_total(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, "Incorrect basket total price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Success message is not disappeared, but should be"

