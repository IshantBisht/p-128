from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome()
browser.get(START_URL)
time.sleep(10)
scrapped_data=[]
def scrape():
        soup = BeautifulSoup(browser.page_source, "html.parser")
        bright_star_table=soup.find("table",attrs={"class","wikitable"})
        table_body=bright_star_table.find("tbody")
        table_rows=table_body.find_all("td")
        for row in table_rows:
            table_calls=row.find_all("td")
            templist=[]
            for call_data in table_calls:
                data=call_data.text.strip()
                templist.append(data)
            scrapped_data.append(templist)
            
scrape()
stars_data=[]
for i in range(0,len(scrapped_data)):
    star_names=scrapped_data[i][1]
    distance=scrapped_data[i][3]  
    mass=scrapped_data[i][5]
    radius=scrapped_data[i][6]
    lum=scrapped_data[i][7]
    required_data=[star_names,distance,mass,radius,lum]
    stars_data.append(required_data)
print(stars_data)
headers=["star_names","distance","mass","radius","luminosity"]
star_df_1=pd.DataFrame(stars_data,columns=headers)
star_df_1.to_csv("scrapped_data.csv",index=True,index_label="ID")