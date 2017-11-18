import zipfile
import os

os.chdir('../test')
# to zip index.html to myzip.zip by using 'w'
# to add file to myzip.zip use 'a'

newZip = zipfile.ZipFile('myzip.zip', 'w')
newZip.write('index.html', compress_type=zipfile.ZIP_DEFLATED)