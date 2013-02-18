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

# a variable (called menu) grabs congressmen listed by last name
menu = soup.find_all("div", {"id":"byName"})

print menu
