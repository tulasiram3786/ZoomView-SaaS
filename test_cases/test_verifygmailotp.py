import imaplib
import email
from email.header import decode_header
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_verifygmailotp:
    EMAIL = "tulasiram1706@gmail.com"
    PASSWORD = "Tulasi@1705"
    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993

    def get_otp_from_email(self):
        try:
            mail = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT)
            mail.login(self.EMAIL, self.PASSWORD)
            mail.select("inbox")

            status, messages = mail.search(None, 'ALL')
            mail_ids = messages[0].split()

            for mail_id in mail_ids[::-1]:
                status, msg_data = mail.fetch(mail_id, "(RFC822)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        if msg["subject"] == "Staging Customer Verification":
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode()
                                    otp = body.split("otp is ")[-1]
                                    return otp.strip()
            return None
        except imaplib.IMAP4.error as e:
            print(f"IMAP error: {e}")
            return None

    def test_get_otp_from_email(self):
        otp = self.get_otp_from_email()
        assert otp is not None, "OTP not found in email"
        self.otp = otp

    def test_enter_otp_into_web_form(self):
        # Ensure test_get_otp_from_email is executed before this test
        if not hasattr(self, 'otp'):
            self.test_get_otp_from_email()

        if hasattr(self, 'otp'):
            driver = webdriver.Chrome()
            driver.get("https://zoomview.zybisys.com/forgot-password")
            driver.maximize_window()
            time.sleep(2)

            otp_input_boxes = driver.find_elements(By.XPATH, "//input[@maxlength='1']")
            for i, char in enumerate(self.otp):
                otp_input_boxes[i].send_keys(char)

            driver.find_element(By.XPATH, "//button[text()='Submit']").click()
            time.sleep(2)

            # Add assertions or further steps as needed

            driver.quit()
        else:
            print("OTP was not set. Exiting test.")


if __name__ == "__main__":
    test = Test_verifygmailotp()
    test.test_get_otp_from_email()
    test.test_enter_otp_into_web_form()
