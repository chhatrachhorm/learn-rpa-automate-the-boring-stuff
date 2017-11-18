import openpyxl

wb = openpyxl.load_workbook('files/account.xlsx')
print(wb.get_sheet_names())

# each sheet has its own worksheet object
accountSheet = wb.get_sheet_by_name('account')

# accessing with column and row's names

# get sheet's cell's values
# A is the col, 1 is the row
print(accountSheet['A1'].value)

# cell object
shell = accountSheet['B2']
print(str(shell.row) + ' ' + str(shell.column) + ' ' + shell.value)
print('coordinate is', shell.coordinate)


# accessing with cell(row, col)
# for i in range(start, end, step)
for i in range(1, 20):
    print(i, accountSheet.cell(row=i, column=2).value)

# looping via rowOfCellObj and cellObj
print('******')
for rowOfCellObjects in accountSheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('******')


