#encoding=utf-8
#author-夏晓旭
#encoding=utf-8
from selenium import webdriver
from Util.Log import *
from Util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
from PageObject.addressBook import *
from Util.Excel import *
from ProjectVar.var import *

def add_contact(driver,name="",email="",is_star=True,mobile="",other_info=""):
    ap= AddressPage(driver)
    ap.add_contact_button().click()
    time.sleep(2)
    ap.contact_name().send_keys(name)
    ap.contact_email().send_keys(email)
    if is_star== "True":
        ap.contact_is_star().click()
    ap.contact_mobile().send_keys(mobile)
    ap.contact_other_info().send_keys(other_info)
    ap.contact_save_button().click()
    time.sleep(3)


if __name__=="__main__":
    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    login(driver,"testman1980", "wulaoshi1978")
    visit_address_page(driver)
    add_contact(driver,"fosterwu","201773733@qq.com",True,"13533333333",u"光荣之路")
    driver.quit()