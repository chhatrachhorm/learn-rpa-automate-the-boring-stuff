#! python3
# program to
# find the total of pop per county and
# organize the data in pop per county in each state

import openpyxl
import pprint

wb = openpyxl.load_workbook('../files/censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

countyData = {}
print('Reading...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    # set default of keys if non-exist
    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {
        'tracts': 0, 'pop': 0
    })
    # increase tracts and add pop for each county in the state
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

print('Writing result...')
res = open('censusUSA2010.py', 'w')
res.write('data = ' + pprint.pformat(countyData))
res.close()
print('Done')

