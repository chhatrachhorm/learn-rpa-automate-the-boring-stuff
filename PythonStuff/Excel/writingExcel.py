import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

# rename the default sheet's name
sheet.title = 'KIT FILE DEMO'
print('Sheet names', wb.get_sheet_names())

wb.create_sheet(index=0, title='First Sheet')
print('Sheet names', wb.get_sheet_names())


# updating values is just like updating object/dictionary
currentSheet = wb.get_sheet_by_name('First Sheet')
currentSheet['A1'].value = 'This is ABS'

wb.save('files/example.xlsx')

