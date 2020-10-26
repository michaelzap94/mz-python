"""
Let's scrape data into a CSV!
Goal: Grab all links from Rithm School blog
Data: store URL, anchor tag text, and date
"""
import requests
from bs4 import BeautifulSoup
from csv import writer
import os

current_dir = os.path.dirname(__file__)
FILENAME = os.path.join(current_dir, 'blog_data.csv')

URL = "https://www.rithmschool.com/blog"
response = requests.get(URL)
htmlDATA = response.text
soup = BeautifulSoup(htmlDATA, "html.parser")
# body = soup.body # optional

dataArr = [] # this is for readibility, you could skip storing the data and write to CSV directly, by moving the loop inside the writer

articles = soup.find_all("article")
for article in articles:
    tempDict = {}
    a_tag = article.find("a") # so we don't call it multiple times as it is time consuming
    tempDict['url'] = a_tag.attrs["href"]
    tempDict['text'] = a_tag.get_text()
    tempDict['date'] = article.find("time").attrs["datetime"]
    dataArr.append(tempDict)

# print(dataArr)

with open(FILENAME, "w", newline='') as csv_file:
    csv_writer = writer(csv_file) # gives the csv_writer with this file
    csv_writer.writerow(["title","link","date"]) # row header
    for data in dataArr:
        csv_writer.writerow([data['text'], data['url'], data['date']])