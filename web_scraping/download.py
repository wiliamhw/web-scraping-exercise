# pip install --user requests
# Download a web page

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    res.raise_for_status()

    # Inspect web element
    print(type(res))
    print(res.status_code == requests.codes.ok)
    print(len(res.text))
    print(res.text[:250])

    # Save downloaded file in hard drive
    playFile = open('RomeoAndJuliet.txt', 'wb') # wb = write in binary
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('There was a problem: %s' % (exc))