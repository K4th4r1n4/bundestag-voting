import logging

from pathlib import Path
import requests
from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By


class BundestagVoting:
    """ToDo"""

    def __init__(self):
        """Initialization."""
        self._configure_logging()
        self.url = "https://www.bundestag.de/parlament/plenum/abstimmung/liste"
        self.download_links = []
        self.browser = webdriver.Firefox()

    def extract_download_links(self):
        """Extract xls download links from page source."""
        content = self.browser.page_source
        for cont in content.split('<ul class="bt-linkliste">')[1:]:
            raw_link = BeautifulSoup(cont, "html").find_all(
                "a", class_="bt-link-dokument")[1]["href"]
            link = f"https://www.bundestag.de{raw_link}"
            self.download_links.append(link)

    def download(self):
        """ToDo"""
        for download_link in self.download_links:
            download_file_name = download_link.split("/")[-1]
            file_name = Path(download_file_name)
            response = requests.get(download_link)
            file_name.write_bytes(response.content)
            sleep(1.5)

    def next_page(self) -> None:
        """Slide to next page."""
        button_right = self.browser.find_elements(
            By.CLASS_NAME, "icon-facelift-slider-arrow"
        )[1]
        button_right.click()
        sleep(5)

    def _configure_logging(self):
        """Helper method to configure logging."""
        class_name = self.__class__.__name__
        package_name = self.__module__.split(".")[0]
        self.logger = logging.getLogger(f"{package_name}.{class_name}")
