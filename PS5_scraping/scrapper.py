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

scrapper_functions = {
    "AMAZON": amazon_scrapper,
    "CURRYS": None,
    "AO": None,
    "VERY": None,
    "ARGOS": None,
    "STUDIO": None,
    "SMYTHS": None,
    "HUGHES": None,
    "JOHN_LEWIS": None
}

async def getAvailability(source, response):
    return await scrapper_functions[source](response)

