import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Zoomview_Login_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker

class Test_Infrastructure:
    loginpage_url = Read_Config.get_loginpage_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    def test_title_verification_for_infrastructure_page(self, setup):
        self.logger.info("*************** Test_Infrastructure *********************")
        self.logger.info("*************** verification of Infrastructure page title *********************")
        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        # --------- calling login page ------------#
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email(self.email)
        self.login.enter_password(self.password)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process

