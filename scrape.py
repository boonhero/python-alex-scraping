import re
import requests
from bs4 import BeautifulSoup
import json


# spoof some headers so the request appears to be coming from a browser, not a bot
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5)",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
    "accept-encoding": "gzip,deflate,sdch",
    "accept-language": "en-US,en;q=0.8",
}

def scrape_eventbrite(url):
    # url = "https://www.eventbrite.com/d/philippines--makati-city/events/?crt=regular&slat=14.5547&slng=121.0244&sort=best"
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("request denied")
        return
    else:
        print("scraping " + url)

    soup = BeautifulSoup(r.text, "html.parser")

    # get desired text from html
    script = soup.find_all('script', text=re.compile('define\(\'eb/require_app_config\','))
    json_text = re.search(r'^\s*define\(\'eb/require_app_config\',\s*({.*?})\s*$', str(script), flags=re.DOTALL | re.MULTILINE).group(1)
    json_text = json_text.splitlines()[1]
    json_text = re.sub("eventsCollection", "\"eventsCollection\"", json_text)
    print("{"+json_text[:-1]+"}")

    return json.loads("{"+json_text[:-1]+"}")

