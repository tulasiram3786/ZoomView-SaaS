import time

import pytest
from selenium.webdriver.common.by import By
from base_pages.Signup_Page import Zoomview_Signup_Page
from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config




class Test_Signup:

    signuppage_url = Read_Config.get_signuppage_url()
    firstname = Read_Config.get_signuppage_firstname()
    lastname = Read_Config.get_signuppage_lastname()
    companyname = Read_Config.get_signuppage_companyname()
    signuppageemail = Read_Config.get_signuppage_email()
    phonenumber = Read_Config.get_signuppage_phonenumber()
    designation = Read_Config.get_signuppage_designation()
    createpassword = Read_Config.get_signuppage_createpassword()
    conformpassword = Read_Config.get_signuppage_conformpassword()
    logger = Log_Maker.log_gen()

    @pytest.mark.sanity
    def test_signup_title_verification(self, setup):

        self.logger.info("*************** Test_Signup *********************")
        self.logger.info("*************** verification of signup page title *********************")
        self.driver = setup
        self.driver.get(self.signuppage_url)
        self.driver.maximize_window()
        time.sleep(2)
        act_title = self.driver.title
        exp_title = "ZoomView | Signup"
        print("Title :- ", act_title)

        if act_title == exp_title:
            self.logger.info("*************** test_signup_title_verification - Title Matched *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_signup_title_verification.png")
            self.logger.info(
                "*************** test_signup_title_verification - Title not matched *********************")
            self.driver.close()
            assert False

        self.driver.quit()

    @pytest.mark.regression
    def test_signup_page_validation(self, setup):
        self.logger.info("*************** test_signup_page_validation started *********************")
        self.driver = setup
        self.driver.get(self.signuppage_url)
        self.driver.maximize_window()
        time.sleep(2)

        act_dashboard_text = self.driver.find_element(By.XPATH,
                                                      "//p[text()='Create your account']").text
        time.sleep(3)

        if act_dashboard_text == "Create your account":
            self.logger.info("*************** signup page verification text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_signup_page_validation.png")
            self.logger.info("*************** signup page verification text not found *********************")
            self.driver.close()
            assert False

        self.driver.quit()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_signup_valid_login(self, setup):
        self.logger.info("*************** test_signup_valid_login started *********************")
        self.driver = setup
        self.driver.get(self.signuppage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.signup = Zoomview_Signup_Page(self.driver)  # Corrected instantiation
        self.signup.enter_signup_firstname(self.firstname)
        self.signup.enter_signup_lastname(self.lastname)
        self.signup.enter_signup_email(self.signuppageemail)
        self.signup.enter_signup_companyname(self.companyname)
        self.signup.enter_signup_phonenumber(self.phonenumber)
        self.signup.enter_signup_designation(self.designation)
        self.signup.enter_signup_createpassword(self.createpassword)
        self.signup.enter_signup_conformpassword(self.conformpassword)
        self.signup.click_signup_createaccount()
        time.sleep(5)  # Wait for the login to process
        act_dashboard_text = self.driver.find_element(By.XPATH,
                                                      "//p[text()='Check your email for the verification link sent to']").text
        time.sleep(3)

        if act_dashboard_text == "Check your email for the verification link sent to":
            self.logger.info("*************** signup page verification text found *********************")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_signup_valid_login.png")
            self.logger.info("*************** signup page verification text not found *********************")
            self.driver.close()
            assert False

        self.driver.quit()

    def test_firstname_invaliddetails(self,setup):

        self.logger.info("*************** test_firstname_invaliddetails started *********************")
        self.driver = setup

        test_cases = [
            ("Tulasiram111", "Enter valid first name"),
            ("tu", "Enter valid first name"),
            (
                "Tulasiram here iam entering more than 30 characters",
                "Enter valid first name"),
            ("tuDJD12$%", "Enter valid first name"),
            ("          ", "Enter valid first name"),
            ("at name last space  ", "Enter valid first name"),

            ("9865478922", "Enter valid first name"),
            ("$*$&#*#-#_@", "Enter valid first name")

        ]

        for first_name, expected_text in test_cases:
            self.logger.info(f"*************** Testing first name: {first_name} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_firstname(first_name)
            time.sleep(3)

            act_dashboard_text = self.driver.find_element(By.XPATH, "//span[text()='Enter valid first name']").text
            time.sleep(3)

            if act_dashboard_text == expected_text:
                self.logger.info(
                    f"*************** First name '{first_name}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_firstname_invaliddetails_{first_name}.png")
                self.logger.info(
                    f"*************** First name '{first_name}' validation text not found *********************")
                assert False

        self.driver.quit()





    def test_lastname_invaliddetails(self,setup):

        self.logger.info("*************** test_lastaname_invaliddetails strted *********************")
        self.driver = setup

        test_cases = [

            (
                "Tulasiram here iam entering more than 30 characters",
                "Enter valid last name"),
            ("tuDJD12$%", "Enter valid last name"),
            ("          ", "Enter valid last name"),
            ("at name last space  ", "Enter valid last name"),

            ("9865478922", "Enter valid last name"),
            ("$*$&#*#-#_@", "Enter valid last name")

        ]

        for last_name, expected_text in test_cases:
            self.logger.info(f"*************** Testing last name: {last_name} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_lastname(last_name)
            time.sleep(3)

            act_dashboard_text = self.driver.find_element(By.XPATH, "//span[text()='Enter valid last name']").text
            time.sleep(3)

            if act_dashboard_text == expected_text:
                self.logger.info(
                    f"*************** Last name '{last_name}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_lastname_invaliddetails_{last_name}.png")
                self.logger.info(
                    f"*************** Last name '{last_name}' validation text not found *********************")
                assert False

        self.driver.quit()

    def test_email_invaliddetails(self,setup):

        self.logger.info("*************** test_email_invaliddetails strted *********************")
        self.driver = setup

        test_cases = [

            (
                "tulasi@gmail.commmmmmm","Invalid email address"),
            ("tulasi@gmail.c", "Invalid email address"),
            ("          ", "Invalid email address"),
            ("tulasi@gmail.com ", "Invalid email address"),

            ("56554@@gmail.com", "Invalid email address"),
            ("#$%$#%^^^%$@@gmail.com", "Invalid email address")

        ]

        for email, expected_text in test_cases:
            self.logger.info(f"*************** Testing Email: {email} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_email(email)
            time.sleep(3)

            act_dashboard_text = self.driver.find_element(By.XPATH, "//span[text()='Invalid email address']").text
            time.sleep(3)

            if act_dashboard_text == expected_text:
                self.logger.info(
                    f"*************** Email '{email}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_email_invaliddetails_{email}.png")
                self.logger.info(
                    f"*************** Email '{email}' validation text not found *********************")
                assert False

        self.driver.quit()

    def test_companyname_invaliddetails(self,setup):

        self.logger.info("*************** test_companyname_invaliddetails strted *********************")
        self.driver = setup

        test_cases = [

            (
                "tulasiram testing company name here iam entering more than 50 characters","Enter valid company name"),
            ("..........", "Enter valid company name"),
            ("          ", "Enter valid company name"),
            ("tulasi ", "Enter valid company name")

        ]

        for companyname, expected_text in test_cases:
            self.logger.info(f"*************** Testing Companyname: {companyname} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_companyname(companyname)
            time.sleep(3)

            act_dashboard_text = self.driver.find_element(By.XPATH, "//span[text()='Enter valid company name']").text
            time.sleep(3)

            if act_dashboard_text == expected_text:
                self.logger.info(
                    f"*************** Companyname '{companyname}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_companyname_invaliddetails_{companyname}.png")
                self.logger.info(
                    f"*************** Companyname '{companyname}' validation text not found *********************")
                assert False

        self.driver.quit()

    def test_phonenumber_invaliddetails(self,setup):

        self.logger.info("*************** test_phonenumber_invaliddetails strted *********************")
        self.driver = setup

        test_cases = [

            ("9847","Phone number does not exists"),
            ("959574653333375", "Phone number does not exists"),
            ("1196859874", "Phone number does not exists")


        ]

        for phonenumber, expected_text in test_cases:
            self.logger.info(f"*************** Testing Phonenumber: {phonenumber} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_phonenumber(phonenumber)
            time.sleep(3)

            act_phonenumber_text = self.driver.find_element(By.XPATH, "//span[text()='Phone number does not exists']").text
            time.sleep(3)

            if act_phonenumber_text == expected_text:
                self.logger.info(
                    f"*************** Phonenumber '{phonenumber}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_phonenumber_invaliddetails_{phonenumber}.png")
                self.logger.info(
                    f"*************** Phonenumber '{phonenumber}' validation text not found *********************")
                assert False

        self.driver.quit()


    def test_designation_invaliddetails(self,setup):

        self.logger.info("*************** test_designation_invaliddetails started *********************")
        self.driver = setup

        test_cases = [

            (
                "Tulasiram testing designation feild and here iam entering more than 50 characters",
                "Enter valid designation name"),
            ("          ", "Enter valid designation name"),
            ("at designation last space  ", "Enter valid designation name")

        ]

        for designation, expected_text in test_cases:
            self.logger.info(f"*************** Testing Designation: {designation} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_designation(designation)
            time.sleep(3)

            act_designation_text = self.driver.find_element(By.XPATH, "//span[text()='Enter valid designation name']").text
            time.sleep(3)

            if act_designation_text == expected_text:
                self.logger.info(
                    f"*************** Designation '{designation}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_designation_invaliddetails_{designation}.png")
                self.logger.info(
                    f"*************** Designation '{designation}' validation text not found *********************")
                assert False

        self.driver.quit()

    def test_createpassword_invaliddetails(self, setup):

        self.logger.info("*************** test_createpassword_invaliddetails started *********************")
        self.driver = setup

        test_cases = [
            ("Tulasiram111", "Password not valid"),
            ("tu", "Password not valid"),
            (
                "Tulasiram djdkfkjfjfkf fkdfjfjjfjfjf fjfjfhere iam entering more than 50 characters",
                "Password not valid"),
            ("          ", "Password not valid"),
            ("at name last space  ", "Password not valid"),
            ("9865478922", "Password not valid"),
            ("$*$&#*#-#_@", "Password not valid")

        ]

        for createpassword, expected_text in test_cases:
            self.logger.info(f"*************** Testing Createpassword: {createpassword} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_createpassword(createpassword)
            time.sleep(3)

            act_createpassword_text = self.driver.find_element(By.XPATH, "//span[text()='Password not valid']").text
            time.sleep(3)

            if act_createpassword_text == expected_text:
                self.logger.info(
                    f"*************** Createpassword '{createpassword}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_createpassword_invaliddetails_{createpassword}.png")
                self.logger.info(
                    f"*************** Createpassword '{createpassword}' validation text not found *********************")
                assert False

        self.driver.quit()

    def test_conformpassword_invaliddetails(self,setup):

        self.logger.info("*************** test_conformpassword_invaliddetails started *********************")
        self.driver = setup

        test_cases = [
            ("Tulasiram111", "Mismatched Password"),
            ("tu", "Mismatched Password"),
            (
                "Tulasiram djdkfkjfjfkf fkdfjfjjfjfjf fjfjfhere iam entering more than 50 characters",
                "Mismatched Password"),
            ("          ", "Mismatched Password"),
            ("at name last space  ", "Mismatched Password"),
            ("9865478922", "Mismatched Password"),
            ("$*$&#*#-#_@", "Mismatched Password")

        ]

        for conformpassword, expected_text in test_cases:
            self.logger.info(f"*************** Testing Conformpassword: {conformpassword} *********************")
            self.driver.get(self.signuppage_url)
            self.driver.maximize_window()
            time.sleep(2)

            signup_page = Zoomview_Signup_Page(self.driver)
            signup_page.enter_signup_conformpassword(conformpassword)
            time.sleep(3)

            act_conformpassword_text = self.driver.find_element(By.XPATH, "//span[text()='Mismatched Password']").text
            time.sleep(3)

            if act_conformpassword_text == expected_text:
                self.logger.info(
                    f"*************** Conformpassword '{conformpassword}' validation text found *********************")
                assert True
            else:
                self.driver.save_screenshot(f".\\screenshots\\test_conformpassword_invaliddetails_{conformpassword}.png")
                self.logger.info(
                    f"*************** Conformpassword '{conformpassword}' validation text not found *********************")
                assert False

        self.driver.quit()

