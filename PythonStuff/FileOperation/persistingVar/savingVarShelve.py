import shelve

# saving
mData = shelve.open('../test/ser/myData')
fav = ['espresso', 'dogs', 'mockito', 'badminton', 'vanilla', 'salty']
mData['fave'] = fav
mData.close()

# manipulating
mVar = shelve.open('./test/ser/myData')
print(list(mVar.keys()))
print(list(mVar.values()))
print(mVar['fave'])

