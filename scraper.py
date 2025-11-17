import requests
from bs4 import BeautifulSoup
import sys

# --- Constants ---
URL = "https://www.npr.org/"
# We must send a User-Agent header, or many sites will block us!
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
OUTPUT_FILE = "headlines.txt"

# --- Emojis ---
SPARKLE = "✨"
ROBOT = "🤖"
NEWSPAPER = "📰"
CHECK_MARK = "✅"
CROSS_MARK = "❌"

def fetch_headlines():
    """
    Fetches the HTML content from the NPR website.
    """
    print(f"{ROBOT} Fetching headlines from NPR...")
    try:
        # A try-except block handles potential errors, like no internet
        response = requests.get(URL, headers=HEADERS)
        
        # This will raise an error if the download failed
        response.raise_for_status() 
        
        print(f"{CHECK_MARK} Website content fetched successfully!\n")
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"\n{CROSS_MARK} Error fetching website: {e}")
        print("Please check your internet connection or the URL.")
        sys.exit(1) # Exit the script if we can't get the news

def parse_headlines(html_content):
    """
    Parses the HTML to find all headlines.
    NPR headlines are in <h2> tags with the class 'title'.
    """
    print(f"{SPARKLE} Parsing HTML to find headlines...")
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # We find all <h2> tags that have a class attribute set to 'title'
    headlines = soup.find_all('h2', class_='title')
    
    # We clean up the list to get just the text
    cleaned_headlines = []
    for headline in headlines:
        # .text gets the text, .strip() removes whitespace
        text = headline.text.strip()
        if text: # Make sure it's not an empty headline
            cleaned_headlines.append(text)
            
    print(f"{CHECK_MARK} Found {len(cleaned_headlines)} headlines!\n")
    return cleaned_headlines

def save_headlines(headlines):
    """
    Saves the list of headlines to a text file.
    """
    print(f"📂 Saving headlines to {OUTPUT_FILE}...")
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            for headline in headlines:
                f.write(headline + '\n')
        
        print(f"{CHECK_MARK} All headlines saved successfully!")
        
    except IOError as e:
        print(f"\n{CROSS_MARK} Error saving file: {e}")

# --- Main Execution ---
def main():
    print(f"\n{NEWSPAPER} --- NPR News Scraper --- {NEWSPAPER}\n")
    html = fetch_headlines()
    if html:
        headlines_list = parse_headlines(html)
        if headlines_list:
            save_headlines(headlines_list)
    print("\n🤖 Scraper finished. Have a great day!\n")

if __name__ == "__main__":
    main()
