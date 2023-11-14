import time

import pytest
from Tests.test_package.conftest import BaseTest
from Pages.pages.TestLogin import SignIn


@pytest.mark.usefixtures("setup")
class TestYourClass(BaseTest):
    def test_signup(self):
        sign_obj = SignIn(self.driver)
        test = sign_obj.create_account()
        alert_txt = sign_obj.switch_to_alert()
        if alert_txt == "Sign up successful.":
            assert alert_txt == "Sign up successful."
        else:
            assert alert_txt == "This user already exist."
        print(alert_txt)
        time.sleep(5)

    def test_login(self):
        sign_obj = SignIn(self.driver)
        name_of_user = sign_obj.login_account()
        assert name_of_user.text == "Welcome shahid7", f"User login failed. Actual: {name_of_user}"
        print(name_of_user.text)
        """Shopping Function is called: HTC One M9"""
        element = sign_obj.shopping()
        """Mobile name is returned and validated"""
        assert element == "HTC One M9"
        self.driver.implicitly_wait(5)
        """Add to cart button is clicked"""
        add_cart = sign_obj.add_to_cart()
        """Alert text is validated"""
        assert add_cart == "Product added."
        element_txt = sign_obj.view_carts()
        assert element_txt == "Total"
        sign_obj.calculate()

    def test_place_order(self):
        sign_obj = SignIn(self.driver)
        sign_obj.place_order()









