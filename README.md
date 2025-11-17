<div align="center">
📰 NEWS-HEADLINE-SCRAPER 🤖

A Python bot that fetches the top headlines from NPR.

</div>
Overview
This project is a simple web scraper built in Python for Task 3 of the Python Developer Internship. It uses the requests library to fetch the HTML of the NPR (National Public Radio) website and BeautifulSoup to parse the HTML and extract all the top headlines.
The script then saves these headlines to a headlines.txt file, providing a clean, simple list of the latest news.
Features

 * 🤖 Smart Fetching: Uses a User-Agent header to mimic a real browser and avoid being blocked.
   
 * 📰 HTML Parsing: Intelligently finds all < h2 > tags with the class title to get clean headlines.
   
 * 📂 File Output: Saves all found headlines to a headlines.txt file, with one headline per line.
   
 * 🛡️ Error Handling: Includes try-except blocks to gracefully handle network errors or file-saving issues.
   
How to Run
1. Prerequisites
You must have Python 3 installed on your system.

2. Clone the Repository
git clone [https://github.com/Tethi04/News-Scraper-App/tree/main]

[https://tethi04.github.io/News-Scraper-App/]

cd News-Scraper-App

4. Install Dependencies
This project uses external packages. Install them easily using the requirements.txt file:
pip install -r requirements.txt

5. Run the Scraper
Execute the Python script from your terminal:
python scraper.py

6. Check the Results
After the script finishes (it's very fast!), you will find a new file named headlines.txt in the same folder. Open it to see all the scraped headlines!
<div align="center">
Created for the Python Developer Internship
</div>
