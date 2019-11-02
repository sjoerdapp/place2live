#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 10:33:15 2019

@author: gunjanrawal
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame()
wikiPage = 'https://en.wikipedia.org/?curid=23797951'
website_url = requests.get(wikiPage).text
soup = BeautifulSoup(website_url, 'lxml')

ListTable = soup.find('table', {'class': 'wikitable sortable'})
rows = ListTable.findAll('tr')

countryList = []
active_per_capita = []
total_per_capita = []

for i in rows[1:]:
    dataList = i.findAll('td')
    countryList.append(dataList[1].find('a').contents[0])
    active_per_capita.append(dataList[-1].contents[0])
    total_per_capita.append(dataList[-2].contents[0])

df['Country'] = countryList
df['Per 1000 capita (active)'] = active_per_capita
df['Per 1000 capita (total)'] = total_per_capita

df.to_csv('CountryListOutput.csv', index=False)
