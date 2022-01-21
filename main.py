from flask import request


import requests


def fetchData(url: str) -> dict:
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("request fail to load")


def main():
    url_link = "http://ftp5.circleftp.net/FILE/Hindi%20TV%20Series/7%20Kadam%20%28TV%20Series%202021-%29/"
    page_information = fetchData(url_link)
    print(page_information)


if __name__ == "__main__":
    main()
