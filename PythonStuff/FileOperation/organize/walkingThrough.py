import os
for foldername, subfolders, filenames in os.walk(os.path.realpath('..')):
    print('current folder \'s name is', foldername)

    for subfolder in subfolders:
        print('Sub folder of' + foldername + ": " + subfolder)

    for filename in filenames:
        print('File inside ' + foldername + ': ' + filename)
