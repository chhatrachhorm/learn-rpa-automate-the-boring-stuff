import requests

try:
    # to check if error
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    res.raise_for_status()
    if res.status_code == requests.codes.ok:
        print(len(res.text))
        print(res.text[:250])
        # to save to storage, pass 'wb' -write binary
        # to standard open()
        # use chuck if the file is large
        myFile = open('files/RomeoJuliet.txt', 'wb')
        for chunk in res.iter_content(100000):
            myFile.write(chunk)
        myFile.close()
except Exception as exc:
    print('There was a problem: %s' % exc)


