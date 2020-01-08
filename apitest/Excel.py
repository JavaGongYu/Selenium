import xlrd
excelDir = r"F:\ExcelTest.xlsx"
workbook=xlrd.open_workbook(excelDir)
# print(workbook.sheet_names()) #打印Sheet名
worksheet=workbook.sheet_by_name('手机号归属地查询')
# print(worksheet.row_values(1)) # 读取第一行
VData=worksheet.cell(1,3).value
print(VData)