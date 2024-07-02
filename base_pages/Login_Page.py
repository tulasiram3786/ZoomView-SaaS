import time

from selenium.webdriver.common.by import By

class Zoomview_Login_Page:

    landingpage_loginbutton_xpath = "(//span[text()='Login'])[1]"
    textbox_Email_xpath = "//input[@name='email']"
    textbox_Password_xpath = "//input[@name='password']"
    button_login_xpath = "//span[text()='Log in']"
    button_logout_xpath1 = "//span[@class='ant-menu-title-content']//p"
    button_logout_xpath2 = "//article[text()='Logout']"


    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.textbox_Email_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_Email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath1).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.button_logout_xpath2).click()
        time.sleep(2)
        self.driver.refresh()
        self.driver.get("https://zoomview.zybisys.com/login")


