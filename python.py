import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the elements you want to scrape
        # This example assumes you want to scrape article titles
        titles = soup.find_all('h2')  # Change 'h2' to the appropriate tag for your target site
        
        # Extract and print the text from each title
        for title in titles:
            print(title.get_text(strip=True))
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://intellipaat.com/blog/interview-questions/"  # Replace with the URL you want to scrape
    scrape_website(url)