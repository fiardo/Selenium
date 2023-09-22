import requests
from bs4 import BeautifulSoup

def get_network_calls(url):
    try:
        # Fetch the web page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx and 5xx)

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all the URLs (you can refine this based on your specific needs)
        urls = set()
        for link in soup.find_all('a', href=True):
            urls.add(link['href'])

        return urls
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    webpage_url = "https://www.universityliving.com/"  # Replace this with the URL of the web page you want to check
    network_calls = get_network_calls(webpage_url)
    if network_calls:
        print("Network calls on the web page:")
        for url in network_calls:
            print(url)
