import os

# get file size
print(os.path.getsize('./test/index.js'))
# get list of file
print(os.listdir(os.getcwd()))

# checking path validity
print(os.path.exists(os.getcwd()))
print(os.path.isdir(os.getcwd()))
print(os.path.isfile(os.getcwd()))

# Opening file with open() and Read with Read()
love = open('./test/miss.txt')
read = love.read()
print(read)

# Writing a file
# rewrite mode
changeLove = open('./test/miss.txt', 'w')
changeLove.write('I am fine')
changeLove.close()
# append mode
changeLove = open('./test/miss.txt', 'a')
changeLove.write('\nStill alive, sorry')
changeLove.close()
