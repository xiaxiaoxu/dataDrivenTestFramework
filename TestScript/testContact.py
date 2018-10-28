#encoding=utf-8
from selenium import webdriver
from Util.Log import *
from Util.FormatTime import *
import time
from Action.visit_address_page import *
from Action.add_contact import *
from Action.login import *
from ProjectVar.var import *
from Util.Excel import *
import sys
reload(sys)
sys.setdefaultencoding("utf8")

pe = parseExcel(test_data_excel_path)
pe.set_sheet_by_index(0)
#获取第一个sheet的所有行
rows = pe.get_all_rows()
for id,row in enumerate(rows[1:]):
    #print id,row
    if row[4].value.lower() == "y":
        print row[1].value
        print row[2].value
        username = row[1].value
        password = row[2].value
        driver = driver=webdriver.Firefox(executable_path="c:\\geckodriver")

        try:
            result = True
            login(driver,username,password)
            visit_address_page(driver)
            pe.set_sheet_by_index(1)
            data_rows = pe.get_all_rows()
            for data_row in data_rows[1:]:
                if data_row[7].value.lower() ==  "y":
                    try:
                        print data_row[1].value,data_row[2].value,data_row[3].value,data_row[4].value,data_row[5].value
                        add_contact(driver, name=data_row[1].value, email=data_row[2].value, is_star=data_row[3].value, mobile=data_row[4].value, other_info=data_row[5].value)
                        #data_row[8].value = date_time_chinese()
                        data_row[9].value = u"成功"
                    except Exception,e:
                        #data_row[8].value = date_time_chinese()
                        data_row[9].value = u"失败"
                        print e
                        result = False
                else:
                    #data_row[8].value = date_time_chinese()
                    data_row[9].value = u"忽略"
                if result:
                    pe.set_sheet_by_index(0)
                    pe.write_cell_content(id + 2, 6, u"成功")
                    assert data_row[6] in driver.page_source
                else:
                    pe.set_sheet_by_index(0)
                    pe.write_cell_content(id + 2, 6, u"失败")

        except Exception,e:
            print e
            pe.set_sheet_by_index(0)
            pe.write_cell_content(id + 2, 6, u"失败")


        #pe.write_cell_content(id + 2, 6, u"成功")
        #pe.save_excel_file()
    else:
        print "this case is ignored！"
        pe.write_cell_content(id + 2, 6, u"忽略")
        pe.save_excel_file()
    #driver.quit()