from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


class Scraper:
    folders = []

    def __init__(self, domain: str, url: str) -> None:
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self.driver.get(url)
        sleep(2)
        self.main_page_content = self.driver.page_source
        self.domain = domain
        self.folder_link = url

    def fetch_list(self, link: str, item_type: str) -> list:
        self.driver.get(link)
        sleep(2)
        html_tree = BeautifulSoup(self.driver.page_source, "html.parser")
        main_content_area = html_tree.find("div", {"id": "content"})
        folders_soup = main_content_area.find_all("li", {"class": f"item {item_type}"})
        items = []
        for item in folders_soup:
            folder = item.find("a", href=True)
            folder_title = folder.find("span", {"class": "label"})["title"]
            folder_link = folder["href"]
            items.append({"title": folder_title, "link": self.domain + folder_link})
        return items

    def fetch_folder_info(self) -> dict:
        self.folders = self.fetch_list(self.folder_link, "folder")
        return self.folders

    def fetch_folder_item(self):
        for folder in self.folders:
            folder["items"] = self.fetch_list(folder["link"], "file")
        return self.folders

    def close(self):
        self.driver.close()


def main():
    current_domain = "http://ftp4.circleftp.net"
    url_link = "http://ftp4.circleftp.net/FILE/English%20%26%20Foreign%20TV%20Series/Friends%20%28TV%20Series%201994-2004%29"

    scraper = Scraper(current_domain, url_link)
    scraper.fetch_folder_info()
    print(scraper.fetch_folder_item())
    scraper.close()


if __name__ == "__main__":
    main()
