import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Zoomview_Login_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from utilities import excel_utils


class Test_Login_data_driven:

    loginpage_url = Read_Config.get_loginpage_url()
    path=".//test_data//zoomview_login_data.xlsx"
    # we are calling directly with the class name because it is in static method.
    logger = Log_Maker.log_gen()
    status_list = []

    def test_valid_login_data_driven(self,setup):
        self.logger.info("*************** test_valid_login_data_driven started *********************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print("number of rows",self.rows)

        for r in range(2,self.rows+1):
            self.email = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.path,"Sheet1",r,2)
            self.exp_login = excel_utils.read_data(self.path,"Sheet1",r,3)
            self.login.enter_email(self.email)
            self.login.enter_password(self.password)
            self.login.click_login()
            time.sleep(3)
            act_title = self.driver.title
            exp_title = "ZoomView | Dashboard"

            if act_title == exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")
                    self.login.click_logout()
                elif self.exp_login == "No":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                    self.login.click_logout()

            elif act_title != exp_title:
                if self.exp_login == "Yes":
                    self.logger.info("test data is failed")
                    self.status_list.append("Fail")
                elif self.exp_login == "No":
                    self.logger.info("test data is passed")
                    self.status_list.append("Pass")

        print("Status list is ",self.status_list)

        if "Fail" in self.status_list:
            self.logger.info("Test data driven test is failed")
            assert False
        else:
            self.logger.info("Test data driven test is passed")
            assert True














