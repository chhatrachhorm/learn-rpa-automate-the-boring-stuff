# create a reference obj from a rectangular
# create element objects
# create a chart obj
# append element obj to chart obj
# add chart to workbook obj

# create a bar
import openpyxl
wb = openpyxl.Workbook()

sheet = wb.active
for i in range(1, 15):
    sheet['A' + str(i)] = i

# min_col, min_row => data to be started
# max_col, max_row => data to be ended with
ref = openpyxl.chart.Reference(
    sheet,
    min_col=1,
    min_row=1,
    max_col=1,
    max_row=14
)
seriesObj = openpyxl.chart.Series(ref, title='Demo Bar')

chartObj = openpyxl.chart.BarChart()
chartObj.title = 'My Bar'
chartObj.append(seriesObj)
sheet.add_chart(chartObj, 'C6')
wb.save('files/chartBarDemo.xlsx')
