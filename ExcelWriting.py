'''
Created on 18-Jul-2017

@author: BALASUBRAMANIAM
'''
from openpyxl import Workbook
import calendar

filepath="G:/test/orangereport_2017.xlsx"
wb=Workbook()
i=0
for month in calendar.month_name:
    if not(len(str(month))==0):
        print(month)
        wb.create_sheet(month+"_2017", i)
        i+=1
wb.save(filepath)