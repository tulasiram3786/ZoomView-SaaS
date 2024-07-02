import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Gmail_Email:

    def __init__(self,driver):
        self.driver = driver

    def signup_for_gmail(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--disable-notifications")
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        #self.driver.get("https://accounts.google.com/")
        # self.driver.get("https://dev.zybisys.com/verify-user/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9idWxlc3UyNzFAZ21haWwuY29tIiwiaWF0IjoxNzE3MDUxNTczLCJleHAiOjE3MTcwNTUxNzN9.v21vmdUNl11qFuupgGADJqe15nfaS4QH7hMdNyvk1m8")
        # self.driver.maximize_window()
        #time.sleep(5)


        self.driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']").click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']").clear()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Email or phone']").send_keys("tulasiram1706@gmail.com")

        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Next']").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//div[text()='Enter your password']").click()
        self.driver.find_element(By.XPATH, "//div[text()='Enter your password']").clear()
        self.driver.find_element(By.XPATH, "//div[text()='Enter your password']").send_keys("Tulasi@1705")

        time.sleep(2)
        self.driver.find_element(By.XPATH,"//span[text()='Next']").click()
        time.sleep(4)

        self.driver.find_element(By.XPATH,"//a[@aria-label='Google apps']").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH,"//span[@data-text='Gmail']").click()
        time.sleep(2)


