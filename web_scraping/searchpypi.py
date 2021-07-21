#! python
# searchpypi.py - Opens several search results.
# Input example: python searchpypi.py faker

from urllib.parse import urlparse, parse_qs
import requests, sys, webbrowser, bs4

print('Searching...')  # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='
                   + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result.
linkElems = []
for link in soup.find_all('a'):
    url = link.get('href')
    if url.startswith("/url?"):
        url = parse_qs(urlparse(url).query)['q']
        linkElems.append(url[0])
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = linkElems[i]
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)