import os


# to correctly specify the path \ or \\ or /
print(os.path.join('h', 'f', 'k'))
# get current working directory
print(os.getcwd())
# change directory
os.chdir(os.getcwd()+'\\test')
print(os.getcwd())
# create a new directory
# os.mkdir(os.getcwd()+'\\test')

# handling absolute path with os.path
# to return absolute path
print(os.path.abspath('.'))
# to check is it's an abs path
print(os.path.isabs('.'))
# to return relative path(desiredPath, startingPath)
print(os.path.relpath('PythonStuff', 'test'))


# dirname and basename and split
print(os.path.dirname(os.getcwd()))
print(os.path.basename(os.getcwd()))
print(os.path.split(os.getcwd()))
