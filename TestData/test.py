#encoding=utf-8
import os
#获取工程所在目录的绝对路径
'''
print __file__
print os.path.dirname(__file__)
print os.path.dirname(os.path.dirname(__file__))
print os.path.dirname(os.path.abspath(__file__))
project_path= os.path.dirname(os.path.abspath(__file__))
print "project_path:",project_path
'''
project_path= os.path.dirname(os.path.abspath(__file__))
print project_path
print project_path.decode('utf-8')+u"\\126邮箱联系人.xlsx"