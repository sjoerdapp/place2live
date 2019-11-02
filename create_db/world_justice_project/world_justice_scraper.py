import json
from csv import writer
from datetime import datetime

import requests


def get_current_year():
    """Get the current year"""
    return datetime.now().year


def get_data():
    """Get the listed countries and their information"""

    year = get_current_year() - 1
    url = f"http://data.worldjusticeproject.org/data/data-roli-{year}.js"
    res = requests.get(url)

    countries = res.text[len("var data = "):]
    countries = json.loads(countries)

    with open("world_justice.csv", "w") as csv_file:
        csv_writer = writer(csv_file)

        # Preparing the csv file header
        csv_writer.writerow(
            [
                "country",
                "region",
                "overall_score",
                "overall_rank",
                "income_rank",
                "region_rank",
            ],
        )

        # Writing information for each count
        for country in countries:
            if country["score"]:
                csv_writer.writerow(
                    [
                        country["country"],
                        country["region"],
                        country["score"],
                        country["global_rank"],
                        country["income_rank"],
                        country["regional_rank"],
                    ],
                )


if __name__ == "__main__":
    get_data()
