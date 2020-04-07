# -*- coding: utf-8 -*-
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import unicodecsv as csv
import math


def getURL(by):

    if(by == "STAVANGER"):
        return "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.20012&location=1.20012.20196"

    elif(by == "BERGEN"):
        return "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.22046&location=1.22046.20220"
    elif (by == "TRONDHEIM"):
        return "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.20016&location=1.20016.20318"
    elif(by == "OSLO"):
        return "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.20061"
    elif(by == "TROMSØ"):
        return "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.22054&location=1.22054.20413"
    else:
        print("ikke gyldig")
        return False


def getPages(URL):
    uClient = uReq(URL)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    container = page_soup.findAll("span", {"class": "u-strong"})
    pages = container[0].contents[0].replace(u'\xa0', "")
    return math.ceil(int(pages)/51)


def getInfo(by):

    URL = getURL(by)
    filename = "../Data/utleiebolig" + by + ".csv"
    f = open(filename, "w", encoding='utf-8')
    f.write("SEP=;" + "\n")
    f.write("\n")
    headers = "ID; beskrivelse; adresse; Kvadratmeter; pris; utleier; type bolig ; link\n"
    f.write(headers)
    pages = getPages(URL)
    for i in range(1, pages+1):
        printInfo(URL + "&page=" + str(i), f)
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
            price = sqm
            sqm = "ikke oppgitt"

        container3 = container.find("div", "ads__unit__content__list")
        typeLandlord = container3.getText()
        residenceType = container3.next.next.getText()

        f.write(ID + ";" + description + ";" + address + "; " +
                sqm + ";" + price + ";" + typeLandlord + ";" + residenceType + link + ";" + "\n")

        print(ID)
        print(description)
        print(address)
        print(link)
        print(sqm)
        print(price)
        print(typeLandlord)
        print(residenceType)


print('\n')


getInfo("STAVANGER")
getInfo("BERGEN")
getInfo("OSLO")
getInfo("TRONDHEIM")
getInfo("TROMSØ")
