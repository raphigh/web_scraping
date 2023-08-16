from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html,"html.parser")

price_tags = bs.find_all(lambda tag : re.search(r"\$\d*",tag.get_text()))

for tag in price_tags:
    price = re.search(r"\$.+",tag.get_text()).group()
    print(price)


