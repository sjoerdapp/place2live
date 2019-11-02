#!/usr/bin/env python
# coding: utf-8
# Written by @yusrilia on GitHub
import csv
from typing import List

import requests
from bs4 import BeautifulSoup

url = requests.get(
    "https://en.wikipedia.org/wiki/List_of_countries_by_traffic-related_death_rate",
).text
soup = BeautifulSoup(url, features="html5lib")
data = soup.find("table", "wikitable sortable")
table = data.find_all("td")

with open("traffic_related_death_rate.csv", "w") as write:
    tmp: List[int] = []
    writer = csv.writer(write)
    writer.writerow(
        [
            "Location",
            "Road fatalities per 100000 inhabitants per year",
            "Road fatalities per 100000 motor vehicles",
            "Road fatalities per 1 billion vehicle-km",
            "Total fatalities latest year",
            "Year",
        ],
    )
    index = 0
    for item in table:
        text = item.text
        result = (text[: text.index("[")]) if "[" in text else text.strip("\n").strip()
        if index % 6 == 4:
            result = int(result.replace(",", ""))
        tmp += [result]
        if index % 6 == 5:
            writer.writerow(tmp)
            tmp = []
        index += 1
