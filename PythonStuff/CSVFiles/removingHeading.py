#! python3
# program to remove heading in csv files

import csv
import os
import zipfile

# make new dir
os.makedirs('files/afterRemove', exist_ok=True)
os.makedirs('files/beforeRemove', exist_ok=True)

# extract all csv files from its zip
oldCsv = zipfile.ZipFile('files/removeCsvHeader.zip')
oldCsv.extractall('files/beforeRemove')

os.chdir('files/beforeRemove')
for file in os.listdir('.'):
    if not file.endswith('.csv'):
        continue
    print('Removing header from ' + file + '...')
    # read csv file in skipping first row
    csvRows = []
    csvFileObj = open(file)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()
    # write csv file
    csvFileObj = open(os.path.join('../afterRemove', file), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()





