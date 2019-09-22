from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_text(self):
        empty_basket_text_example = "Your basket is empty. Continue shopping"
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert empty_basket_text_example == empty_basket_text, "Basket isn't empty"

    def should_not_be_product_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Some products in the basket"
