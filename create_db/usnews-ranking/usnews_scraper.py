import json
import re
from csv import writer

import requests
from bs4 import BeautifulSoup


def get_data():
    agent = "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    headers = {"User-Agent": agent}  # Defining a user agent is necessary to the request
    res = requests.get(
        "https://www.usnews.com/news/best-countries/overall-rankings", headers=headers,
    )

    soup = BeautifulSoup(res.text, "html.parser")
    script = soup.find_all("script")[-1]  # The data is hard coded in a script tag

    pattern = r"window\.__APOLLO_STATE__ =(.*?)window\."
    data = re.search(pattern, script.text, re.DOTALL).group(1)
    data = json.loads(data)

    countries = data["$ROOT_QUERY.context"]["rankings"]["json"]
    return countries


def write_to_csv():
    """Write the data into a csv file in the current directory"""

    countries = get_data()
    with open("usnews_ranking.csv", "w") as csv_file:
        csv_writer = writer(csv_file)

        # Preparing the csv file header
        csv_writer.writerow(
            [
                "rank",
                "name",
                "gdp",
                "population",
                "capital",
                "gdp_per_capita",
                "geographic_region_name",
            ],
        )

        # Writing information for each country
        for country in countries:
            country = country["country_summary"]
            if country["overall_rank"]:
                csv_writer.writerow(
                    [
                        country["overall_rank"],
                        country["name"],
                        country["gdp"],
                        country["population"],
                        country["capital"],
                        country["gdp_per_capita"],
                        country["geographic_region_name"],
                    ],
                )


if __name__ == "__main__":
    write_to_csv()
