from bs4 import BeautifulSoup
from scraper import fetch_content


def fetch_folder_info(document: bytes, page_link: str) -> dict:
    # print(BeautifulSoup(document, "html.parser").prettify())
    html_tree = BeautifulSoup(document, "html.parser")
    main_content_area = html_tree.find("div", {"id": "content"})
    folders_soup = main_content_area.find_all("li", {"class": "item folder"})

    folders = []
    for item in folders_soup:
        folder = item.find("a", href=True)
        folder_title = folder.find("span", {"class": "label"})["title"]
        folder_link = folder["href"]
        folders.append({"title": folder_title, "link": page_link + folder_link})
    return folders


def main():
    url_link = "http://ftp4.circleftp.net/FILE/English%20%26%20Foreign%20TV%20Series/Friends%20%28TV%20Series%201994-2004%29"

    current_domain = "http://ftp4.circleftp.net"
    page_content = fetch_content(url_link)
    content_information = fetch_folder_info(page_content, current_domain)
    print(content_information)


if __name__ == "__main__":
    main()
