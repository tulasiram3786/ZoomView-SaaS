import random
import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Zoomview_Forgotpassword_Page:

    button_sp_forgotpassword_xpath = "//a[text()='Forgot Password?']"
    text_findyouraccount_xpath = "//p[text()='Find Your Account']"
    textbox_fp_email_xpath = "//input[@id='email']"
    button_fp_submit_xpath = "//button[@type='submit']"
    button_backtologin_xpath = "//p[text()='BACK TO LOGIN']"
    authentication_submit_button_xpath = "//button[text()='Submit']"
    textbox_createpassword_xpath = "//input[@id='password']"
    textbox_conformpassword_xpath = "//input[@id='conformPassword']"
    hidden_button_for_create_xpath = "(//span[contains(@class,'ant-input-suffix')])[1]"
    hidden_button_for_conform_xpath = "(//span[contains(@class,'ant-input-suffix')])[2]"
    setpassword_button_xpath = "//button[text()='Set Password']"

    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def click_signup_forgotpasswordbutton(self):
        self.driver.find_element(By.XPATH, self.button_sp_forgotpassword_xpath).click()

    def enter_forgotpasswordpage_email(self, fp_email):
        self.driver.find_element(By.XPATH, self.textbox_fp_email_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_fp_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_fp_email_xpath).send_keys(fp_email)

    def click_forgotpasswordpage_submit(self):
        self.driver.find_element(By.XPATH, self.button_fp_submit_xpath).click()

    def click_forgotpasswordpage_backtologin(self):
        self.driver.find_element(By.XPATH, self.button_backtologin_xpath).click()

    def enter_otp_digit_by_digit(self, otp):
        otp = str(otp)
        for i, digit in enumerate(otp):
            otp_field_xpath = f"//input[contains(@aria-label, 'character {i + 1}')]"
            otp_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, otp_field_xpath)))
            otp_field.clear()
            otp_field.send_keys(digit)

    def authentication_submit_button(self):
        self.driver.find_element(By.XPATH, self.authentication_submit_button_xpath).click()

    def enter_text_createpassword(self, createpassword):
        self.driver.find_element(By.XPATH, self.textbox_createpassword_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_createpassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_createpassword_xpath).send_keys(createpassword)

    def enter_text_conformpassword(self, conformpassword):
        self.driver.find_element(By.XPATH, self.textbox_conformpassword_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_conformpassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_conformpassword_xpath).send_keys(conformpassword)

    def click_hidden_button_for_create(self):
        self.driver.find_element(By.XPATH, self.hidden_button_for_create_xpath).click()

    def click_hidden_button_for_conform(self):
        self.driver.find_element(By.XPATH, self.hidden_button_for_conform_xpath).click()

    def click_setpassword_button(self):
        self.driver.find_element(By.XPATH, self.setpassword_button_xpath).click()

