import random
import time

from selenium.webdriver.common.by import By


class Zoomview_Signup_Page:

    textbox_firstname_xpath = "//input[@name='first_name']"
    textbox_lastname_xpath = "//input[@name='last_name']"
    textbox_email_xpath = "//input[@name='email']"
    textbox_companyname_xpath = "//input[@name='company_name']"
    textbox_phonenumber_xpath = "//input[@name='phone']"
    textbox_designation_xpath = "//input[@name='designation']"
    textbox_createpassword_xpath = "//input[@name='password']"
    textbox_conformpassword_xpath = "//input[@name='confirm_password']"
    textbox_createpassword_eyesymbol_xpath = "(//span[@class='ant-input-suffix'])[1]"
    textbox_conformpassword_eyesymbol_xpath = "(//span[@class='ant-input-suffix'])[2]"
    button_createaccount_xpath = "//span[text()='Create Account']"

    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def enter_signup_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(firstname)

    def enter_signup_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(lastname)

    def enter_signup_email(self, signupemail):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(signupemail)

    def enter_signup_companyname(self, companyname):
        self.driver.find_element(By.XPATH, self.textbox_companyname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_companyname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_companyname_xpath).send_keys(companyname)

    def enter_signup_phonenumber(self, phnumber):
        self.driver.find_element(By.XPATH, self.textbox_phonenumber_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_phonenumber_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_phonenumber_xpath).send_keys(phnumber)

    def enter_signup_designation(self, designation):
        self.driver.find_element(By.XPATH, self.textbox_designation_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_designation_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_designation_xpath).send_keys(designation)

    def enter_signup_createpassword(self, createpassword):
        self.driver.find_element(By.XPATH, self.textbox_createpassword_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_createpassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_createpassword_xpath).send_keys(createpassword)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.textbox_createpassword_eyesymbol_xpath).click()

    def enter_signup_conformpassword(self, conformpassword):
        self.driver.find_element(By.XPATH, self.textbox_conformpassword_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_conformpassword_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_conformpassword_xpath).send_keys(conformpassword)
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.textbox_conformpassword_eyesymbol_xpath).click()


    def click_signup_createaccount(self):
        self.driver.find_element(By.XPATH, self.button_createaccount_xpath).click()

