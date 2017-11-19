#! python3

import requests
import os
import bs4
import threading

os.makedirs('files', exist_ok=True)
os.makedirs('files/downloaded', exist_ok=True)


def downloader(start_comic, end_comic):
    for urlNumber in range(start_comic, end_comic):
        print('Downloading page http://xkcd.com/%s ...' % urlNumber)
        try:
            res = requests.get('http://xkcd.com/%s' % urlNumber)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'lxml')

            element = soup.select('#comic img')
            if element == []:
                print('Could not find comic image')
            else:
                url = 'http:' + element[0].get('src')
                print('Downloading image %s...' % url)
                try:
                    img = requests.get(url)
                    img.raise_for_status()
                    file = open(os.path.join('files/downloaded', os.path.basename(url)), 'wb')
                    for chunk in img.iter_content(100000):
                        file.write(chunk)
                    file.close()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


# multi threading
downloadThreads = []
for i in range(0, 1400, 100):  # loop 14 times create 14 thread, each thread download 100 img
    downloadThread = threading.Thread(target=downloader, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# waiting
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done')
