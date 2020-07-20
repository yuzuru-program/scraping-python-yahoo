import urllib.request as request
from bs4 import BeautifulSoup

req = request.Request(
    "https://www.yahoo.co.jp",
    None,
    {}
)

instance = request.urlopen(req)
soup = BeautifulSoup(instance, "html.parser")

li = soup.select('main article section ul')[0].select('li')

for m in li:
    print(m.text)
    print(m.select("a")[0].get("href"))
    print()
