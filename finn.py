import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.20016&location=1.20016.20318"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parser
page_soup = soup(page_html, "html.parser")

# Fetches all the residences
containers = page_soup.findAll("div", {"class": "ads__unit__content"})


# Grabs the id, price, m2, link, and adress
for container in containers:
    print(container.h2.getText())
    print(container.h2.a["id"])
    print(container.h2.a["href"])

print("\n")
print(containers[0].find("div", "ads__unit__content__details"))

container2 = containers[0].find("div", "ads__unit__content__keys")
print(container2[0])
