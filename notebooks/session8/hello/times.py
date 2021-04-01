import pandas as pd


def convert_to_TX_time(ts):
    return ts.tz_convert("US/Central")


def convert_to_DE_time(ts):
    return ts.tz_convert("Europe/Berlin")


if __name__ == "__main__":
    ts = pd.Timestamp.utcnow()

    print(f"The time in TX is {convert_to_TX_time(ts)}")
    print(f"The time in DE is {convert_to_DE_time(ts)}")