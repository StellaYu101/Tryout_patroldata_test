##LIBRARY SETUP
import urllib2, requests, csv
from bs4 import BeautifulSoup

##CSV OUTPUT SETUP
outfile = open('patroltest.csv','w')
writer = csv.writer(outfile)

##GRAB DATA
url = "https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=04/07/2019"
html = urllib2.urlopen(url).read()

##PROCESS HTML
soup = BeautifulSoup(html, 'html.parser')

##SCRAPE DATA
table = soup.find('table',{'class':'accidentOutput'})
rows = table.find_all('tr')
for row in rows:
	cells = row.find_all('td')
	data = []##CREATE EMPTY LIST

	for cell in cells:
		data.append(cell.text.encode('utf-8'))##CONVERTING FORMAT

	writer.writerow(data)##WRITE DATA INTO THE LIST WE CREATED UP THERE
