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

    text_lamauat_system_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='System']//following-sibling::p)[1]"
    text_lamauat_Database_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Database']//following-sibling::p)[1]"
    text_lamauat_Application_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Application']//following-sibling::p)[1]"
    text_lamauat_Network_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Network']//following-sibling::p)[1]"

    text_lamaprod_system_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='System']//following-sibling::p)[2]"
    text_lamaprod_Database_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Database']//following-sibling::p)[2]"
    text_lamaprod_Application_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Application']//following-sibling::p)[2]"
    text_lamaprod_Network_xpath = "(//div[@class='flex gap-1 justify-center items-center']//descendant::p[text()='Network']//following-sibling::p)[2]"






