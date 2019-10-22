import re
import requests
from bs4 import BeautifulSoup
import csv


def get_row(country_link):
    """

    :param country_link: The link of country to get th score from
    :return: list containing the country name and score for a csv row
    """
    country_name = country_link.split('/')[-1]
    try:
        print(country_link)
        base_url = "https://freedomhouse.org{}"
        res = requests.get(base_url.format(country_link))
        soup_text = BeautifulSoup(res.text, "lxml").text
        regex = r"Aggregate Score:(.{0,9})"
        reg = re.compile(regex)
        sc_dirty = reg.search(soup_text).group(1)
        score = [s for s in sc_dirty.split()[0] if s.isdigit()]
        score = "".join(score)
        score = float(score)
    except AttributeError:
        score = None
    return [country_name, score]


def get_countries():
    """

    :return: list of country links
    """
    site_url = "https://freedomhouse.org/report/freedom-world/freedom-world-2018"
    html_text = requests.get(site_url).text
    soup_object = BeautifulSoup(html_text, 'html.parser')

    # the first option not relevant
    country_options = soup_object.find(id="table-ul-left-side").find("select").find_all('option')[1:]
    country_links = [country_option.get('value') for country_option in country_options]
    return country_links


def write_csv(rows):
    """
    creates csv file with the given rows
    :param rows:  the rows to write
    """
    with open('scores.csv', 'w') as file_handler:
        writer = csv.writer(file_handler)
        writer.writerow(["name", "score"])
        for row in rows:
            writer.writerow(row)


def main():
    countries = get_countries()
    rows = [get_row(country) for country in countries]
    write_csv(rows)


if __name__ == '__main__':
    main()
