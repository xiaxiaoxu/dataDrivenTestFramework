#encoding=utf-8
from selenium import webdriver
from Util.Log import *
from Util.FormatTime import *
import time
from PageObject.login_page import *
from PageObject.home_page import *
def login(driver,username, password):
    #time.sleep(2)
    lp = LoginPage(driver)
    lp.login(username, password)
    info("login successfully!")
    print date_time_chinese()

if __name__=="__main__":
    driver = webdriver.Firefox(executable_path="c:\\geckodriver")
    login(driver, "testman1980", "wulaoshi1978")
