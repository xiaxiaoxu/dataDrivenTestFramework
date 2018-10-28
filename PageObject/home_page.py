#encoding=utf-8
import time
from Util.ObjectMap import *
from Util.ParsePageObjectRepository import ParsePageObjectRepositoryConfig
from Action.login import *
class HomePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.parse_config_file=ParsePageObjectRepositoryConfig()
        self.login_page_items=self.parse_config_file.getItemsFromSection(
            "126mail_homepage")
        print self.login_page_items

    def address_book_page_link(self):
        locateType, locateExpression = self.login_page_items['home_page.addressbook'].split(">")
        print locateType, locateExpression
        return getElement(self.driver, locateType, locateExpression)

if __name__=="__main__":
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    login(driver, "xiaxiaoxu1987", "gloryroad")
    hp=HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(5)
