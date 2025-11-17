Task 3: Interview Questions
1. What is a GET request?
   
A GET request is one of the most common HTTP methods. It is used to retrieve or fetch data from a specified resource (like a server or a website). When you type a URL into your browser, you are sending a GET request.

2. How do you install external packages in Python?

You use pip, the package installer for Python. The command is pip install <package_name>. For example, to install requests, you would run pip install requests.

3. What is a User-Agent in HTTP?
   
A User-Agent is an HTTP header that is a string of text. It tells the server what kind of software (e.g., browser type, operating system) is making the request. Many websites block requests that don't have a valid User-Agent to prevent simple bots.

4. What is soup.find_all() used for?
   
In BeautifulSoup, soup.find_all(name, attrs, ...) is a method that finds all HTML tags that match the criteria you provide. For example, soup.find_all('h2', class_='title') finds every single <h2> tag that has an attribute class="title". It returns a list of all matching tags.

5. What are the risks of web scraping?
   
 * IP Blocking: The website can detect your high rate of requests and block your IP address.
 * Legal Issues: You might be breaking the website's Terms of Service. Scraping copyrighted data or personal information is illegal in many places.
 * Website Changes: Scrapers are fragile. If the website changes its HTML structure (e.g., changes a class name), your scraper will break.
 * Getting Bad Data: The site might intentionally feed you fake data if it detects you are a bot.
   
6. What's the difference between id and class in HTML?
   
 * id: Must be unique on a webpage. An id (like id="main-logo") can only be used on one element. It's like a person's social security number.
 * class: Can be re-used on many elements. A class (like class="headline") can be applied to all headline elements. It's like a person's job title (e.g., "teacher").
   
7. What is an HTML tag?

An HTML tag is the fundamental building block of an HTML page. It's a keyword enclosed in angle brackets (< >) that defines how content should be formatted or structured. For example, <p> defines a paragraph, <h2> defines a heading, and <a> defines a link.

8. What does .text return in BeautifulSoup?
   
The .text (or .get_text()) attribute on a BeautifulSoup object returns all the "human-readable" text content from within that tag, with all the HTML tags stripped out.

9. What is a try-except block?
    
A try-except block is Python's way of handling errors.
 * try: You put the code that might cause an error inside this block.
 * except: If an error does happen in the try block, the code in the except block is run instead of the program crashing. It lets you handle errors gracefully.
   
10. What are HTTP status codes?
    
HTTP status codes are 3-digit codes sent by the server to indicate the result of a request. Common ones include:
 * 200 OK: The request was successful.
 * 404 Not Found: The server could not find the requested resource.
 * 500 Internal Server Error: Something went wrong on the server's end.
 * 403 Forbidden: You are not allowed to access this resource.
 
