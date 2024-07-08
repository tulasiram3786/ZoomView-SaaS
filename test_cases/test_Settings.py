import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Zoomview_Login_Page
from base_pages.Settings_Page import Zoomview_Settings_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_Settins:
    loginpage_url = Read_Config.get_loginpage_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    def test_title_verification_for_settigspage(self, setup):
        self.logger.info("*************** Test_Settings *********************")
        self.logger.info("*************** verification of settings page title *********************")
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
        # --------- calling settings page ---------#
        self.settings = Zoomview_Settings_Page(self.driver)
        self.settings.click_settings_dropdown()
        time.sleep(1)
        self.settings.click_settings_notification()
        time.sleep(3)

        act_title = self.driver.title
        exp_title = "ZoomView | Notification"

        if act_title == exp_title:
            self.logger.info(
                "*************** test_title_verification_for_settigspage - Title Matched *********************")
            assert True
            print("Settings page Title :", act_title)
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification_for_settigspage.png")
            self.logger.info(
                "*************** test_title_verification_for_settigspage - Title not matched *********************")
            self.driver.close()
            assert False



    def test_settings_enter_valid_emails(self, setup):
        self.logger.info("*************** Test_Settings *********************")
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

        # --------- calling settings page ---------#
        self.settings = Zoomview_Settings_Page(self.driver)
        self.settings.click_settings_dropdown()
        time.sleep(1)
        self.settings.click_settings_notification()
        time.sleep(5)

        # Click the "ADD EMAILS +" button to add a new email input field
        add_email_button = self.driver.find_element(By.XPATH, "//span[text()='ADD EMAILS +']")
        add_email_button.click()
        time.sleep(3)  # Wait for the new input field to appear

        # Find the last email input field to use for all test cases
        email_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@name, 'email')]")
        if email_inputs:
            last_email_input = email_inputs[-1]
            last_email_input.click()
            time.sleep(3)

            # Enter email into the new field
            last_email_input.send_keys("tulasiram1704@gmail.com")
            time.sleep(3)
            self.settings.click_savebutton()
            time.sleep(5)

            act_toast_message = self.driver.find_element(By.XPATH, self.settings.email_toastmessage_xpath).text
            exp_toast_message = "Inserted Successfully"

            if act_toast_message == exp_toast_message:
                self.logger.info("*************** test_settings_enteremail - email entered *********************")
                assert True
            else:
                self.driver.save_screenshot(".\\screenshots\\test_settings_enteremail.png")
                self.logger.info("*************** test_settings_enteremail - email not entered *********************")
                assert False

        else:
            self.logger.info(
                "*************** test_settings_enteremail - no email input field found *********************")
            assert False

        self.driver.quit()



    def test_settings_remove_email(self, setup):
        self.logger.info("*************** Test_Settings *********************")
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

        # --------- calling settings page ---------#
        self.settings = Zoomview_Settings_Page(self.driver)
        self.settings.click_settings_dropdown()
        time.sleep(1)
        self.settings.click_settings_notification()
        time.sleep(3)

        # Identify and remove the specific email
        email_to_remove = "tulasiram1704@gmail.com"
        email_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@name, 'email')]")
        remove_button_xpath_template = "//input[@value='tulasiram1704@gmail.com']//following-sibling::span/p[text()='REMOVE']"

        for email_input in email_inputs:
            if email_input.get_attribute("value") == email_to_remove:
                remove_button_xpath = remove_button_xpath_template.format(email=email_to_remove)
                remove_button = self.driver.find_element(By.XPATH, remove_button_xpath)
                remove_button.click()
                time.sleep(2)
                break

        self.settings.click_deletebutton()
        time.sleep(3)
        # Confirm deletion and save changes
        self.settings.click_savebutton()
        time.sleep(5)



    def test_settings_enter_invalid_emails(self, setup):
        self.logger.info("*************** Test_Settings *********************")
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

        # --------- calling settings page ---------#
        self.settings = Zoomview_Settings_Page(self.driver)
        self.settings.click_settings_dropdown()
        time.sleep(1)
        self.settings.click_settings_notification()
        time.sleep(3)

        # Click the "ADD EMAILS +" button to add a new email input field
        add_email_button = self.driver.find_element(By.XPATH, "//span[text()='ADD EMAILS +']")
        add_email_button.click()
        time.sleep(1)  # Wait for the new input field to appear

        # Find the last email input field to use for all test cases
        email_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@name, 'email_')]")
        if email_inputs:
            last_email_input = email_inputs[-1]

            test_cases = [
                ("tulasi@gmail.commmmmmm", "Please enter a valid email address"),
                ("tulasi@gmail.c", "Please enter a valid email address"),
                ("          ", "Please enter a valid email address"),
                ("tulasi@gmail.com ", "Please enter a valid email address"),
                ("56554@@gmail.com", "Please enter a valid email address"),
                ("#$%$#%^^^%$@@gmail.com", "Please enter a valid email address")
            ]

            for settings_email, expected_text in test_cases:
                self.logger.info(f"*************** Testing Email: {settings_email} *********************")

                # Clear the input field by selecting all and deleting
                last_email_input.click()
                last_email_input.send_keys(Keys.CONTROL, 'a')
                last_email_input.send_keys(Keys.DELETE)
                time.sleep(1)  # Wait for the field to clear

                # Enter the new test email
                last_email_input.send_keys(settings_email)
                time.sleep(1)  # Wait for the validation to appear

                # Verify the validation text
                try:
                    act_dashboard_text = self.driver.find_element(By.XPATH,
                                                                  "//span[text()='Please enter a valid email address']").text
                    if act_dashboard_text == expected_text:
                        self.logger.info(
                            f"*************** Email '{settings_email}' validation text found *********************")
                        assert True
                    else:
                        self.driver.save_screenshot(
                            f".\\screenshots\\test_settings_enter_invalid_emails_{settings_email}.png")
                        self.logger.info(
                            f"*************** Email '{settings_email}' validation text not found *********************")
                        assert False
                except NoSuchElementException:
                    self.driver.save_screenshot(
                        f".\\screenshots\\test_settings_enter_invalid_emails_{settings_email}.png")
                    self.logger.info(
                        f"*************** Validation message not found for email '{settings_email}' *********************")
                    assert False

                time.sleep(1)  # Shorter wait time after validation

            # Optionally, close the browser after the test
            # self.driver.quit()
































