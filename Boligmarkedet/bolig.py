# -*- coding: utf-8 -*-
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import math


def getURL(by):
    if(by == "STAVANGER"):
        return "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20012&location=1.20012.20196"

    elif(by == "BERGEN"):
        return "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22046&location=1.22046.20220"
    elif (by == "TRONDHEIM"):
        return "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20016&location=1.20016.20318"
    elif(by == "OSLO"):
        return "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20061"
    elif(by == "TROMSØ"):
        return "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22054&location=1.22054.20413"
    else:
        print("ikke gyldig")
        return False


def getPPSqm(price, sqm):

    if("not found" in price or "not found" in sqm):
        return "None"

    elif("-" in price and "-" in sqm):
        price = price.split("-")
        sqm = sqm.split("-")
        priceLow = price[0].split(" ")
        priceHigh = price[1].split(" ")
        sqmLow = sqm[0].split(" ")
        sqmHigh = sqm[1].split(" ")
        return str(round(float(priceLow[0])/float(sqmLow[0]))) + " - " + str(round(float(priceHigh[1])/float(sqmHigh[1])))

    elif("Solgt" in price):
        return "solgt - uvisst"

    else:
        price = price.split(" ")
        sqm = sqm.split(" ")
        return round(float(price[0])/float(sqm[0]))


def getPages(URL):
    uClient = uReq(URL)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    container = page_soup.findAll("span", {"class": "u-strong"})
    pages = container[0].contents[0].replace(u'\xa0', "")
    return math.ceil(int(pages)/51)


def getDataFromOnePage(URL, f):
    uClient = uReq(URL)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div", {"class": "ads__unit__content"})
    for container in containers:
        description = container.a.contents[0]
        id = container.a["id"]

        address = container.find(
            "div", {"class", "ads__unit__content__details"}).getText()
        try:
            sqm = container.find(
                "div", {"class", "ads__unit__content__keys"}).contents[0].text
        except IndexError:
            sqm = "not found"
        try:
            price = container.find(
                "div", {"class", "ads__unit__content__keys"}).contents[1].text.replace(u'\xa0', "")

        except IndexError:
            price = "not found"

        totalprice = container.findAll(
            "div", {"class", "ads__unit__content__list"})[1].text.strip()

        if("•" in totalprice):
            totalprice = totalprice.split("•")
            fellesgjeld = totalprice[1]
            totalprice = totalprice[0]
            if(':' in fellesgjeld):
                temp = fellesgjeld.split(':')
                fellesgjeld = temp[1].replace(':', '')

        else:
            fellesgjeld = '0'

        broker = container.findAll(
            "div", {"class", "ads__unit__content__list"})[0].text.strip()

        ppsqmm = getPPSqm(price, sqm)

        f.write(str(id) + " ; " + description + " ; " + address + " ; " + sqm + " ; " +
                price + "; " + str(ppsqmm) + " ; " + totalprice + ";" + str(fellesgjeld) + " ; "+broker + "\n")


def exportData(by):
    filename = "../Data/Boligdata" + by + ".csv"
    f = open(filename, "w")
    headers = "ID; Beskrivelse; adresse; kvadratmeter; pris;pris per kvadratmeter ; totalpris ; fellesutgifter; megler \n"
    f.write(headers)
    URL = getURL(by)
    for i in range(1, getPages(URL)):
        getDataFromOnePage(URL + "&page="+str(i), f)
    f.close()


exportData("STAVANGER")
exportData("OSLO")
exportData("BERGEN")
exportData("TRONDHEIM")
exportData("TROMSØ")
