import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 2500
sheet['A2'] = 2563
sheet['A3'] = 2646
sheet['A4'] = '=SUM(A1:A3)'
wb.save('files/formulate.xlsx')
