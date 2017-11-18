import csv

mcsv = open('files/example.csv')
mreader = csv.reader(mcsv)
# reading from reader obj
for row in mreader:
    print('Row ', str(mreader.line_num) + ' ' + str(row))

# Alternative Way
# data = list(mreader)  # 2D array
# print('Data', data)
