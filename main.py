import urllib
import requests
from bs4 import BeautifulSoup





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    u2 = urllib.request.urlopen('https://www.merriam-webster.com/dictionary/run')
    soup = BeautifulSoup(u2, 'html.parser')
    r = requests.get('https://random-word-api.herokuapp.com/word?number=10')
    print(r.text)
    #print(soup.prettify())container
    mydivs = soup.findAll("a", {"class": "important-blue-link"})
    m2ydivs = soup.findAll("div", {"class": "container"})
    print(mydivs)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
