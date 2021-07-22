# Open Tower of God manga

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
type(browser)
    # <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
comic_name = 'Tower of God'
browser.get('https://m.manganelo.com/w')
try:
    searchBarElem = browser.find_element_by_id('search-story')
    # print('Found <%s> element with that class name!' % (linkElem.tag_name))
    searchBarElem.send_keys(comic_name)
    searchBarElem.send_keys(Keys.ENTER)
    print("Current page title: " + browser.title)

    browser.implicitly_wait(5)
    linkElem = browser.find_element_by_xpath("//a[@title='" + comic_name + "']")
    linkElem.click()
    print("Current page title: " + browser.title)
    
    print('Tab will close in 5 seconds.')
    browser.implicitly_wait(5)
    browser.quit()
except:
    print('Was not able to find an element with that name.')