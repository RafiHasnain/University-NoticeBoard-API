import requests
import bs4
import json

res = requests.get('https://www.aiub.edu/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

notices = soup.find_all("div", class_="card-block px-2")
dates = soup.find_all("div", class_="date align-middle")
links = soup.find_all('div', class_="card-block px-2")

info = []
URL = []
for links in soup.find_all('div', class_="card-block px-2"):
    for link in links.find_all('a'):
        URL.append("https://www.aiub.edu/"+link.get('href'))
i = 0
while i <= 5:

    information = {}
    information['notice'] = ((notices[i].getText()).strip())
    information['date'] = ((dates[i].getText()).strip())
    information['url'] = URL[i]
    info.append(information)
    with open("notices.json", "w") as f:
        f.write(json.dumps(info, indent=4))
    i += 1
