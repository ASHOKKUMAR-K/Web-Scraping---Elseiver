# Import Packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scrapper:
    BASE_URL_1 = "https://www.elsevier.com/catalog?page="
    BASE_URL_2 = "&cat0=&cat1=&cat2=&exclude=aggregations&exclude=categories&producttype=journal&series=&size=20&sort=datedesc"

    def scrape(self):
        data = pd.DataFrame(columns=["Paper-Name", "Paper-url", "Posted-Year"])
        page = 1
        while True:
            # Generating URL
            url = self.get_url(page)

            # Hit URL and get response
            response = requests.get(url)

            if response.ok:
                html = response.content
                # Creating Soup
                soup = BeautifulSoup(html, "html.parser")

                # All Papers on current page
                all_papers_on_current_page = soup.find_all(['div'], class_='row listing-products')

                for paper in all_papers_on_current_page:
                    # Paper Name
                    paper_name = paper.find_all('a')[1].text
                    # Paper url
                    paper_url = paper.find_all('a')[1]['href']
                    # Posted year
                    posted_year = paper.find_all('div', class_='listing-products-info-text-meta')[0].find_all('p')[1].text[-4:]
                    print(paper_name, '\t', paper_url, '\t', posted_year)
                    data.appe


            else:
                print("URL error")
            if page == 1:
                break
            page += 1

    @staticmethod
    def get_url(page):
        return Scrapper.BASE_URL_1 + str(page) + Scrapper.BASE_URL_2