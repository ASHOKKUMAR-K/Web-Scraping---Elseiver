# Import Packages
import elseiver_scrapper


def scrape_elseiver():
    scrapper = elseiver_scrapper.Scrapper()
    scrapper.scrape()


if __name__ == "__main__":
    scrape_elseiver()