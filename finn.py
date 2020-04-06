# -*- coding: utf-8 -*-
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def getInfo():
    URL = "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.20016&location=1.20016.20318&page="
    filename = "utleiebolig.csv"
    f = open(filename, "w")
    f.write("SEP=," + "\n")
    f.write("\n")
    headers = "ID, beskrivelse, adresse, link, Kvadratmeter, pris, utleier, type bolig\n"
    f.write(headers)

    for i in range(1, 15):
        printInfo(URL + str(i), f)
    print(i)
    f.close()


def printInfo(URL, f):
    my_url = URL
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # HTML parser
    page_soup = soup(page_html, "html.parser")

    # Fetches all the residences
    containers = page_soup.findAll("div", {"class": "ads__unit__content"})

    container1 = containers[0]
    # Grabs the id, price, m2, link, and adress
    for container in containers:
        ID = container.h2.a["id"]
        description = container.h2.getText()
        address = container.contents[2].getText()
        link = "finn.no" + container.h2.a["href"]

        container2 = container.find("div", "ads__unit__content__keys")

        sqm = container2.contents[0].getText()
        try:
            price = container2.contents[1].getText()
        except IndexError:
            price = "ikke oppgitt"

        container3 = container.find("div", "ads__unit__content__list")
        typeLandlord = container3.getText()
        residenceType = container3.next.next.getText()

        f.write(ID + "," + description.replace(",", " - ") + "," + address.replace(",", " - ") + ", " + link + "," +
                sqm + "," + price + "," + typeLandlord + "," + residenceType + "\n")

        print(ID)
        print(description)
        print(address)
        print(link)
        print(sqm)
        print(price)
        print(typeLandlord)
        print(residenceType)

        print('\n')


getInfo()
