#! python3

# program to open all the possible links from the google search
# to run: crazy your_query

import requests
import sys
import webbrowser
import bs4
import pyperclip


def crazy_search(query):
    print('https://google.com/search?q=' + query)
    try:
        res = requests.get('https://google.com/search?q=' + query)
        res.raise_for_status()
        # each result link will contains in .r class > a tag
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        links = soup.select('.r a')
        for i in range(len(links)):
            webbrowser.open('http://google.com' + links[i].get('href'))
    except Exception as exc:
        print('Error occur: %s' % exc)


print('Googling...')
if len(sys.argv) > 1:
    crazy_search(''.join(sys.argv[1:]))
else:
    crazy_search(pyperclip.paste())

