import pprint


# saving
fav = [
    {'type': 'food', 'lists': ['ice-cream', 'beacon', 'vanilla'], 'desc':'so cute'},
    {'type': 'pet', 'lists': ['dogs', 'not insect'], 'desc': 'am scared'}
]
print(pprint.pformat(fav))
Fav = open('../test/ser/hFav.py', 'w')
Fav.write('fav = ' + pprint.pformat(fav) + '\n')
Fav.close()


