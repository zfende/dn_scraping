from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "http://quotes.yourdictionary.com/theme/marriage/"
html = urlopen(url).read()
porocni_citati = BeautifulSoup(html)

citati = porocni_citati.findAll("p", attrs={"class": "quoteContent"})

izbor = 1

for citat in citati:
    if izbor <= 5:
        print citat.text
        print ("-------------")
    izbor = izbor + 1