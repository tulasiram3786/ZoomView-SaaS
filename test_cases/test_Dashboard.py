import time

from urllib3.util import request

from base_pages.Dashboard_Page import Zoomview_Dashboard_Page
from base_pages.Login_Page import Zoomview_Login_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from selenium.webdriver.common.by import By
from tabulate import tabulate
import pandas as pd
from pytest_html import extras

class Test_Dashboard:
    loginpage_url = Read_Config.get_loginpage_url()
    email = Read_Config.get_email()
    password = Read_Config.get_password()
    logger = Log_Maker.log_gen()

    # def test_title_verification_for_dashboad(self,setup):
    #     self.logger.info("*************** Test_Dashboard *********************")
    #     self.logger.info("*************** verification of Dashboard page title *********************")
    #     self.driver = setup
    #     self.driver.get(self.loginpage_url)
    #     self.driver.maximize_window()
    #     time.sleep(2)
    #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
    #     self.login.enter_email(self.email)
    #     self.login.enter_password(self.password)
    #     self.login.click_login()
    #     time.sleep(5)  # Wait for the login to process
    #     act_title = self.driver.title
    #     exp_title = "ZoomView | Dashboard"
    #     print("Dashboard Title :- ",act_title)
    #
    #     if act_title == exp_title:
    #         self.logger.info("*************** test_title_verification_for_dashboad - Title Matched *********************")
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\screenshots\\test_title_verification_for_dashboad.png")
    #         self.logger.info("*************** test_title_verification_for_dashboad - Title not matched *********************")
    #         self.driver.close()
    #         assert False
    #
    def test_dashboard_table(self,setup):
        self.logger.info("*************** Test_Dashboard table *********************")
        self.logger.info("*************** Table data is printed *********************")

        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email(self.email)
        self.login.enter_password(self.password)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process

        # Locate the table element
        table = self.driver.find_element(By.XPATH, "//table")

        # Locate all rows in the table
        rows = table.find_elements(By.XPATH, ".//tr")

        # Prepare data for DataFrame
        table_data = []
        for row in rows:
            # Locate all cells in the current row
            cells = row.find_elements(By.XPATH, ".//td | .//th")
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)

        # Create DataFrame
        df = pd.DataFrame(table_data[1:], columns=table_data[0])

        # Generate the formatted table output using tabulate
        formatted_table = tabulate(df, headers='keys', tablefmt='pretty')

        # Write the formatted table to a text file
        with open('table_output1.txt', 'w', encoding='utf-8') as file:
            file.write(formatted_table)

        print("Table data has been saved to 'table_output2.txt'.")

    # def test_validationofHosts(self,setup):
    #
    #     self.logger.info("*************** Test_Dashboard verify hosts count *********************")
    #     self.logger.info("*************** hosts count = live+offline+stale *********************")
    #
    #     self.driver = setup
    #     self.driver.get(self.loginpage_url)
    #     self.driver.maximize_window()
    #     time.sleep(2)
    #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
    #     self.login.enter_email(self.email)
    #     self.login.enter_password(self.password)
    #     self.login.click_login()
    #     time.sleep(5)  # Wait for the login to process
    #     self.dashboard = Zoomview_Dashboard_Page(self.driver)
    #     self.dashboard.verify_dashboard_hosts()
    #     self.logger.info("*************** Dashboard hosts count matched with live,offline,stale *********************")
    #
    #
    # def test_validationofservices(self,setup):
    #
    #     self.logger.info("*************** Test_Dashboard verify services count *********************")
    #     self.logger.info("*************** services count = ok+warn+crit *********************")
    #
    #     self.driver = setup
    #     self.driver.get(self.loginpage_url)
    #     self.driver.maximize_window()
    #     time.sleep(2)
    #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
    #     self.login.enter_email(self.email)
    #     self.login.enter_password(self.password)
    #     self.login.click_login()
    #     time.sleep(5)  # Wait for the login to process
    #     self.dashboard = Zoomview_Dashboard_Page(self.driver)
    #     self.dashboard.verify_dashboard_services()
    #     self.logger.info("*************** Dashboard serives count matched with ok,warn,crit *********************")

    def test_print_dashboard_lamauat_values(self,setup):
        self.logger.info("*************** test_print_dashboard_lama_values print lama uat values *********************")
        self.logger.info("*************** printing lama uat values *********************")

        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email(self.email)
        self.login.enter_password(self.password)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process
        self.dashboard = Zoomview_Dashboard_Page(self.driver)
        self.dashboard.print_lama_uat_system()
        self.dashboard.print_lama_uat_network()
        self.dashboard.print_lama_uat_application()
        self.dashboard.print_lama_uat_database()

    def test_print_dashboard_lamaprod_values(self,setup):
        self.logger.info("*************** test_print_dashboard_lamaprod_values print lama prod values *********************")
        self.logger.info("*************** printing lama prod values *********************")

        self.driver = setup
        self.driver.get(self.loginpage_url)
        self.driver.maximize_window()
        time.sleep(2)
        self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
        self.login.enter_email(self.email)
        self.login.enter_password(self.password)
        self.login.click_login()
        time.sleep(5)  # Wait for the login to process
        self.dashboard = Zoomview_Dashboard_Page(self.driver)
        self.dashboard.print_lama_prod_system()
        self.dashboard.print_lama_prod_network()
        self.dashboard.print_lama_prod_application()
        self.dashboard.print_lama_prod_database()

















