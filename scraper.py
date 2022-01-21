from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def fetch_content(url: str) -> bytes:

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get(url)
    return driver.page_source


if __name__ == "__main__":
    url_link = "http://ftp5.circleftp.net/FILE/Hindi%20TV%20Series/7%20Kadam%20%28TV%20Series%202021-%29"
    print(fetch_content(url_link))
