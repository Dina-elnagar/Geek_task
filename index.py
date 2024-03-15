# # import requests
# # from bs4 import BeautifulSoup
# # import time
#
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
#
#
# def scrape_twitter_account(account_url):
#     driver = webdriver.Chrome()  # Adjust this according to your browser and webdriver location
#     driver.get(account_url)
#     time.sleep(5)  # Give time for the page to fully load
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()
#     return soup
#
#
# # Rest of the code remains the same...
#
#
# # this is default one
# # def scrape_twitter_account(account_url):
# #     headers = {'User-Agent': 'Mozilla/5.0'}
# #     response = requests.get(account_url, headers=headers)
# #     soup = BeautifulSoup(response.text, 'html.parser')
# #     return soup
#
# # this to show the page in the terminal
# # def scrape_twitter_account(account_url):
# #     headers = {'User-Agent': 'Mozilla/5.0'}
# #     response = requests.get(account_url, headers=headers)
# #     soup = BeautifulSoup(response.text, 'html.parser')
# #     print(soup.prettify())  # Print out the HTML content for debugging
# #     return soup
#
#
# # this is default one
# # def count_stock_mentions(soup, ticker):
# #     tweets = soup.find_all('div', class_='tweet')
# #     count = 0
# #     for tweet in tweets:
# #         tweet_text = tweet.find('div', class_='js-tweet-text-container').text
# #         if f"${ticker}" in tweet_text:
# #             count += 1
# #     return count
#
# # def count_stock_mentions(soup, ticker):
# #     tweets = soup.find_all('div', class_='tweet')
# #     count = 0
# #     for tweet in tweets:
# #         tweet_text = tweet.find('div', class_='js-tweet-text-container').text
# #         print("Tweet Text:", tweet_text)
# #         if f"${ticker}" in tweet_text:
# #             print("Stock symbol found in tweet!")
# #             count += 1
# #     return count
#
# def count_stock_mentions(soup, ticker):
#     tweets = soup.find_all('div',
#                            class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0')
#     count = 0
#     for tweet in tweets:
#         tweet_text = tweet.find('div',
#                                 class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-9ilb82 r-qvutc0').text
#         print("Tweet Text:", tweet_text)
#         if f"${ticker}" in tweet_text:
#             print("Stock symbol found in tweet!")
#             count += 1
#     return count
#
#
# def main():
#     twitter_accounts = [
#         "https://twitter.com/Mr_Derivatives",
#         "https://twitter.com/warrior_0719",
#         "https://twitter.com/ChartingProdigy",
#         "https://twitter.com/allstarcharts",
#         "https://twitter.com/yuriymatso",
#         "https://twitter.com/TriggerTrades",
#         "https://twitter.com/AdamMancini4",
#         "https://twitter.com/CordovaTrades",
#         "https://twitter.com/Barchart",
#         "https://twitter.com/RoyLMattox"
#     ]
#
#     ticker = input("Enter the stock symbol : ").upper()
#     interval_minutes = int(input("Enter the time interval for scraping (in minutes): "))
#
#     while True:
#         total_mentions = 0
#         for account_url in twitter_accounts:
#             soup = scrape_twitter_account(account_url)
#             mentions = count_stock_mentions(soup, ticker)
#             total_mentions += mentions
#
#         if total_mentions == 0:
#             print(f"{ticker} was not mentioned in the last {interval_minutes} minutes.")
#         else:
#             print(f"{ticker} was mentioned {total_mentions} times in the last {interval_minutes} minutes.")
#
#         time.sleep(interval_minutes * 60)
#
#
# # def main():
# #     twitter_accounts = [
# #         "https://twitter.com/Mr_Derivatives",
# #         "https://twitter.com/warrior_0719",
# #         "https://twitter.com/ChartingProdigy",
# #         "https://twitter.com/allstarcharts",
# #         "https://twitter.com/yuriymatso",
# #         "https://twitter.com/TriggerTrades",
# #         "https://twitter.com/AdamMancini4",
# #         "https://twitter.com/CordovaTrades",
# #         "https://twitter.com/Barchart",
# #         "https://twitter.com/RoyLMattox"
# #     ]
# #
# #     ticker = input("Enter the stock symbol ($) : ").upper()
# #     interval_minutes = int(input("Enter the time interval for scraping (in minutes): "))
# #
# #     while True:
# #         total_mentions = 0
# #         for account_url in twitter_accounts:
# #             soup = scrape_twitter_account(account_url)
# #             mentions = count_stock_mentions(soup, ticker)
# #             total_mentions += mentions
# #
# #         print(f"{ticker} was mentioned {total_mentions} times in the last {interval_minutes} minutes.")
# #         time.sleep(interval_minutes * 60)
#
#
# if __name__ == "__main__":
#     main()


# import requests
# from bs4 import BeautifulSoup
# import time
#
#
# # def scrape_twitter_account(account_url):
# #     headers = {'User-Agent': 'Mozilla/5.0'}
# #     response = requests.get(account_url, headers=headers)
# #     soup = BeautifulSoup(response.text, 'html.parser')
# #     return soup
#
# def scrape_twitter_account(account_url):
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     response = requests.get(account_url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.prettify())  # Print out the HTML content for debugging
#     return soup
#
#
# def count_stock_mentions(soup, ticker):
#     # tweets = soup.find_all('div', class_='css-1dbjc4n r-18u37iz r-thb0q2')
#     tweets = soup.find_all('div', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu')
#     count = 0
#     for tweet in tweets:
#         tweet_text = tweet.find('div', class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-9ilb82 r-1jw0kru r-1jw0kru r-1w50u8q r-o7ynqc r-6416eg')
#         # tweet_text = tweet.find('div', class_='css-1rynq56 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim').text
#         if f"${ticker}" in tweet_text:
#             count += 1
#     return count
#
#
# def main():
#     twitter_accounts = [
#         "https://twitter.com/Mr_Derivatives",
#         "https://twitter.com/warrior_0719",
#         "https://twitter.com/ChartingProdigy",
#         "https://twitter.com/allstarcharts",
#         "https://twitter.com/yuriymatso",
#         "https://twitter.com/TriggerTrades",
#         "https://twitter.com/AdamMancini4",
#         "https://twitter.com/CordovaTrades",
#         "https://twitter.com/Barchart",
#         "https://twitter.com/RoyLMattox"
#     ]
#
#     ticker = input("Enter the stock symbol (without $): ").upper()
#     interval_minutes = int(input("Enter the time interval for scraping (in minutes): "))
#
#     while True:
#         total_mentions = 0
#         for account_url in twitter_accounts:
#             soup = scrape_twitter_account(account_url)
#             mentions = count_stock_mentions(soup, ticker)
#             total_mentions += mentions
#
#         if total_mentions == 0:
#             print(f"{ticker} was not mentioned in the last {interval_minutes} minutes.")
#         else:
#             print(f"{ticker} was mentioned {total_mentions} times in the last {interval_minutes} minutes.")
#
#         time.sleep(interval_minutes * 60)
#
#
# if __name__ == "__main__":
#     main()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import time


# def scrape_twitter_account(account_url):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Run in headless mode
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(account_url)
#     time.sleep(5)  # Wait for page to load (you may need to adjust this)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()  # Close the browser
#     return soup

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
#
#
# def scrape_twitter_account(account_url):
#     mobile_url = account_url.replace("twitter.com", "mobile.twitter.com")
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-web-security")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get(mobile_url)
#     time.sleep(5)  # Wait for the page to load
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()
#     return soup
#
#
# def count_stock_mentions(soup, ticker):
#     tweets = soup.find_all('div', class_='tweet-text')
#     count = 0
#     for tweet in tweets:
#         tweet_text = tweet.get_text()
#         if f"${ticker}" in tweet_text:
#             count += 1
#     return count
#
#
# def main():
#     twitter_accounts = [
#         "https://twitter.com/Mr_Derivatives",
#         "https://twitter.com/warrior_0719",
#         "https://twitter.com/ChartingProdigy",
#         "https://twitter.com/allstarcharts",
#         "https://twitter.com/yuriymatso",
#         "https://twitter.com/TriggerTrades",
#         "https://twitter.com/AdamMancini4",
#         "https://twitter.com/CordovaTrades",
#         "https://twitter.com/Barchart",
#         "https://twitter.com/RoyLMattox"
#     ]
#
#     ticker = input("Enter the stock symbol (without $): ").upper()
#     interval_minutes = int(input("Enter the time interval for scraping (in minutes): "))
#
#     while True:
#         total_mentions = 0
#         for account_url in twitter_accounts:
#             soup = scrape_twitter_account(account_url)
#             mentions = count_stock_mentions(soup, ticker)
#             total_mentions += mentions
#
#         if total_mentions == 0:
#             print(f"{ticker} was not mentioned in the last {interval_minutes} minutes.")
#         else:
#             print(f"{ticker} was mentioned {total_mentions} times in the last {interval_minutes} minutes.")
#
#         time.sleep(interval_minutes * 60)
#
#
# if __name__ == "__main__":
#     main()


import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup


def scrape_twitter_account(account_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(account_url)
    time.sleep(5)  # Wait for the page to load
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup


def count_stock_mentions(soup, ticker):
    tweets = soup.find_all('div', class_='tweet-text')
    count = 0
    for tweet in tweets:
        tweet_text = tweet.get_text()
        if f"${ticker}" in tweet_text:
            count += 1
    return count


def main():
    twitter_accounts = [
        "https://twitter.com/Mr_Derivatives",
        "https://twitter.com/warrior_0719",
        "https://twitter.com/ChartingProdigy",
        "https://twitter.com/allstarcharts",
        "https://twitter.com/yuriymatso",
        "https://twitter.com/TriggerTrades",
        "https://twitter.com/AdamMancini4",
        "https://twitter.com/CordovaTrades",
        "https://twitter.com/Barchart",
        "https://twitter.com/RoyLMattox"
    ]

    ticker = input("Enter the stock symbol (without $): ").upper()
    interval_minutes = int(input("Enter the time interval for scraping (in minutes): "))

    while True:
        total_mentions = 0
        for account_url in twitter_accounts:
            soup = scrape_twitter_account(account_url)
            mentions = count_stock_mentions(soup, ticker)
            total_mentions += mentions

        if total_mentions == 0:
            print(f"{ticker} was not mentioned in the last {interval_minutes} minutes.")
        else:
            print(f"{ticker} was mentioned {total_mentions} times in the last {interval_minutes} minutes.")

        time.sleep(interval_minutes * 60)


if __name__ == "__main__":
    main()
