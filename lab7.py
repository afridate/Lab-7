import requests


def get_news(request_url):
    response = requests.get(request_url)
    data = response.json()
    print(data)


key = "308395f04a374fac9dd57310d7648847"

while True:
    option = input(
        "1 - top headlines for a country, "
        "2 - top headlines by source, "
        "3 - search by keyword, "
        "0 - exit: "
    )

    match option:
        case "1":
            country = input("Enter country: ")
            url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={key}"
            get_news(url)

        case "2":
            source = input("Enter source: ")
            url = f"https://newsapi.org/v2/top-headlines?sources={source}&apiKey={key}"
            get_news(url)

        case "3":
            keyword = input("Enter keyword: ")
            date = input("Enter date (YYYY-MM-DD): ")
            sort = input("Sort by: ")
            url = f"https://newsapi.org/v2/everything?q={keyword}&from={date}&sortBy={sort}&apiKey={key}"
            get_news(url)

        case "0":
            break

        case _:
            print("Try again!")
