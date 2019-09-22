from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login1" in self.browser.current_url, \
            "This is not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), \
            "Email field in Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            "Password field in Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), \
            "Email field in Registration form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), \
            "Password field in Registration form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD), \
            "Confirm Password field in Registration form is not presented"
