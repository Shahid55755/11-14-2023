import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Pages.pages.BaseClass import BasePage
from Tests.test_package.conftest import BaseTest


@pytest.mark.usefixtures("setup")
class SignIn(BaseTest):
    def __init__(self, driver):
        """Sign Up page locators"""
        self.driver = driver
        self.signup = (By.ID, "signin2")
        self.username = (By.ID, "sign-username")
        self.password = (By.ID, "sign-password")
        self.signup_button = (By.CSS_SELECTOR, "button[onclick='register()']")
        self.btn = (By.CSS_SELECTOR, "button[onclick='register()']")

        """Login page locators"""
        self.signin = (By.ID, "login2")
        self.login_username = (By.ID, "loginusername")
        self.login_password = (By.ID, "loginpassword")
        self.login_button = (By.CSS_SELECTOR, "button[onclick='logIn()']")
        self.name_of_user = (By.ID, "nameofuser")

        """Selected Item for shopping"""
        self.item_name = (By.LINK_TEXT, "HTC One M9")
        self.add_to_cart_btn = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")

        """View cart"""
        self.view_cart = (By.XPATH, "//*[@id='cartur']")
        self.view_total = (By.XPATH, "//h2[normalize-space()='Total']")
        self.price_td = (By.XPATH, '//tbody/tr[2]/td[3]')

        """place_order"""
        self.place_order_loc = (By.CSS_SELECTOR, ".btn.btn-success")

    def create_account(self):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.signup))
        wait.click()
        log.info("Signup button is pressed")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(self.btn, "Sign up"))
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.username)).send_keys("shahid7")
        log.info("User Name is Shahid7")
        wait.until(EC.presence_of_element_located(self.password)).send_keys("1234567")
        log.info("Password Entered")
        wait.until(EC.presence_of_element_located(self.signup_button)).click()
        log.info("SignUp Button is pressed")
        return self.driver.title

    def switch_to_alert(self):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 20)
        alert = wait.until(EC.alert_is_present())
        # Get the text of the alert
        alert_text = alert.text
        log.info("Alert is Opened")
        print(f"Alert text: {alert_text}")
        alert.accept()
        log.info("Alert Accepted")
        """Close button after signup"""
        self.driver.find_element(By.CSS_SELECTOR, "div[id='signInModal'] "
                                                  "div[class='modal-footer'] button:nth-child(1)").click()
        log.info("Closed button is pressed after sign up")
        """Close button coding"""
        return alert_text

    def login_account(self):
        log = self.getLogger()
        wait = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.signin))
        wait.click()
        log.info("Sign In button is pressed")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(self.login_button, "Log in"))
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.login_username)).send_keys("shahid7")
        log.info("User Name is entered")
        wait.until(EC.presence_of_element_located(self.login_password)).send_keys("1234567")
        log.info("Password is entered")
        wait.until(EC.presence_of_element_located(self.login_button)).click()
        """Display Name-->logged"""
        name = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.name_of_user))
        log.info(f"Logged in as {name.text}")
        return name

    def shopping(self):
        try:
            log = self.getLogger()
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.item_name)
            )
            element_text = element.text
            # Scroll to the element using JavaScript
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
            log.info(f"Item is selected: {element_text}")
            return element_text

        except NoSuchElementException:
            print("Element with LINK_TEXT 'HTC One M9' not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def add_to_cart(self):
        try:
            log = self.getLogger()
            element = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.add_to_cart_btn)
            )
            element_text = element.text
            element.click()
            log.info(f"Button  is clicked: {element_text}")
            wait = WebDriverWait(self.driver, 20)
            alert = wait.until(EC.alert_is_present())
            log.info("alert is opened")
            # Get the text of the alert
            alert_text = alert.text
            log.info(f"alert text {alert_text}")
            print(f"Alert text: {alert_text}")
            alert.accept()
            log.info("Alert Accepted")
            return alert_text

        except NoSuchElementException:
            print("Element with Add to cart option not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_carts(self):
        try:
            log = self.getLogger()
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.view_cart)
            )
            element_text = element.text
            element.click()
            log.info(f"Button  is clicked: {element_text}")
            # return element_text
            wait = WebDriverWait(self.driver, 20)
            total = wait.until(EC.presence_of_element_located(self.view_total))
            total_txt = total.text
            return total_txt

        except NoSuchElementException:
            print("Element with Add to cart option not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def calculate(self):
        wait = WebDriverWait(self.driver, 20)
        td_elements = wait.until(EC.presence_of_all_elements_located(self.price_td))

        # Initialize a variable to store the sum
        total_sum = 0

        # Loop through each <td> element, extract its text, and add to the sum
        for td_element in td_elements:
            try:
                # Convert the text to an integer and add to the sum
                total_sum += int(td_element.text)
            except ValueError:
                # Handle the case where the text is not a valid integer
                print(f"Skipping non-integer value: {td_element.text}")

        # Print the total sum
        print(f"Total sum of values: {total_sum}")

    def place_order(self):
        wait = WebDriverWait(self.driver, 20)
        poc = wait.until(EC.presence_of_element_located(self.place_order_loc))
        poc.click()
        time.sleep(5)

