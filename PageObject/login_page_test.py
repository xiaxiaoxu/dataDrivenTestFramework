#encoding=utf-8
#author-夏晓旭
# encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.login_page_items = self.parse_config_file.getItemsFromSection(
            "126mail_login")
        print self.login_page_items

    def frame(self):
        locateType, locateExpression = self.login_page_items['login_page.frame'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def username(self):
        locateType, locateExpression = self.login_page_items['login_page.username'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def password(self):
        locateType, locateExpression = self.login_page_items['login_page.password'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def loginbutton(self):
        locateType, locateExpression = self.login_page_items['login_page.loginbutton'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

    def username_clear(self):
        self.username().clear()

    def username_input(self, value):
        self.username().send_keys(value)

    def password_input(self, value):
        self.password().send_keys(value)

    def loginbutton_click(self):
        self.loginbutton().click()

    def login(self):
        self.driver.switch_to.frame(self.frame())
        self.username_clear()
        self.username_input('testman1980')
        self.password_input('wulaoshi1978')
        self.loginbutton_click()



if __name__=='__main__':
    from selenium import webdriver
    driver=webdriver.Firefox(executable_path='c:\\geckodriver')
    driver.get('http:\\mail.126.com')
    login_t=LoginPage(driver)
    login_t.login()



