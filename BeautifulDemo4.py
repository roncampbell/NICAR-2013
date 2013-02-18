# Script for scraping websites

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

# variables and aliases -- finds tables for letters of alphabet
# then finds rows for individual members of congress
# then finds columns for info about those members
for tab in menu:
     tables = tab.find_all("table")
     for table in tables:
        row = table.find_all("tr")
        for tr in row:
            col = tr.find_all("td")
            # test for valid text in columns, then extract columns
            try:
                name = col[0].a.string
                district = col[1].string
                party = col[2].string
                room = col[3].string
                phone = col[4].string
                str = "\t"
                congo = (name, district, party, room, phone)
                print str.join(congo)
            except:
                # print 'error: there wasn't text in all the columns presumably'
                pass
