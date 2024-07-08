import random
import time
from selenium.webdriver.common.by import By

class Zoomview_Infrastructure_Page:

    infrastructure_total_hosts_xpath = "(//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::div[@class='h-[30px]']"
    infrastructure_live_hosts_xpath = "((//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[4]"
    infrastructure_offline_host_xpath = "((//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[6]"
    infrastructure_stale_host_xpath = "((//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[8]"

    infrastructure_total_service_xpath = "(//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::div[@class='h-[30px]']"
    infrastructur_service_ok_xpath = "((//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[4]"
    infrastructur_service_critical_xpath = "((//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[6]"
    infrastructur_service_warning_xpath = "((//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[8]"

    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def verify_infrastructure_hosts(self):
        total_hosts = int(self.driver.find_element(By.XPATH, self.infrastructure_total_hosts_xpath).text)
        live = int(self.driver.find_element(By.XPATH, self.infrastructure_live_hosts_xpath).text)
        offline = int(self.driver.find_element(By.XPATH, self.infrastructure_offline_host_xpath).text)
        stale = int(self.driver.find_element(By.XPATH, self.infrastructure_stale_host_xpath).text)
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

    def verify_infrastructure_services(self):
        total_service = int(self.driver.find_element(By.XPATH, self.infrastructure_total_service_xpath).text)
        ok = int(self.driver.find_element(By.XPATH, self.infrastructur_service_ok_xpath).text)
        warn = int(self.driver.find_element(By.XPATH, self.infrastructur_service_warning_xpath).text)
        critical = int(self.driver.find_element(By.XPATH, self.infrastructur_service_critical_xpath).text)
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
            print(Color.GREEN + "Infrastructure Services count is succssfully matched with ok,warn,crit" + Color.END)
        else:
            print(Color.RED + "Infrastructure Services count is not matched with ok,warn,crit" + Color.END)
