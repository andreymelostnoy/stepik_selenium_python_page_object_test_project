from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username1")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password1")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email1")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password11")
    REGISTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password21")
