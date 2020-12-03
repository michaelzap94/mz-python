"""
This script will scrape UK retailers to find when the PS5 is available
"""
from bs4 import BeautifulSoup
from constants import RETAILERS

async def amazon_scrapper(response):
    htmlDATA = await response.content.read()
    soup = BeautifulSoup(htmlDATA, "html.parser")
    availabilityDiv = soup.find(id="availability")
    outter = availabilityDiv.find("span")
    text = outter.get_text().strip()
    return False if ("unavailable" in text) else True

async def studio_scrapper(response):
    htmlDATA = await response.content.read()
    soup = BeautifulSoup(htmlDATA, "html.parser")
    availabilityDiv = soup.find(class_="egl_now product-details__price-now")
    outter = availabilityDiv.find("span")
    text = outter.get_text().strip()
    return False if ("unavailable" in text.lower()) else True

scrapper_functions = {
    "AMAZON": amazon_scrapper,
    "CURRYS": None,
    "AO": None,
    "VERY": None,
    "ARGOS": None,
    "STUDIO": studio_scrapper,
    "SMYTHS": None,
    "HUGHES": None,
    "JOHN_LEWIS": None
}

async def getAvailability(source, response):
    print(f"scrapping: {source}")
    return await scrapper_functions[source](response)

