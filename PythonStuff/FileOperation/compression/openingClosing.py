import os
import zipfile
import shutil

os.chdir('../test')

newZip = zipfile.ZipFile('myzip.zip')
print('Name Lists', newZip.namelist())
indexInfo = newZip.getinfo(newZip.namelist()[1])
print('index info size:', indexInfo.file_size)
print('index info compressed size:', indexInfo.compress_size)
newZip.close()
shutil.copy('myzip.zip', 'new.zip')
new = zipfile.ZipFile('new.zip')

# extract all to extract the entire zip
new.extractall('zipping/zipnew')
# extract to extract a particular file in zip
new.extract(new.namelist()[1], 'zipping')

