import urllib2, requests, csv
from bs4 import BeautifulSoup
outfile = open('patroltest.csv','w')
writer = csv.writer(outfile)
url = "https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=04/07/2019"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('table',{'class':'accidentOutput'})
rows = table.find_all('tr')
for row in rows:
	cells = row.find_all('td')
	data = []

	for cell in cells:
		data.append(cell.text.encode('utf-8'))

	writer.writerow(data)
