# load XKCD home page
# save comic image on that page
# use prev btn
# download until the first one
# http://xkcd.com/#


import requests
import os
import bs4

# the image is in img tag under div tag with id = "comic"
# when the prev btn click, the url will change according to
# comic pic => http://xkcd.com/#

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Start downloading')

    try:
        print('Downloading in %s...' % url)
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text)

        element = soup.select('#comic img')
        if element == []:
            print('No image found')
        else:
            try:
                comicUrl = 'http:' + element[0].get('src')
                print('Downloading from url %s' % comicUrl)
                res = requests.get(comicUrl)
                res.raise_for_status()

                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
                for chuck in res.iter_content(100000):
                    imageFile.write(chuck)
                imageFile.close()
                prevLink = soup.select('a[rel="prev"]')[0]
                url = 'http://xkcd.com' + prevLink.get('href')
            except Exception as exc:
                # skip image
                print(exc)
                prevLink = soup.select('a[rel="prev"]')[0]
                url = 'http://xkcd.com' + prevLink.get('href')
                continue
    except Exception as e:
        print(e)

print('Finish Downloading')
