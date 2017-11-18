import shutil
import os
# to copy, move, rename and delete

# copy
fpath = '../test/index.js'
dpath = '../test/organizing'
npath = '../test/organizing/newIndexName.js'
shutil.copy(fpath, dpath)
shutil.copy(fpath, npath)

# copy entire folder into a new one
shutil.copytree('../test', '../test/new')

# moving - file and folder
shutil.move(fpath, '../test/move/index.js')
shutil.move('../test/move/index.js', '../test/index.js')

# permanent deletion
# os.unlink(path) => delete file
# os.rmdir(path) => remove empty folder
# shutil.rmtree(path) => remove everything
for i in range(10):
    temp = open('../test/a' + str(i) + '.jkl', 'w')
    temp.write('Something')
    temp.close()

for filename in os.listdir('../test'):
    if filename.endswith('.jkl'):
        os.unlink('../test/'+filename)
