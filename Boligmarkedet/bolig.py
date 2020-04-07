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
                "div", {"class", "ads__unit__content__keys"}).contents[1].text
        except IndexError:
            price = "not found"

        totalprice = container.findAll(
            "div", {"class", "ads__unit__content__list"})[1].text.strip()
        broker = container.findAll(
            "div", {"class", "ads__unit__content__list"})[0].text.strip()

        f.write(str(id) + " , " + description + " , " + address + " , " + sqm + " , " +
                price + " , " + totalprice + " , "+broker + "\n")


def exportData(by):
    filename = "Boligdata" + by + ".csv"
    f = open(filename, "w")
    headers = "ID, Beskrivelse, adresse, kvadratmeter, pris, totalpris + fellesgjeld, megler \n"
    f.write(headers)
    URL = getURL(by)
    for i in range(1, getPages(URL)):
        getDataFromOnePage(URL + "&page="+str(i), f)

    f.close()


exportData("STAVANGER")
exportData("BERGEN")
exportData("TRONDHEIM")
exportData("OSLO")
exportData("TROMSØ")
