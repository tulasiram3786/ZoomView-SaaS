import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from base_pages.Forgot_Password_Page import Zoomview_Forgotpassword_Page
from base_pages.Gmail_email import Gmail_Email
from base_pages.Login_Page import Zoomview_Login_Page
from base_pages.zoho_email import Zoho_email
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config


class Test_ForgotPassword:
    forgotpasswordpage_url = Read_Config.get_forgotpasswordpage_url()
    fp_email = Read_Config.get_forgotpassword_email()
    logger = Log_Maker.log_gen()
    loginpage_url = Read_Config.get_loginpage_url()

    def test_Forgotpassword_title_verification(self, setup):

        self.logger.info("*************** Test_ForgotPassword *********************")
        self.logger.info("*************** verification of ForgotPassword page title *********************")
        self.driver = setup
        self.driver.get(self.forgotpasswordpage_url)
        self.driver.maximize_window()
        time.sleep(3)
        act_title = self.driver.title
        exp_title = "ZoomView | ForgotPassword"
        print("Title :- ", act_title)

        if act_title == exp_title:
            self.logger.info(
                "*************** test_Forgotpassword_title_verification - Title Matched *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_Forgotpassword_title_verification.png")
            self.logger.info(
                "*************** test_Forgotpassword_title_verification - Title not matched *********************")
            self.driver.close()
            assert False

        self.driver.quit()

    def test_forgotpassword_page_validation(self, setup):
        self.logger.info("*************** test_forgotpassword_page_validation started *********************")
        self.driver = setup
        self.driver.get(self.forgotpasswordpage_url)
        self.driver.maximize_window()
        time.sleep(2)

        act_dashboard_text = self.driver.find_element(By.XPATH,
                                                      "//p[text()='Find Your Account']").text
        time.sleep(3)

        if act_dashboard_text == "Find Your Account":
            self.logger.info("*************** Forgotpassword page verification text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_forgotpassword_page_validation.png")
            self.logger.info("*************** Forgotpassword page verification text not found *********************")
            self.driver.close()
            assert False

        self.driver.quit()

    def test_forgotpassword_page_valid_email(self, setup):
        self.logger.info("*************** test_forgotpassword_page_valid_email started *********************")
        self.driver = setup
        self.driver.get(self.forgotpasswordpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.forgotpassword = Zoomview_Forgotpassword_Page(self.driver)  # Corrected instantiation
        self.forgotpassword.enter_forgotpasswordpage_email(self.fp_email)
        self.forgotpassword.click_forgotpasswordpage_submit()
        time.sleep(5)  # Wait for the login to process
        act_forgotpassword_text = self.driver.find_element(By.XPATH, "//p[text()='Authentication']").text
        time.sleep(3)

        if act_forgotpassword_text == "Authentication":
            self.logger.info("*************** Forgotpassword text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_forgotpassword_page_valid_email.png")
            self.logger.info("*************** Forgotpassword text not found *********************")
            self.driver.close()
            assert False

    def test_forgotpassword_email_invaliddetails(self, setup):

        self.logger.info("*************** test_forgotpassword_email_invaliddetails started *********************")
        self.driver = setup

        test_cases = [

            (
                "tulasi@gmail.commmmmmm", "Please enter a valid email address."),
            ("tulasi@gmail.c", "Please enter a valid email address."),
            ("          ", "Please enter a valid email address."),
            ("tulasi@gmail.com ", "Please enter a valid email address."),

            ("56554@@gmail.com", "Please enter a valid email address."),
            ("#$%$#%^^^%$@@gmail.com", "Please enter a valid email address.")

        ]

        for fp_email, expected_text in test_cases:
            self.logger.info(f"*************** Testing Forgotpassword_email: {fp_email} *********************")
            self.driver.get(self.forgotpasswordpage_url)
            self.driver.maximize_window()
            time.sleep(2)

            forgotpassword_page = Zoomview_Forgotpassword_Page(self.driver)
            forgotpassword_page.enter_forgotpasswordpage_email(fp_email)
            time.sleep(3)

            act_dashboard_text = self.driver.find_element(By.XPATH,
                                                          "//div[text()='Please enter a valid email address.']").text
            time.sleep(3)

            if act_dashboard_text == expected_text:
                self.logger.info(
                    f"*************** forgotpassword page '{fp_email}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_forgotpassword_email_invaliddetails_{fp_email}.png")
                self.logger.info(
                    f"*************** forgotpassword page '{fp_email}' validation text not found *********************")
                assert False

        self.driver.quit()

    def test_forgotpassword_verify_otp(self,setup):

        self.logger.info("*************** forgotpassword_verify_otp started *********************")
        self.driver = setup
        self.driver.get(self.forgotpasswordpage_url)
        self.driver.maximize_window()
        time.sleep(3)
        self.forgotpassword = Zoomview_Forgotpassword_Page(self.driver)  # Corrected instantiation
        self.forgotpassword.enter_forgotpasswordpage_email(self.fp_email)
        self.forgotpassword.click_forgotpasswordpage_submit()
        time.sleep(5)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver.execute_script("window.open('');")  # Open a new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get("https://www.zoho.com/mail/login.html")

        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(4)

        zoho = Zoho_email(self.driver)
        zoho.signup_for_zoho_for_verify_otp()
        time.sleep(5)
        otp = zoho.extract_otp()
        print(f"The OTP is: {otp}")
        zoho.close_current_window()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        forgotpassword_page = Zoomview_Forgotpassword_Page(self.driver)

        forgotpassword_page.enter_otp_digit_by_digit(otp)
        time.sleep(2)
        forgotpassword_page.authentication_submit_button()
        self.driver.implicitly_wait(10)

        forgotpassword_page.enter_text_createpassword("Zybisys@123")
        time.sleep(2)
        forgotpassword_page.click_hidden_button_for_create()
        time.sleep(2)
        forgotpassword_page.enter_text_conformpassword("Zybisys@123")
        time.sleep(2)
        forgotpassword_page.click_hidden_button_for_conform()
        time.sleep(2)
        forgotpassword_page.click_setpassword_button()
        time.sleep(5)



        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email("tulasiram.r@zybisys.com")
        self.login.enter_password("Zybisys@123")
        self.driver.find_element(By.XPATH, "//span[@class='ant-input-suffix']").click()
        time.sleep(2)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process
        act_dashboard_text = self.driver.find_element(By.XPATH, "//a[text()='Dashboard']").text
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














