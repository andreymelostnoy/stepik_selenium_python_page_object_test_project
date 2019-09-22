from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        abb_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        abb_to_basket_button.click()

    def price_of_basket_should_be_equal_price_of_product(self):
        price_of_product = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_of_basket = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text
        assert price_of_basket == price_of_product, "Price of basket isn't equal price of product"

    def product_in_basket_should_be_equal_the_product_in_product_card(self):
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        product_in_product_card = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_PRODUCT_CARD).text
        assert product_in_basket == product_in_product_card, \
            "Name of product isn't equal in the basket and the product card"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
