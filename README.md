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
