import requests
import csv
from bs4 import BeautifulSoup

URL = "https://www.uttamis.co.tz/net-asset-value?date2=&page="

outfile = open("table_data.csv","w",newline='')
writer = csv.writer(outfile)
tab_data = []

for x in range(2667):

    page = requests.get(URL + str(x+1))
    tree = BeautifulSoup(page.content,"html.parser")
    table_tag = tree.select("table")[0]
    if x == 0:
        tab_data = [[item.text for item in row_data.select("th,td")]
                        for row_data in table_tag.select("tr")]
    else:
        tab_data += [[item.text for item in row_data.select("td")]
                        for row_data in table_tag.select("tr")]
   

for data in tab_data:
    writer.writerow(data)
    print(' '.join(data))