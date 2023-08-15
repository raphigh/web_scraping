from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):

    try:
        html = urlopen(url)
    except HTTPError as e :
        print(e)
    except URLError as e :
        print(e)

    try:
        bs = BeautifulSoup(html,"html.parser")
        title = bs.body.h1
    except AttributeError:
        return None
    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("tag not found")
else:
    print(title)