# import imaplib
# import email
# import re
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Function to connect to Gmail and fetch OTP
# def get_otp_from_email(username, password):
#     try:
#         mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
#         mail.login(username, password)
#         mail.select("inbox")
#
#         status, messages = mail.search(None, 'UNSEEN')
#         mail_ids = messages[0].split()
#
#         for mail_id in mail_ids[::-1]:
#             status, msg_data = mail.fetch(mail_id, "(RFC822)")
#             for response_part in msg_data:
#                 if isinstance(response_part, tuple):
#                     msg = email.message_from_bytes(response_part[1])
#                     if "Staging Customer Verification" in msg["subject"].lower():
#                         for part in msg.walk():
#                             if part.get_content_type() == "text/plain":
#                                 body = part.get_payload(decode=True).decode()
#                                 # Extract OTP using regex
#                                 otp = re.findall(r'\d+', body)
#                                 if otp:
#                                     return otp[0]
#         return None
#     except imaplib.IMAP4.error as e:
#         print(f"IMAP error: {e}")
#         return None
#
# # Function to automate the web form submission
# def enter_otp_into_web_form(otp):
#     driver = webdriver.Chrome()
#     driver.get("https://zoomview.zybisys.com/forgot-password")
#     driver.maximize_window()
#     time.sleep(2)
#
#     otp_input_boxes = driver.find_elements(By.XPATH, "//input[contains(@aria-label, 'character')]")
#     for i, char in enumerate(otp):
#         otp_input_boxes[i].send_keys(char)
#
#     driver.find_element(By.XPATH, "//button[text()='Submit']").click()
#     time.sleep(2)
#
#     # Add assertions or further steps as needed
#
#     driver.quit()
#
# # Directly setting the properties
# email_username = 'tulasiram1706@gmail.com'
# email_password = 'Tulasi@1705'
#
# # Get OTP from email
# otp = get_otp_from_email(email_username, email_password)
# if otp:
#     print(f"Retrieved OTP: {otp}")
#     # Enter OTP into web form
#     enter_otp_into_web_form(otp)
# else:
#     print("No OTP received")


import imaplib
import email
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Function to connect to Gmail and fetch OTP
def get_otp_from_email(username, app_password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(username, app_password)
        mail.select("inbox")

        status, messages = mail.search(None, 'UNSEEN')
        mail_ids = messages[0].split()

        for mail_id in mail_ids[::-1]:
            status, msg_data = mail.fetch(mail_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    if "Staging Customer Verification" in msg["subject"].lower():
                        for part in msg.walk():
                            if part.get_content_type() == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                # Extract OTP using regex
                                otp = re.findall(r'\d+', body)
                                if otp:
                                    return otp[0]
        return None
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
        return None

# Function to automate the web form submission
def enter_otp_into_web_form(otp):
    driver = webdriver.Chrome()
    driver.get("https://zoomview.zybisys.com/forgot-password")
    driver.maximize_window()
    time.sleep(2)

    otp_input_boxes = driver.find_elements(By.XPATH, "//input[@maxlength='1']")
    for i, char in enumerate(otp):
        otp_input_boxes[i].send_keys(char)

    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(2)

    # Add assertions or further steps as needed

    driver.quit()

# Directly setting the properties
email_username = 'tulasiram1706@gmail.com'
app_password = 'qnwv wblu mxwu xhfq '

# Get OTP from email
otp = get_otp_from_email(email_username, app_password)
if otp:
    print(f"Retrieved OTP: {otp}")
    # Enter OTP into web form
    enter_otp_into_web_form(otp)
else:
    print("No OTP received")

