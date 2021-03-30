import pandas as pd


def retrieve_soccer_schedule():
    url = "https://www.espn.com/soccer/schedule/_/league/ger.1"

    # Returns a list of tables -- We know that the first one
    # is the one we want
    return pd.read_html(url)[0]


if __name__ == "__main__":
    df = retrieve_soccer_schedule()
    df.to_csv("soccer_schedule.csv")
