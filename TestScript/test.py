#encoding=utf-8
from selenium import webdriver
from Util.Log import *
from Util.FormatTime import *
import time
from Action.visit_address_page import *
from Action.add_contact import *
from Action.login import *
from ProjectVar.var import *
import sys
reload(sys)
sys.setdefaultencoding("utf8")

pe = parseExcel(test_data_excel_path)
pe.set_sheet_by_index(1)
print pe.get_default_sheet()
#获取第一个sheet的所有行
rows= pe.get_all_rows()
print "rows:",rows
#遍历每一行
for id,row in enumerate(rows):
    print id,row
