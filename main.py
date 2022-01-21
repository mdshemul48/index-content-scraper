from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


from bs4 import BeautifulSoup
from scraper import fetch_content


class Scraper:
    folders = []

    def __init__(self, domain: str, url: str) -> None:
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self.driver.get(url)
        self.main_page_content = self.driver.page_source
        self.domain = domain

    def fetch_folder_info(self) -> dict:
        html_tree = BeautifulSoup(self.main_page_content, "html.parser")
        main_content_area = html_tree.find("div", {"id": "content"})
        folders_soup = main_content_area.find_all("li", {"class": "item folder"})

        for item in folders_soup:
            folder = item.find("a", href=True)
            folder_title = folder.find("span", {"class": "label"})["title"]
            folder_link = folder["href"]
            self.folders.append(
                {"title": folder_title, "link": self.domain + folder_link}
            )

        return self.folders

    def close(self):
        self.driver.close()


# def
# def main():
#     url_link = "http://ftp4.circleftp.net/FILE/English%20%26%20Foreign%20TV%20Series/Friends%20%28TV%20Series%201994-2004%29"

#     current_domain = "http://ftp4.circleftp.net"
#     page_content = fetch_content(url_link)
#     content_information = fetch_folder_info(page_content, current_domain)
#     print(content_information)


if __name__ == "__main__":
    current_domain = "http://ftp4.circleftp.net"
    url_link = "http://ftp4.circleftp.net/FILE/English%20%26%20Foreign%20TV%20Series/Friends%20%28TV%20Series%201994-2004%29"

    scraper = Scraper(current_domain, url_link)
    print(scraper.fetch_folder_info())

    scraper.close()
