from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

url = "https://scrapebook22.appspot.com/"
html = urlopen(url).read()

seznam = open("seznam.csv", "w")

prva_stran = BeautifulSoup(html)
print (prva_stran.html.head.title.string)

for povezava in prva_stran.findAll("a"):
    if povezava.string == "See full profile":
        url_profila = url + povezava["href"]
        html_profila = urlopen(url_profila).read()
        profil = BeautifulSoup(html_profila)
        ime = profil.find("div", attrs={"class": "row"}).h1.string
        email_span = profil.find("span", attrs={"class": "email"}).string
        mesto = profil.find("span", attrs={"data-city": True}).string

        podatki = ime.string + "," + email_span.string + "," + mesto.string
        #print podatki
        seznam.write(podatki + "\n")

seznam.close()
