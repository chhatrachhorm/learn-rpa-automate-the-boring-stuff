import send2trash
myFile = open('../test/missyou.txt', 'a')
myFile.write('really miss you')
myFile.close()

send2trash.send2trash('../test/missyou.txt')

