#encoding=utf-8
from selenium import webdriver
from Util.Log import  *
from Util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
from login import *

#driver = webdriver.Chrome(executable_path="e:\\chromedriver")
#login(driver, "testman1980", "wulaoshi1978")

def visit_address_page(driver):
    hp = HomePage(driver)
    time.sleep(5)
    hp.address_book_page_link().click()
    time.sleep(5)

if __name__=="__main__":
    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    login(driver,"xiaxiaoxu1987", "gloryroad")
    visit_address_page(driver)