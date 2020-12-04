"""
This script will scrape UK retailers to find when the PS5 is available
"""
import json
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

async def hughes_scrapper(soup):
    availabilityDiv = soup.find(class_="filter--count")
    number = availabilityDiv.get_text().strip().lower()
    return False if (int(number) <= 5) else True

async def very_scrapper(soup):
    availabilityDiv = soup.find(class_="productsPerPage")
    text = availabilityDiv.get_text().strip().lower()
    number = text.split("of ")[1].split(")")[0]
    return False if (int(number) <= 24) else True

async def currys_scrapper(soup):
    availabilityDiv = soup.find(attrs={"data-component":"list-page-results-message"})
    outter = availabilityDiv.find("strong")
    text = outter.get_text().strip().lower()
    number = text.split("of ")[1].split(" ")[0]
    return False if (int(number) <= 2) else True

async def shopTo_scrapper(soup):
    availabilityDiv = soup.find(class_="orderbox_inventory")
    outter = availabilityDiv.find("p")
    text = outter.get_text().strip().lower()
    return False if ("out" in text) else True

async def ao_scrapper(soup):
    availabilityDiv = soup.find(id="lister-data")
    availabilityDiv = str(availabilityDiv)
    json_raw = availabilityDiv.split(">", 1)[1].split("</script>")[0].strip()
    json_dict = json.loads(json_raw)
    return False if (len(json_dict["Products"]) <= 2) else True

async def argos_scrapper(soup):
    availabilityDiv = soup.find(id="h1title")
    text = availabilityDiv.get_text().strip().lower()
    return False if ("unavailable" in text) else True

scrapper_functions = {
    "AMAZON": amazon_scrapper,
    "CURRYS": currys_scrapper,
    "AO": ao_scrapper,
    "VERY": very_scrapper,
    "ARGOS": argos_scrapper,
    "STUDIO": studio_scrapper,
    "SMYTHS": smyths_scrapper,
    "HUGHES": hughes_scrapper,
    "SHOP_TO": shopTo_scrapper
}

async def getAvailability(source, html_response):
    html = await html_response.content.read()
    # if(source == "ARGOS"):
    #     print(html)
    soup = BeautifulSoup(html, "html.parser")
    return await scrapper_functions[source](soup)
    

