"""

@author: PaulEvans8669
"""
import re

import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_countries_by_English-speaking_population"
data = pd.read_html(url, ".+")[0]

# edit column names
data.columns = data.columns.droplevel(0)
data.columns = [
    "country",
    "1",
    "2",
    "total_english_speakers(%)",
    "4",
    "5",
    "6",
    "7",
    "8",
]
for i in range(8, 3, -1):
    del data[data.columns[i]]
del data[data.columns[2]]
del data[data.columns[1]]
print(data.columns)

data.columns = [
    "country",
    "total_english_speakers",
]

# delete last row ("total")
data = data[:-1]

# save to csv
data.to_csv("EnglishSpeakingPopulation.csv", index=False)

# remove unwanted chars
with open('EnglishSpeakingPopulation.csv', 'r') as f:
    content = f.read()
    content_new = re.sub(r'\[.*?\]', '', content)
    content_new = re.sub("\"", '', content_new)
    f.close()

# rewrite to file
with open('EnglishSpeakingPopulation.csv', 'w') as f:
    f.write(content_new)
    f.close()
