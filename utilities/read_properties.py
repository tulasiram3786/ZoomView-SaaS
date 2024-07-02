import configparser
from utilities import random as Random

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:

    ######################### login page ###########################

    @staticmethod
    def get_loginpage_url():
        url=config.get('zoomview login info','loginpage_url')
        return url

    @staticmethod
    def get_email():
        email = config.get('zoomview login info', 'email')
        return email

    @staticmethod
    def get_password():
        password = config.get('zoomview login info', 'password')
        return password

    @staticmethod
    def get_invalid_email():
        invalidemail = config.get('zoomview login info', 'invalid_email')
        return invalidemail

    @staticmethod
    def get_invalid_password():
        invalidpassword = config.get('zoomview login info', 'invalid_password')
        return invalidpassword

    ######################### signup page ###########################

    @staticmethod
    def get_signuppage_url():
        url = config.get('zoomview signup info', 'signuppage_url')
        return url

    @staticmethod
    def get_signuppage_firstname():
        firstname = config.get('zoomview signup info', 'firstname')
        return firstname

    @staticmethod
    def get_signuppage_lastname():
        lastname = config.get('zoomview signup info', 'lastname')
        return lastname

    @staticmethod
    def get_signuppage_email():
        email = Random.generate_random_email()
        return email

    @staticmethod
    def get_signuppage_companyname():
        companyname = config.get('zoomview signup info', 'companyname')
        return companyname

    @staticmethod
    def get_signuppage_phonenumber():
        phonenumber = Random.generate_random_phone_number()
        return phonenumber

    @staticmethod
    def get_signuppage_designation():
        designation = config.get('zoomview signup info', 'designation')
        return designation

    @staticmethod
    def get_signuppage_createpassword():
        createpassword = config.get('zoomview signup info', 'createpassword')
        return createpassword

    @staticmethod
    def get_signuppage_conformpassword():
        conformpassword = config.get('zoomview signup info', 'conformpassword')
        return conformpassword

    ########################### Forgot password page ###############################

    @staticmethod
    def get_forgotpasswordpage_url():
        url = config.get('zoomview forgotpassword info', 'forgotpasswordpage_url')
        return url

    @staticmethod
    def get_forgotpassword_email():
        fp_email = config.get('zoomview forgotpassword info', 'email')
        return fp_email