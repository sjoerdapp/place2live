import pandas as pd
import difflib
from utils import text_color
from utils import text_type

df = pd.read_csv("city/output/list_of_countries.csv")


def get_closest_country(country_name: str):
    """ This function fins the closest match for the country"""
    countries = df['country'].values.tolist()
    results = difflib.get_close_matches(country_name, countries)
    return results


def run_country_checker():
    """Checks for a valid country by checking df"""
    while True:
        try:
            country = input(
                text_color(
                    "What is your country? ", text_type.QUESTION,
                ),
            )
            country = country.lower()
            country = country.title()
            float(df[df.country == country]["purchasing_power_index"])
        except TypeError:
            res = get_closest_country(country)
            print(
                    text_color(
                        f"'{country}' is an invalid country or did you mean {res}"
                        f". Please try again.",
                        text_type.WARNING,
                    ),
            )
        else:
            return country


YOUR_COUNTRY = run_country_checker()


def max_min_index(name_index):
    """Return maximum and minimum value with country of a column from df."""
    country_and_name = df[['country', name_index]]
    counrties_in_name_index = country_and_name.sort_values(name_index).dropna()
    min_value = [
        list(counrties_in_name_index[name_index])[0],
        list(counrties_in_name_index['country'])[0],
    ]
    max_value = [
        list(counrties_in_name_index[name_index])[-1],
        list(counrties_in_name_index['country'])[-1],
    ]
    return max_value, min_value


def print_question(name_index, max_min_value, mood):
    """
    Return a question that asks the user about the status of a factor
    in his country, also displays the maximum and minimum value of this factor
    in the world.
    """
    if mood == 'higher is better':
        first_value = max_min_value[0]
        second_value = max_min_value[1]
    elif mood == 'lower is better':
        first_value = max_min_value[1]
        second_value = max_min_value[0]
    message = text_color(
        f"What is your desirable {name_index} ({mood})? "
        f"The best score in the world is "
        f"{first_value[0]} "
        f"({first_value[1]}), "
        f"the worst is {second_value[0]} "
        f"({second_value[1]}) ", text_type.QUESTION,
    )
    return message


def _value_checker(index_input):
    """Helper function to input check the main index functions"""
    if index_input == '':  # empty string, default index
        return "default"
    try:
        return float(index_input)
    except ValueError:
        return False


def purchase_power_func():
    """finds your purchase power index"""
    country_purchasing_power_index = float(
        df[df.country == YOUR_COUNTRY]["purchasing_power_index"],
    )
    print(
        text_color(
            f"In your country purchasing power "
            f"index is {country_purchasing_power_index}", text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question(
                    'purchasing power index', max_min_purchasing,
                    'higher is better',
                ),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_purchasing_power_index
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
                text_type.WARNING,
            ),
        )


def safety_func():
    """finds your safety index"""
    country_safety_index = float(
        df[df.country == YOUR_COUNTRY]["safety_index"],
    )
    print(
        text_color(
            f"In your country safety index is {country_safety_index} or "
            f" crime Index is {round((100.0-country_safety_index), 2)}",
            text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question('safety index', max_min_safety, 'higher is better'),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_safety_index
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
                text_type.WARNING,
            ),
        )


def health_care_func():
    """finds your health care index"""
    country_health_care_index = float(
        df[df.country == YOUR_COUNTRY]["health_care_index"],
    )
    print(
        text_color(
            f"In your country health care index is {country_health_care_index}",
            text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question(
                    'health care index', max_min_health,
                    mood='higher is better',
                ),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_health_care_index
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
            ),
            text_type.WARNING,
        )


def climate_func():
    """finds your climate index"""
    country_climate_index = float(
        df[df.country == YOUR_COUNTRY]["climate_index"],
    )
    print(
        text_color(
            f"In your country climate index is {country_climate_index}",
            text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question(
                    'climate index', max_min_climate,
                    'higher is better',
                ),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_climate_index
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
                text_type.WARNING,
            ),
        )


def cost_of_living_func():
    """finds your cost of living index"""
    country_cost_of_living_index = float(
        df[df.country == YOUR_COUNTRY]["cost_of_living_index"],
    )
    print(
        text_color(
            f"In your country cost of living "
            f"index is {country_cost_of_living_index}",
            text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question(
                    'cost of living index', max_min_cost,
                    'lower is better',
                ),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_cost_of_living_index
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
                text_type.WARNING,
            ),
        )


def property_price_to_income_ratio_func():
    """finds your property price to income ratio index"""
    country_property_price_to_income_ratio = float(
        df[df.country == YOUR_COUNTRY]["property_price_to_income_ratio"],
    )
    print(
        text_color(
            f"In your country house price to "
            f"income ratio index is {country_property_price_to_income_ratio}",
            text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question(
                    'property price to income ratio', max_min_property,
                    'lower is better',
                ),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_property_price_to_income_ratio
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
                text_type.WARNING,
            ),
        )


def traffic_commute_time_func():
    """finds your traffic commute time index"""
    country_traffic_commute_time_index = float(
        df[df.country == YOUR_COUNTRY]["traffic_commute_time_index"],
    )
    print(
        text_color(
            f"In your country traffic commute time "
            f"index is {country_traffic_commute_time_index}", text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question(
                    'traffic commute time index', max_min_traffic,
                    'lower is better',
                ),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_traffic_commute_time_index
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
                text_type.WARNING,
            ),
        )


def pollution_func():
    """finds your pollution index"""
    country_pollution_index = float(
        df[df.country == YOUR_COUNTRY]["pollution_index"],
    )
    print(
        text_color(
            f"In your country pollution index is {country_pollution_index}",
            text_type.ANSWER,
        ),
    )

    while True:
        index_input = (
            input(
                print_question(
                    'pollution index', max_min_pollution,
                    'lower is better',
                ),
            )
        )
        if isinstance(_value_checker(index_input), float):
            return _value_checker(index_input)
        elif _value_checker(index_input) == "default":
            return country_pollution_index
        print(
            text_color(
                f"'{index_input}' is an invalid index. Please try again.",
                text_type.WARNING,
            ),
        )


values = {
    "purchasing_power_index": 200,
    "safety_index": 200,
    "health_care_index": 200,
    "cost_of_living_index": 0,
    "property_price_to_income_ratio": 0,
    "traffic_commute_time_index": 0,
    "pollution_index": 0,
    "climate_index": 200,
}
df = df.fillna(value=values)

if __name__ == "__main__":

    max_min_purchasing = max_min_index('purchasing_power_index')
    max_min_safety = max_min_index('safety_index')
    max_min_health = max_min_index('health_care_index')
    max_min_cost = max_min_index('cost_of_living_index')
    max_min_property = max_min_index('property_price_to_income_ratio')
    max_min_traffic = max_min_index('traffic_commute_time_index')
    max_min_pollution = max_min_index('pollution_index')
    max_min_climate = max_min_index('climate_index')
    your_purchasing_power_index = float(purchase_power_func())
    your_safety_index = float(safety_func())
    your_health_care_index = float(health_care_func())
    your_climate_index = float(climate_func())
    your_cost_of_living_index = float(cost_of_living_func())
    your_property_price_to_income_ratio = float(
        property_price_to_income_ratio_func(),
    )
    your_traffic_commute_time_index = float(traffic_commute_time_func())
    your_pollution_index = float(pollution_func())

    out_df = df[(df.purchasing_power_index > your_purchasing_power_index) &
                (df.safety_index > your_safety_index) &
                (df.health_care_index > your_health_care_index) &
                (df.cost_of_living_index < your_cost_of_living_index) &
                (
                    df.property_price_to_income_ratio <
                    your_property_price_to_income_ratio
                ) &
                (
                    df.traffic_commute_time_index <
                    your_traffic_commute_time_index
                ) &
                (df.pollution_index < your_pollution_index) &
                (df.climate_index > your_climate_index)]

    print_out_df = out_df[
        ["country", "freedomhouse_score", "quality_of_life_index"]
    ].dropna().sort_values(by=['freedomhouse_score'], ascending=False)

    if print_out_df.empty:
        print(
            text_color(
                f"There is no country better than {YOUR_COUNTRY}.",
                text_type.ANSWER,
            ),
        )
    else:
        with pd.option_context("display.max_rows", None, "display.max_columns", None):
            print(text_color(print_out_df, text_type.ANSWER))
