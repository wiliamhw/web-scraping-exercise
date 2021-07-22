# Web Scraping

## 1.Open URL
Filename: `mapIt.py`  
Description: 
> Launches a map in the browser using an address from the command line or clipboard.  
> Shebang only works on Linux.

Rquirement: `pip install --user pyperclip`  
Input example: `python mapIt.py 870 Valencia St, San Francisco, CA 94110`


## 2. Download Text From Website
Filename: `req.py`  
Description:  
> Download a web page

Rquirement: `pip install --user requests`


## 3. Parse HTML
Filename: `parse_html.py`  
Description:
> Get some HTML elements from 
> local HTML file or online website.  
> Change `opCode` variable to run other sections

Requirements:
```
pip install --user requests
pip install --user beautifulsoup4
```


## 4. Opening Search Results
Filename: `searchpypi.py`  
Description:
> Opens several search results.

Input example: `python searchpypi.py faker`  
Requirements:
```
pip install --user requests
pip install --user beautifulsoup4
```
Input example: `python searchpypi.py faker`

## 5. Selenium
Filename: `selenium.py`
Description:
> Use selenium to scrape web
Requirements:
```
pip install --user selenium
<browser name> webdriver that has been put on the system PATH
```
