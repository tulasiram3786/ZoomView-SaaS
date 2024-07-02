
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC






class Zoho_email:

    def __init__(self,driver):
        self.driver = driver

    # customer_button_xpath = "(//a[text()='Customer'])"
    # table_first_row_xpath = "(//tr[@class='ant-table-row ant-table-row-level-0'])[1]"
    # table_action_button_xpath = "(//tr[@class='ant-table-row ant-table-row-level-0'])[1]//td[7]"


    def signup_for_zoho(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.driver.get("https://www.zoho.com/mail/login.html")
        # self.driver.get("https://dev.zybisys.com/verify-user/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9idWxlc3UyNzFAZ21haWwuY29tIiwiaWF0IjoxNzE3MDUxNTczLCJleHAiOjE3MTcwNTUxNzN9.v21vmdUNl11qFuupgGADJqe15nfaS4QH7hMdNyvk1m8")
        self.driver.maximize_window()
        time.sleep(5)
        signup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@class='zwelcome-info']//a)[1]")))
        signup.click()
        # self.driver.find_element(By.XPATH, "(//a[text()='SIGN IN'])[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='login_id']").click()
        self.driver.find_element(By.XPATH, "//input[@id='login_id']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='login_id']").send_keys("tulasiram.r@zybisys.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='password']").click()
        self.driver.find_element(By.XPATH, "//input[@id='password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("1Xbet@3786")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@id='nextbtn']//span[text()='Sign in']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='I Understand']").click()
        time.sleep(15)
        # self.driver.find_element(By.XPATH, "//a[text()='I Understand']").click()
        self.driver.implicitly_wait(20)
        self.driver.find_element(By.XPATH, "//div[contains(@role,'tablist')]//button[contains(@aria-label,'Mail')]").click()
        time.sleep(15)

        self.iframe_locator = (By.XPATH, "//iframe[contains(@id,'mailIframe')]")
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(self.iframe_locator))
        time.sleep(5)

        self.mail_button_xpath = (By.XPATH, "(//ul[@class='zmApps']//li)//i[@class='msi-mailApp zmDoubleIcon']")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.mail_button_xpath)).click()
        time.sleep(10)

        self.inbox_xpath = (By.XPATH, "((//div[@class='zmTreeText'])//span[contains(@data-testid,'lhs-node-txt') or text()='Inbox'])[3]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.inbox_xpath)).click()
        time.sleep(10)

        self.email_subject_locator = (By.XPATH, "(//span[contains(text(), 'Staging Customer Verification')])[1]")  # Update the subject text accordingly
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.email_subject_locator)).click()
        time.sleep(10)

        self.verification_link_locator = (By.XPATH, "//div[contains(@class,'jsConTent ')]")  # Update the link text accordingly
        data = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.verification_link_locator))
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", data)
        data.click()


    def signup_for_zoho_for_verify_otp(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--disable-notifications")
        # self.driver = webdriver.Chrome(options=chrome_options)
        # # self.driver = webdriver.Chrome()
        # self.driver.get("https://www.zoho.com/mail/login.html")
        # # self.driver.get("https://dev.zybisys.com/verify-user/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im9idWxlc3UyNzFAZ21haWwuY29tIiwiaWF0IjoxNzE3MDUxNTczLCJleHAiOjE3MTcwNTUxNzN9.v21vmdUNl11qFuupgGADJqe15nfaS4QH7hMdNyvk1m8")
        # self.driver.maximize_window()
        time.sleep(2)
        signup = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='zwelcome-info']//a)[1]")))
        signup.click()
        # self.driver.find_element(By.XPATH, "(//a[text()='SIGN IN'])[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='login_id']").click()
        self.driver.find_element(By.XPATH, "//input[@id='login_id']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='login_id']").send_keys("tulasiram.r@zybisys.com")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[text()='Next']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='password']").click()
        self.driver.find_element(By.XPATH, "//input[@id='password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("1Xbet@3786")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@id='nextbtn']//span[text()='Sign in']").click()
        time.sleep(3)
        # self.driver.find_element(By.XPATH, "//a[text()='I Understand']").click()
        # time.sleep(15)
        self.driver.find_element(By.XPATH, "//div[contains(@role,'tablist')]//button[contains(@aria-label,'Mail')]").click()
        time.sleep(15)

        self.iframe_locator = (By.XPATH, "//iframe[contains(@id,'mailIframe')]")
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(self.iframe_locator))
        time.sleep(5)

        self.mail_button_xpath = (By.XPATH, "(//ul[@class='zmApps']//li)//i[@class='msi-mailApp zmDoubleIcon']")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.mail_button_xpath)).click()
        time.sleep(20)

        # self.inbox_xpath = (By.XPATH, "((//div[@class='zmTreeText zmBold'])//span[contains(@data-testid,'lhs-node-txt') or text()='Inbox'])[3]")
        # WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.inbox_xpath)).click()
        # time.sleep(20)

        self.inbox_xpath = (By.XPATH, "//span[text()='Inbox']")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.inbox_xpath)).click()
        time.sleep(20)

        self.email_subject_locator = (By.XPATH, "(//span[contains(text(), 'Staging Customer Verification')])[1]")  # Update the subject text accordingly
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.email_subject_locator)).click()
        time.sleep(10)

        # self.verification_link_locator = (By.XPATH, "//div[contains(@class,'jsConTent ')]")  # Update the link text accordingly
        # data = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.verification_link_locator))
        # time.sleep(1)
        # self.driver.execute_script("arguments[0].scrollIntoView();", data)
        # data.click()


    def extract_otp(self):
        otp_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'jsConTent ')]")))
        otp_text = otp_element.text
        print("otp:", otp_text)
        otp = ''.join(filter(str.isdigit, otp_text))
        print("one time password is:", otp)
        return otp
        # print("one time password is:", otp)
        # return otp


    def close_current_window(self):
        self.driver.close()