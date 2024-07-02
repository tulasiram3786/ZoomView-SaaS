from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.NAME, 'first_name')
        self.first_name_error = (By.XPATH,"//span[text()='Enter valid first name']")

    def enter_first_name(self, first_name):
        first_name_elem = self.driver.find_element(*self.first_name_field)
        first_name_elem.clear()
        first_name_elem.send_keys(first_name)

    def submit_form(self):
        first_name_elem = self.driver.find_element(*self.first_name_field)
        first_name_elem.send_keys(Keys.RETURN)  # Submit the form by pressing Enter

    def is_first_name_validation_message_displayed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.first_name_error)
            )
            return True
        except:
            return False
