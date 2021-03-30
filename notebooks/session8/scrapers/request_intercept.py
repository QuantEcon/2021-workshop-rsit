import requests

import pandas as pd


def retrieve_vaccination_data():
    url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data"

    data = requests.get(url).json()

    return data


def parse_vaccine_json_to_df(data):
    df = pd.DataFrame(data["vaccination_data"])

    return df


if __name__ == '__main__':
    data = retrieve_vaccination_data()
    df = parse_vaccine_json_to_df(data)
    df.to_csv("vaccination_data.csv")
