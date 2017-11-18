import requests
import bs4
# to install bs4 - pip install beautifulsoup4

# download or open html from storage
res = requests.get('https://i-out.io')
res.raise_for_status()
# pass text to bs4
demoSoup = bs4.BeautifulSoup(res.text, "lxml")


# for local html file
# myFile = open('index.html')
# mySoup = bs4.BeautifulSoup(myFile.read())

# soup will help finding element with select
# https://automatetheboringstuff.com/chapter11/

element = demoSoup.select('#app')  # array will be return
print(element[0].attrs)


