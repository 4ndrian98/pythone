import urllib.request
address = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(address)
theBytes = response.read()
#print(response)
#print(dir(response))
#print (theBytes)
html = theBytes.decode(encoding='iso-8859-1')
from bs4 import BeautifulSoup
doc = BeautifulSoup(html,"html.parser")
#print(doc.prettify())
t1 = doc.table
t2=t1.find_next("table")
t3=t2.find_next("table")
t4 =t3.find_next("table")
#print(t4)
riga = t4.find_next("tr")

import pandas
province = pandas.DataFrame (columns=["sigla","nome", "abitanti"])

riga = riga.find_next("tr")
i=0
while riga != None:
    tdx = riga.find_next("td")
    tdx = tdx.find_next("td")
    provincia = tdx.get_text()
    tdx = tdx.find_next("td")
    abitanti = int(tdx.get_text().replace(".", ""))
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    tdx = tdx.find_next("td")
    sigla = tdx.get_text()
    province.loc[i]=[sigla,provincia, abitanti]
    if sigla == "VT" : break
    i += 1
    riga = riga.find_next("tr")


province_sorted = province.sort_values(by="abitanti", ascending=False)
print(province_sorted)

import pickle
dbfile = open('province','wb')
pickle.dump(province_sorted,dbfile)
dbfile.close()
