# Task
from ntscraper import Nitter
import re
import time


# Function to scrape tweets from a Twitter account and count mentions of a stock symbol
def scrape_and_count_mentions(account, stock_symbol):
    nitter = Nitter()
    tweets = nitter.get_tweets(account, number=100)  # Scraping 100 tweets from the specified account
    mentions_count = 0

    # Regular expression pattern to search for stock symbols
    pattern = r'\$' + re.escape(stock_symbol) + r'\b'

    for tweet in tweets:
        try:
            # Check if the tweet content is available
            if 'content' in tweet:
                # Searching for mentions of the stock symbol in tweet text
                if re.search(pattern, tweet['content'], flags=re.IGNORECASE):
                    mentions_count += 1
        except Exception as e:
            print(f"Error processing tweet: {e}")
            continue  # Skip this tweet and continue with the next one

    return mentions_count


# List of Twitter accounts to scrape
twitter_accounts = [
    "Mr_Derivatives",
    "warrior_0719",
    "ChartingProdigy",
    "allstarcharts",
    "yuriymatso",
    "TriggerTrades",
    "AdamMancini4",
    "CordovaTrades",
    "Barchart",
    "RoyLMattox"
]

# Prompt user for the stock symbol
stock_symbol = input("Enter the stock symbol (e.g., TSLA, AAPL): $")

# Prompt user for the time interval (in minutes)
scraping_interval = int(input("Enter the time interval for scraping session (in minutes): "))

while True:
    total_mentions = 0

    # Scraping and counting mentions for each Twitter account
    for account in twitter_accounts:
        mentions = scrape_and_count_mentions(account, stock_symbol)
        total_mentions += mentions
        print(f"{account}: {mentions} mentions of {stock_symbol}.")

    print(f"Total mentions of {stock_symbol}: {total_mentions} in the last {scraping_interval} minutes.")
    print(f"Waiting {scraping_interval} minutes for the next scraping session...\n")

    time.sleep(scraping_interval * 60)    # Wait for the specified interval before scraping again