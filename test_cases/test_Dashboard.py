import time

from urllib3.util import request

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

        # # Locate the table element
        # table = self.driver.find_element(By.XPATH, "//table")
        #
        # # Locate all rows in the table
        # rows = table.find_elements(By.XPATH, ".//tr")
        #
        # # Prepare data for DataFrame
        # table_data = []
        # for row in rows:
        #     # Locate all cells in the current row
        #     cells = row.find_elements(By.XPATH, ".//td | .//th")
        #     row_data = [cell.text for cell in cells]
        #     table_data.append(row_data)
        #
        # # Create DataFrame
        # df = pd.DataFrame(table_data[1:], columns=table_data[0])
        #
        # # Generate the formatted table output using tabulate
        # formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
        #
        # # Write the formatted table to a text file
        # with open('table_output1.txt', 'w', encoding='utf-8') as file:
        #     file.write(formatted_table)
        #
        # print("Table data has been saved to 'table_output1.txt'.")

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

        # Convert DataFrame to HTML table
        html_table = df.to_html(index=False)

        # Embed the HTML table into the pytest-html report
        extra = extras.html(html_table)
        request.config._html.add_extra(extra)

        print("Table data has been saved to 'table_output1.txt' and embedded in the HTML report.")



