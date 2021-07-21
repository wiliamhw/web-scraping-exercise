# pip install --user beautifulsoup4

import requests, bs4
opCode = 3
if (opCode == 0):
    # Parse text attribute from https://nostarch.com and store it in `noStarchSoup`
    res = requests.get('https://nostarch.com')
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(type(noStarchSoup))
elif (opCode == 1):
    # Parse text attribute from example.html and store it in `exampleSoup`
    exampleFile = open('example.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
    elems = exampleSoup.select('#author')
    type(elems) # elems is a list of Tag objects.
        # <class 'list'>
    len(elems)
        # 1
    type(elems[0])
        # <class 'bs4.element.Tag'>
    str(elems[0]) # The Tag object as a string.
        # '<span id="author">Al Sweigart</span>'
    elems[0].getText()
        # 'Al Sweigart'
    elems[0].attrs
        # {'id': 'author'}
elif (opCode == 2):
    # Parse paragraph attribute from example.html and store it in `exampleSoup`
    exampleFile = open('example.html')
    exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
    pElems = exampleSoup.select('p')
    str(pElems[0])
        # '<p>Download my <strong>Python</strong> book from <a href="https://
        # inventwithpython.com">my website</a>.</p>'
    pElems[0].getText()
        # 'Download my Python book from my website.'
    str(pElems[1])
        # '<p class="slogan">Learn Python the easy way!</p>'
    pElems[1].getText()
        # 'Learn Python the easy way!'
    str(pElems[2])
        # '<p>By <span id="author">Al Sweigart</span></p>'
    pElems[2].getText()
        # 'By Al Sweigart'
elif (opCode == 3):
    # Get data from element attributes
    soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
    spanElem = soup.select('span')[0]
    str(spanElem)
        # '<span id="author">Al Sweigart</span>'
    spanElem.get('id')
        # 'author'
    spanElem.get('some_nonexistent_addr') == None
        # True
    spanElem.attrs
        # {'id': 'author'}