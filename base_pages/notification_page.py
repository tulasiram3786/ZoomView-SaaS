from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NotificationPage:
    def __init__(self, driver):
        self.driver = driver
        self.notification_locator = (By.CLASS_NAME, "notification-class")  # Update with actual locator
        self.close_button_locator = (By.CLASS_NAME, "notification-close-button")  # Update with actual locator

    def wait_for_notification(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.notification_locator)
            )
            self.driver.find_element(*self.close_button_locator).click()
        except:
            pass  # If no notification is found, continue without interruption