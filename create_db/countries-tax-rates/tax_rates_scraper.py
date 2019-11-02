import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame()
wiki_page = "https://en.wikipedia.org/wiki/List_of_countries_by_tax_rates"
website_url = requests.get(wiki_page).text
soup = BeautifulSoup(website_url, "html.parser")

list_table = soup.find("table", {"class": "wikitable sortable"})
rows = list_table.findAll("tr")

countries = []
corporate_taxes = []
income_taxes_lowest = []
income_taxes_highest = []
sales_taxes = []

for row in rows[1:]:
    data_list = row.findAll("td")
    countries.append(data_list[0].find("a").text)
    corporate_taxes.append(data_list[1].contents[0].strip())
    income_taxes_lowest.append(data_list[2].contents[0].strip())
    income_taxes_highest.append(data_list[3].contents[0].strip())
    sales_taxes.append(data_list[4].contents[0].strip())


df["country"] = countries
df["corporate_tax"] = corporate_taxes
df["income_taxes_lowest_marginal_rate"] = income_taxes_lowest
df["income_taxes_heighest_marginal_rate"] = income_taxes_highest
df["sales_tax"] = sales_taxes


df.to_csv("tax_rates.csv", index=False)
