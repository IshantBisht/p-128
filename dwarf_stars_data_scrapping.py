from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import requests
import csv
import pandas as pd
url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page=requests.get(url)
soup=bs(page.text,"html.parser")
star_table=soup.find_all("table",{"class":"wikitable sortable"})
total_table=len(star_table)
templist=[]
table_rows=star_table[1].find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]
    templist.append(row)
star_names=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(templist)):
    star_names.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])
headers=["star_names","distance","mass","radius"]
df2=pd.DataFrame(list(zip(star_names,distance,mass,radius,)),columns=["star_names","distance","mass","radius"])
print(df2)
df2.to_csv("dwarf_stars.csv",index=True,index_label="id")
