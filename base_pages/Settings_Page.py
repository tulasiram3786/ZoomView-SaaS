import random
import time
from selenium.webdriver.common.by import By

class Zoomview_Settings_Page:

    text_settings_dropdown_xpath = "(//span[text()='Settings'])[1]"
    link_settings_dropdown_notifications_xpath = "//a[text()='Notifications']"
    button_addemail_xpath = "//span[text()='ADD EMAILS +']"
    textbox_enteremail_xpath = "//input[contains(@name,'email')]"
    button_save_xpath = "//button[@type='button']//span[text()='SAVE ']"
    email_toastmessage_xpath = "//div[text()='Inserted Successfully']"
    button_remove_xpath = "(//p[text()='REMOVE'])[1]"
    button_delete_xpath = "//span[text()='Delete']"

    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def click_settings_dropdown(self):
        self.driver.find_element(By.XPATH,self.text_settings_dropdown_xpath).click()


    def click_settings_notification(self):
        self.driver.find_element(By.XPATH,self.link_settings_dropdown_notifications_xpath).click()

    def enter_settings_email(self,email):
        self.driver.find_element(By.XPATH,self.textbox_enteremail_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_enteremail_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_enteremail_xpath).send_keys(email)

    def click_addemails(self):
        self.driver.find_element(By.XPATH,self.button_addemail_xpath).click()

    def click_savebutton(self):
        self.driver.find_element(By.XPATH,self.button_save_xpath).click()

    def click_removebutton(self):
        self.driver.find_element(By.XPATH,self.button_remove_xpath).click()

    def click_deletebutton(self):
        self.driver.find_element(By.XPATH,self.button_delete_xpath).click()



