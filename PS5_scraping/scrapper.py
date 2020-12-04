"""
This script will scrape UK retailers to find when the PS5 is available
"""
from bs4 import BeautifulSoup
from constants import RETAILERS

async def amazon_scrapper(soup):
    availabilityDiv = soup.find(id="availability")
    outter = availabilityDiv.find("span")
    text = outter.get_text().strip().lower()
    return False if ("unavailable" in text) else True

async def studio_scrapper(soup):
    availabilityDiv = soup.find(class_="egl_now product-details__price-now")
    outter = availabilityDiv.find("span")
    text = outter.get_text().strip().lower()
    return False if ("unavailable" in text) else True

async def smyths_scrapper(soup):
    availabilityDiv = soup.find(class_="deliveryType homeDelivery js-stockStatus")
    text = availabilityDiv.get_text().strip().lower()
    return False if ("out" in text) else True

scrapper_functions = {
    "AMAZON": amazon_scrapper,
    "CURRYS": None,
    "AO": None,
    "VERY": None,
    "ARGOS": None,
    "STUDIO": studio_scrapper,
    "SMYTHS": smyths_scrapper,
    "HUGHES": None,
    "JOHN_LEWIS": None
}

async def getAvailability(source, html_response):
    print(f"scrapping: {source}")
    soup = BeautifulSoup(await html_response.content.read(), "html.parser")
    return await scrapper_functions[source](soup)
    

