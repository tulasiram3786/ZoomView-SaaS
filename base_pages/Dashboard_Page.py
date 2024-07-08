import time
from selenium.webdriver.common.by import By

class Zoomview_Dashboard_Page:

    button_Dashboard_xpath = "//a[text()='Dashboard']"
    total_Hosts_xpath = "(//p[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::div[@class='h-[30px]']"
    hosts_Live_xpath = "((//p[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//ancestor::p)[4]"
    hosts_Offline_xpath = "((//p[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//ancestor::p)[6]"
    hosts_Stale_xpath = "((//p[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//ancestor::p)[8]"

    total_Service_xpath = "(//p[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::div[@class='h-[30px]']"
    service_Ok_xpath = "((//p[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//ancestor::p)[4]"
    service_critical_xpath = "((//p[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//ancestor::p)[6]"
    service_warning_xpath = "((//p[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//ancestor::p)[8]"

    text_lamauat_System_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='System']//following-sibling::p)[1]"
    text_lamauat_Database_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Database']//following-sibling::p)[1]"
    text_lamauat_Application_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Application']//following-sibling::p)[1]"
    text_lamauat_Network_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Network']//following-sibling::p)[1]"

    text_lamaprod_System_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='System']//following-sibling::p)[2]"
    text_lamaprod_Database_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Database']//following-sibling::p)[2]"
    text_lamaprod_Application_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Application']//following-sibling::p)[2]"
    text_lamaprod_Network_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Network']//following-sibling::p)[2]"

    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def verify_dashboard_hosts(self):
        total_hosts = int(self.driver.find_element(By.XPATH, self.total_Hosts_xpath).text)
        live = int(self.driver.find_element(By.XPATH, self.hosts_Live_xpath).text)
        offline = int(self.driver.find_element(By.XPATH, self.hosts_Offline_xpath).text)
        stale = int(self.driver.find_element(By.XPATH, self.hosts_Stale_xpath).text)
        print("Totals hosts", total_hosts)
        print("Live hosts:", live)
        print("Offline hosts:", offline)
        print("Stale hosts:", stale)
        total_Hosts = live + offline + stale
        print("The sum of Live, offline and stale hosts:", total_Hosts)

        class Color:
            RED = '\033[91m'
            END = '\033[0m'
            GREEN = '\033[92m'

        if total_hosts == total_Hosts:
            print(Color.GREEN + "successfully matched" + Color.END)
        else:
            print(Color.RED + "not matched" + Color.END)

    def verify_dashboard_services(self):
        total_service = int(self.driver.find_element(By.XPATH, self.total_Service_xpath).text)
        ok = int(self.driver.find_element(By.XPATH, self.service_Ok_xpath).text)
        warn = int(self.driver.find_element(By.XPATH, self.service_warning_xpath).text)
        critical = int(self.driver.find_element(By.XPATH, self.service_critical_xpath).text)
        print("Totals services", total_service)
        print("ok services:", ok)
        print("warn services:", warn)
        print("crit services:", critical)
        total_services = ok + warn + critical
        print("The sum of ok, warn and crit services:", total_services)

        class Color:
            RED = '\033[91m'
            END = '\033[0m'
            GREEN = '\033[92m'

        if total_service == total_services:
            print(Color.GREEN + "Dashboard Services count is succssfully matched with ok,warn,crit" + Color.END)
        else:
            print(Color.RED + "Dashboard Services count is not matched with ok,warn,crit" + Color.END)

    def print_lama_uat_system(self):
        system=self.driver.find_element(By.XPATH, self.text_lamauat_System_xpath).text
        print("Lama uat system :-",system)

    def print_lama_uat_network(self):
        network=self.driver.find_element(By.XPATH, self.text_lamauat_Network_xpath).text
        print("Lama uat network :-",network)

    def print_lama_uat_application(self):
        application=self.driver.find_element(By.XPATH, self.text_lamauat_Application_xpath).text
        print("Lama uat application :-",application)

    def print_lama_uat_database(self):
        database=self.driver.find_element(By.XPATH, self.text_lamauat_Database_xpath).text
        print("Lama uat database :-",database)

    def print_lama_prod_system(self):
        system=self.driver.find_element(By.XPATH, self.text_lamaprod_System_xpath).text
        print("Lama prod system :-",system)

    def print_lama_prod_network(self):
        network=self.driver.find_element(By.XPATH, self.text_lamaprod_Network_xpath).text
        print("Lama prod network :-",network)

    def print_lama_prod_application(self):
        application=self.driver.find_element(By.XPATH, self.text_lamaprod_Application_xpath).text
        print("Lama prod application :-",application)

    def print_lama_prod_database(self):
        database=self.driver.find_element(By.XPATH, self.text_lamaprod_Database_xpath).text
        print("Lama prod database :-",database)






