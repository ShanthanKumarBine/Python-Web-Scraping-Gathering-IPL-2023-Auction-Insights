# Python Web Scraping: Gathering IPL 2023 Auction Insights

This project involves web scraping to gather data from two different websites. The first part of the project involves scraping data about countries from [ScrapeThisSite](https://www.scrapethissite.com/pages/simple/), while the second part involves scraping IPL 2023 auction data from [IPLT20](https://www.iplt20.com/auction/2023).

## Overview

The project consists of two main parts:

1. **Scraping Country Data:**
   - Utilized BeautifulSoup and Requests libraries in Python to scrape data from the [ScrapeThisSite](https://www.scrapethissite.com/pages/simple/) website.
   - Extracted information such as country name, capital, population, and area.
   - Converted the scraped data into a DataFrame using Pandas and saved it as a CSV file.

2. **Scraping IPL 2023 Auction Data:**
   - Scraped IPL 2023 auction data from the [IPLT20](https://www.iplt20.com/auction/2023) website using BeautifulSoup and Requests libraries.
   - Extracted details such as player name, base price, sold price, and franchise.
   - Created a DataFrame and saved the auction data as a CSV file.

## Project Files

- **country_data_scraper.py:** Python script for scraping country data.
- **IPL_auction_scraper.py:** Python script for scraping IPL 2023 auction data.
- **data_title.txt:** Text file containing the title of the scraped data from the ScrapeThisSite website.
- **Countries_of_the_World.csv:** CSV file containing the scraped country data.
- **Ipl_Auction_2023.csv:** CSV file containing the IPL 2023 auction data.
- **README.md:** This file providing an overview of the project.
