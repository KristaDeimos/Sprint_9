from .login_page import LoginPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        return self
