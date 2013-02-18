# Script for scraping website

# import Python module to deal with websites
import urllib2

# import BeautifulSoup to scrape websites
from bs4 import BeautifulSoup

# these next lines read the website into BeautifulSoup
url = "http://www.house.gov/representatives"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)
page.close()

# the "prettify" command in BeautifulSoup lets us see the website structure
print(soup.prettify())
