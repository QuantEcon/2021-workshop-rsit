import requests

import pandas as pd


FRED_URL = "https://api.stlouisfed.org/fred"


def fred_series_request(series):
    key = "d4f97d5305ace8b756e361252fbf02cd"
    url = (
        FRED_URL +
        "/series/observations" +
        f"?series_id={series}&file_type=json&api_key={key}"
    )

    return requests.get(url).json()


if __name__ == "__main__":
    data = fred_series_request("GDP")
    df = pd.DataFrame(data["observations"])
    df.to_csv("GDP.csv")
