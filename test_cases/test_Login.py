import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Zoomview_Login_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_Login:
    loginpage_url = Read_Config.get_loginpage_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    invalid_email = Read_Config.get_invalid_email()
    invalid_password = Read_Config.get_invalid_password()
    logger = Log_Maker.log_gen()            #we are calling directly with the class name because it is in static method.

    @pytest.mark.regression
    def test_title_verification(self,setup):
        self.logger.info("*************** Test_Login *********************")
        self.logger.info("*************** verification of login page title *********************")
        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        act_title = self.driver.title
        exp_title = "ZoomView | Login"
        print(act_title)

        if act_title == exp_title:
            self.logger.info("*************** test_title_verification - Title Matched *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("*************** test_title_verification - Title not matched *********************")
            #print("\033[1;31mGraphs is not coming\033[0m")
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_page_validation(self, setup):
        self.logger.info("*************** test_login_page_validation started *********************")
        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)

        act_dashboard_text = self.driver.find_element(By.XPATH,
                                                      "//p[text()='Login to Zoomview']").text
        time.sleep(3)

        if act_dashboard_text == "Login to Zoomview":
            self.logger.info("*************** login page verification text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_login_page_validation.png")
            self.logger.info("*************** login page verification text not found *********************")
            self.driver.close()
            assert False

        self.driver.quit()

    def test_valid_login(self,setup):
        self.logger.info("*************** test_valid_login started *********************")
        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email(self.email)
        self.login.enter_password(self.password)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process
        act_dashboard_text = self.driver.find_element(By.XPATH, "(//p[text()='Dashboard'])[1]").text
        time.sleep(3)

        if act_dashboard_text == "Dashboard":
            self.logger.info("*************** Dashboard text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
            self.logger.info("*************** Dashboard text not found *********************")
            self.driver.close()
            assert False

    def test_invalid_login(self):
        self.logger.info("*************** test_invalid_login started *********************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email(self.invalid_email)
        self.login.enter_password(self.invalid_password)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process
        loginerror_message = self.driver.find_element(By.XPATH, "//p[text()='Email ID or Password is wrong']").text

        if loginerror_message == "Email ID or Password is wrong":
            self.logger.info("*************** test_invalid_login - error messages matched *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
            self.logger.info("*************** test_invalid_login - error messages not matched *********************")
            self.driver.close()
            assert False

    def test_valid_email_login(self,setup):
        self.logger.info("*************** test_valid_email_login started *********************")
        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email(self.email)
        self.login.enter_password("Tulasi@1111111111111")
        self.driver.find_element(By.XPATH,"//span[@class='ant-input-suffix']").click()
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process
        act_dashboard_text = self.driver.find_element(By.XPATH, "//p[text()='Email ID or Password is wrong']").text
        time.sleep(3)

        if act_dashboard_text == "Email ID or Password is wrong":
            self.logger.info("*************** login password error text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_email_login.png")
            self.logger.info("*************** login password error text not found *********************")
            self.driver.close()
            assert False

    def test_valid_password_login(self,setup):
        self.logger.info("*************** test_valid_password_login started *********************")
        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email("jack.dddddddemo@gmail.com")
        self.login.enter_password(self.password)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process
        act_dashboard_text = self.driver.find_element(By.XPATH, "//p[text()='Email ID or Password is wrong']").text
        time.sleep(3)

        if act_dashboard_text == "Email ID or Password is wrong":
            self.logger.info("*************** login error text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_valid_password_login.png")
            self.logger.info("*************** login error text not found *********************")
            self.driver.close()
            assert False

    def test_login_email_invaliddetails(self,setup):

        self.logger.info("*************** test_login_email_invaliddetails strted *********************")
        self.driver = setup

        test_cases = [

            (
                "tulasi@gmail.commmmmmm","Please enter a valid email address"),
            ("tulasi@gmail.c", "Please enter a valid email address"),
            #("          ", "Invalid email address"),
            #("tulasi@gmail.com ", "Invalid email address"),

            ("56554@@gmail.com", "Please enter a valid email address"),
            ("#$%$#%^^^%$@@gmail.com", "Please enter a valid email address")

        ]

        for login_email, expected_text in test_cases:
            self.logger.info(f"*************** Testing Email: {login_email} *********************")
            self.driver.get(self.loginpage_url)
            self.driver.maximize_window()
            time.sleep(2)

            login_page = Zoomview_Login_Page(self.driver)
            login_page.enter_email(login_email)
            time.sleep(3)

            act_dashboard_text = self.driver.find_element(By.XPATH, "//span[text()='Please enter a valid email address']").text
            time.sleep(3)

            if act_dashboard_text == expected_text:
                self.logger.info(
                    f"*************** Email '{login_email}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_login_email_invaliddetails_{login_email}.png")
                self.logger.info(
                    f"*************** Email '{login_email}' validation text not found *********************")
                assert False

        self.driver.quit()


    def test_login_password_invaliddetails(self, setup):

        self.logger.info("*************** test_login_password_invaliddetails started *********************")
        self.driver = setup

        test_cases = [
            ("Tulasiram111", "Please enter a valid password"),
            ("tu", "Please enter a valid password"),
            (
                "Tulasiram djdkfkjfjfkf fkdfjfjjfjfjf fjfjfhere iam entering more than 50 characters",
                "Please enter a valid password"),
            ("          ", "Please enter a valid password"),
            ("at name last space  ", "Please enter a valid password"),
            ("9865478922", "Please enter a valid password"),
            ("$*$&#*#-#_@", "Please enter a valid password")

        ]

        for login_password, expected_text in test_cases:
            self.logger.info(f"*************** Testing password: {login_password} *********************")
            self.driver.get(self.loginpage_url)
            self.driver.maximize_window()
            time.sleep(2)

            login_page = Zoomview_Login_Page(self.driver)
            login_page.enter_password(login_password)
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//span[@class='ant-input-suffix']").click()
            time.sleep(3)

            act_password_text = self.driver.find_element(By.XPATH, "//span[text()='Please enter a valid password']").text
            time.sleep(3)

            if act_password_text == expected_text:
                self.logger.info(
                    f"*************** password '{login_password}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_login_password_invaliddetails{login_password}.png")
                self.logger.info(
                    f"*************** password '{login_password}' validation text not found *********************")
                assert False

        self.driver.quit()


if __name__ == "__main__":
    test_login = Test_Login()

    # Setup the WebDriver
    driver = test_login.setup_driver()

    # Assign the driver to the test object
    test_login.driver = driver

    #Call the test methods

    test_login.test_title_verification()
    test_login.test_login_page_validation()
    test_login.test_valid_login()
    test_login.test_invalid_login()
    test_login.test_valid_email_login()
    test_login.test_valid_password()


