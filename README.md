# Fingerprinting Evasion
This project is designed to demonstrate how to use Selenium with undetected_chromedriver to scrape web pages while evading fingerprinting techniques. It includes code to configure the Chrome WebDriver with enhanced fingerprinting protection and to scrape data from web pages, specifically targeting the CreepJS website for demonstration purposes.

## Features
- Configures Chrome WebDriver with undetected_chromedriver to evade fingerprinting detection.
- Utilizes BeautifulSoup for parsing HTML content.
- Extracts fingerprint data from web pages to analyze browser characteristics.
- Saves fingerprint information to JSON files and captures page snapshots as PDFs.

# CreepJS Fingerprinting Evasion

## Prerequisites
Before running this project, ensure you have the following prerequisites set up:

1. **Python**: Make sure you have Python installed on your system. This project is compatible with Python 3.
2. **Chrome Browser**: Ensure you have Google Chrome browser installed on your system.
3. **Proxy Server**: You need access to a proxy server to configure the Chrome WebDriver. Replace the `PROXY` variable in the `main.py` script with your desired proxy server address and port.
4. **Dependencies**: Install the required Python dependencies specified in requirements.txt using pip.

## Installation
1. Clone this repository to your local machine.
2. Install the required Python dependencies using pip install -r requirements.txt

## Challenges
1. creepjs apperently is one of the best page which seems to have alot of tests/checks in order to identify the browser as human or bot.
2. It already has tests to block out the stealth which have been ever developed for the playwright(playwright-stealth) or Puppeteer-extra-plugin-stealth. This made it difficult to invade this using the existing developed libraries/tools.
3. creepjs had alot of coverage of tests including the broswer properties, navigator properties, hardware configuration etc. But appearently none of the above mentioned stealth tools were able to pretend as webdriver = False.
4. Thats where I tried using the undetected_chromedriver along with setting some extra properties to make it believe that its not a webdriver which is accessing the page.
5. Other than this proxies places an important role in keep refreshing the session to generate new fingerprints.
6. I tried using data center proxies from Germany, Romania and USA and all works fine. Also tested the residential proxies, they work on this as well.

