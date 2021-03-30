import requests

from bs4 import BeautifulSoup


def retrieve_webpage_soup():
    html = requests.get("https://magicseaweed.com/Baltrum-Surf-Report/1117/").text
    soup = BeautifulSoup(html)

    return soup


def extract_swell(soup):
    list_group_items = soup.find_all("li", attrs={"class": "list-group-item"})

    rows = []
    for item in list_group_items[:2]:
        out = {}
        out["variable"] = item.find("div", attrs={"class": "list-group-title"}).text.strip()
        out["value"] = item.find("div", attrs={"class": "list-group-content"}).text.strip()
        rows.append(out)

    return pd.DataFrame(rows)


if __name__=='__main__':
    soup = retrieve_webpage_soup()
    df = extract_swell(soup)
    df.to_csv("swell.csv")
