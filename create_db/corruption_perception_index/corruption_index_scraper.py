from csv import writer

import requests


def get_data():
    """Get the listed countries and their information"""

    countries = requests.get(
        "https://www.transparency.org/assets/data/cpi2018/table-data.json?",
    ).json()["data"]

    with open("corruption_index.csv", "w") as csv_file:
        csv_writer = writer(csv_file)

        # Preparing the csv file header
        csv_writer.writerow(["country", "region", "rank/180", "score/100"])

        # Writing information for each country
        for country in countries:
            csv_writer.writerow([country[1], country[2], country[0], country[3]])


if __name__ == "__main__":
    get_data()
