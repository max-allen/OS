from bs4 import BeautifulSoup as Soup
from urllib.request import Request, urlopen

req = Request("https://blog.pragmaticengineer.com/data-structures-and-algorithms-i-actually-used-day-to-day/")
page = urlopen(req).read()
soup = Soup(page, 'html.parser')
text = soup.get_text()

with open('output.md', 'w') as f:
    f.write(text)