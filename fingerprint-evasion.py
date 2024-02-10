import re
import json
import time
import base64
from bs4 import BeautifulSoup
import undetected_chromedriver as uc

# Configure your proxy host and port
PROXY = "vmw.xxxxxx.com:19888"


def configure_driver():
    """Configure and return a Chrome WebDriver instance with enhanced fingerprinting protection."""
    options = uc.ChromeOptions()
    options.add_argument(f'--proxy-server={PROXY}')
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "download.prompt_for_download": False,
    })
    driver = uc.Chrome(headless=False, use_subprocess=True, options=options)
    return enhance_browser_fingerprints(driver)


def enhance_browser_fingerprints(driver):
    """Enhance the driver to mimic human behavior and evade fingerprinting."""
    # Content script to modify browser properties
    content_script = """
        (function() {
            var properties = [
                'webdriver',
                '_Selenium_IDE_Recorder',
                'callSelenium',
                '_selenium',
                '__webdriver_script_fn',
                '__driver_evaluate',
                '__webdriver_evaluate',
                '__selenium_evaluate',
                '__fxdriver_evaluate',
                '__driver_unwrapped',
                '__webdriver_unwrapped',
                '__selenium_unwrapped',
                '__fxdriver_unwrapped',
                '__webdriver_script_func'
            ];

            // Hide WebDriver properties
            properties.forEach(function(property) {
                if (window.hasOwnProperty(property)) {
                    Object.defineProperty(window, property, { value: false, writable: false });
                }
            });
        })();
    """
    # Execute the content script using Chrome DevTools Protocol
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': content_script})
    return driver


def get_page_source(driver, url):
    """Get page source and return BeautifulSoup object."""
    driver.get(url)

    # Wait for page to load and have all statistics available
    for _ in range(60):
        time.sleep(1)
        if 'performance benchmark' in driver.page_source:
            break

    time.sleep(5)
    return BeautifulSoup(driver.page_source, 'lxml')


def extract_fingerprint_score(soup):
    """Extract fingerprint data from BeautifulSoup object."""
    fingerprint_score = {}
    try:
        fingerprint_score = {
            "fp_id": soup.select_one('div.ellipsis-all').text.split(':')[1].strip(),
            "trust_socre": soup.select_one('div.visitor-info div.col-six div').text.split(':')[1].strip(),
            "bot": soup.select_one(
                'div.visitor-info div.col-six:last-child div.block-text div:first-child').text.replace('bot: ', '')
        }

        for tag in soup.select_one('div.visitor-info div.col-six:last-child'):
            if 'lies' in tag.text:
                fingerprint_score["lies"] = re.search(r"\((\d+)\)", tag.text).group(1)
                break
    except Exception as e:
        print('Error occurred while extracting the statistics.', e)

    return fingerprint_score


def save_fingerprint_information(fingerprint_score, driver, attempt):
    """Save fingerprint score to a JSON file and page snapshot as a PDF."""
    # Save fingerprint score to a JSON file
    with open(f'creepjs_fingerprints_score_{attempt}.json', 'w') as fp:
        json.dump(fingerprint_score, fp, indent=3)

    # Save full page as PDF
    pdf_data = driver.execute_cdp_cmd('Page.printToPDF', {})
    pdf_bytes = base64.b64decode(pdf_data['data'])
    with open(f'creepjs_snapshot_{attempt}.pdf', 'wb') as pdf_file:
        pdf_file.write(pdf_bytes)


def main():
    """Main function to execute the web scraping and fingerprinting evasion process."""
    driver = None
    try:
        # Configure and initialize the WebDriver with enhanced fingerprinting protection
        driver = configure_driver()

        # Iterate through attempts
        for attempt in range(1, 5):
            # Get page source and parse with BeautifulSoup
            soup = get_page_source(driver, 'https://abrahamjuliot.github.io/creepjs/')

            # Extract fingerprint score data
            fingerprint_score = extract_fingerprint_score(soup)

            # Save fingerprint information
            save_fingerprint_information(fingerprint_score, driver, attempt)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the WebDriver session
        if driver is not None:
            driver.close()
            driver.quit()


if __name__ == "__main__":
    main()
