#encoding=utf-8
import os
#获取工程所在目录的绝对路径
'''
print __file__
print os.path.dirname(__file__)
print os.path.dirname(os.path.dirname(__file__))
print os.path.dirname(os.path.abspath(__file__))
'''
project_path=os.path.dirname(os.path.dirname(__file__))
print "project_path:",project_path

#获取页面对象库文件的绝对路径
page_object_repository_path=project_path.decode("utf-8")+u"/conf/PageObjectRepository.ini"

#测试数据excel文件的绝对路径
test_data_excel_path=project_path.decode("utf-8")+u"/TestData/126邮箱联系人.xlsx"
username_col_no=1
password_col_no=2
is_executed_col_no=4
test_result_col_no=6
assert_keyword_col_no=6

if __name__=='__main__':
    print project_path
    print page_object_repository_path
    print test_data_excel_path
    print os.path.exists(page_object_repository_path)
    print os.path.exists(test_data_excel_path)