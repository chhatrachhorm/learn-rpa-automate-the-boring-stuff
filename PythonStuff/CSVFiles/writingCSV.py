import csv
out = open('files/new.csv', 'w', newline='')
outWriter = csv.writer(out)
outWriter.writerow(['hello', 'world', 'miss'])
outWriter.writerow([156, 45646, 6.5, 464])
out.close()
