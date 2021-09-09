import requests
import bs4
import json

res = requests.get('https://www.aiub.edu/')


soup = bs4.BeautifulSoup(res.text, 'lxml')

# notices = soup.find_all("h5", class_="card-title")

# for link in soup.find_all('a'):
#     print(link.get('href'))


notices = soup.find_all("div", class_="card-block px-2")
dates = soup.find_all("div", class_="date align-middle")
links = soup.find_all('div', class_="card-block px-2")


# notices = soup.find_all("div", class_="notice")
# print(notices[0].getText())


# def write_json(data, filename="sample.json"):
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)

# def write_json(data, filename="sample.json"):
#     # json_object = json.dumps(a, indent=2)
#     with open(filename, "w") as f:
#         # write_file.write(json_object)
#         json.dump(data, f, indent=4)


#
# information = {}

# data1 = ["notice", "notice", "notice", "notice", "notice", "notice"]
# data2 = ["date", "date", "date", "date", "date", "date"]
# notice = {}
# date = {}
# info = [
#     "information": [information]

# ]
# information = []
info = []
URL = []
for links in soup.find_all('div', class_="card-block px-2"):
    for link in links.find_all('a'):
        URL.append("https://www.aiub.edu/"+link.get('href'))
i = 0
while i <= 5:
    # print(notices[i])
    # notice.append((notices[i].getText()).strip())
    # information = {"notice": ((notices[i].getText()).strip()),
    #                "date": ((dates[i].getText()).strip()),
    #                "url": URL[i]
    #                }

    # print(Convert_json(info))
    # print(json_covert(info))

    # write_json(info)
    information = {}
    information['notice'] = ((notices[i].getText()).strip())
    information['date'] = ((dates[i].getText()).strip())
    information['url'] = URL[i]
    info.append(information)
    with open("sample.json", "w") as f:
        f.write(json.dumps(info, indent=4))
    i += 1


# with open("sample.json") as json_file:
#     data = json.load(json_file)
#     temp = data["information"]
#     y = {"notice": "example", "date": "example", "url": "example"}
#     temp.append(y)
# write_json(data)
# Convert_json(info)
# notice = (notices.strip())

# information = {'notices': notice.strip(), 'dates': date.strip()}
# write_json(notices[i])


# i = 0
# while i <= 5:
# print(notices[i])
# date.append((dates[i].getText()).strip())
# information = {"date": ((dates[i].getText()).strip())}
# date["date"] = ((dates[i].getText()).strip())
# i += 1
# information = {'notices': notice.strip(), 'dates': date.strip()}
# print(dates[i].getText())
# write_json(notices[i])


# information = {'notices': notice, 'dates': date}

# for n in range(len(notice)):
#     information[n] = notice[n]
# for n in range(len(URL)):
#     information[[n]] = URL[n]

# it = dict(zip(date, notice))
# it1 = zip("date", date)
# it2 = zip(it, it1)
# information = dict(it)

# it = dict(zip(data1, notice))
# it1 = zip(data2, date)
# it2 = zip(it, it1)
# information = dict(zip(it, it1))

# i = 0
# while i <= 5:
#     information["notices"] = notice
#     information["dates"] = date
#     # information["url"] = URL
#     i += 1

# information["notice"] = notice

# notice1 = dict.fromkeys(notice)
# date1 = dict.fromkeys(date)

# information = {
#     "notice": notice,
#     "date": date,

# }

# print(info)
#  Json convertion code

#  Json convertion code
# json_object = json.dumps(information, indent=2)
# with open("sample.json", "w") as write_file:
#     write_file.write(json_object)


# print(len(notices))
# print(notice)

# i = 0
# while i <= 5:
#     print(notices[i].getText())
#     i += 1


# print(notices[0].getText())

# with open("sample.json", "w") as f:
#     json.dump(info, f, indent=2)
