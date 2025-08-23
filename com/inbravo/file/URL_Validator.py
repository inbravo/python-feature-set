from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

# This script fetches all hyperlinks from a given URL and checks their validity.
# URLValidator.py
# This script fetches all hyperlinks from a specified URL and checks their validity.
# It uses the requests library to make HTTP requests and BeautifulSoup to parse HTML content.
# URLValidator.py

def get_all_links(url):
    """
    Fetch all the hyperlinks from the given URL.

    This function sends an HTTP GET request to the specified URL, parses the HTML content,
    and extracts all the hyperlinks. It ensures that the extracted links are absolute URLs
    by resolving relative paths against the base URL.

    Args:
        url (str): The URL of the webpage to fetch links from.

    Returns:
        set: A set of absolute URLs (str) extracted from the webpage. If an error occurs
             during the request or parsing, an empty set is returned.

    Raises:
        None: Any exceptions during the request or parsing are caught and logged.
    """
    """Fetch all the links from the given URL."""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()
        for a_tag in soup.find_all("a", href=True):
            full_url = urljoin(url, a_tag["href"])
            links.add(full_url)
        return links
    except requests.RequestException as e:
        print(f"Error fetching links from {url}: {e}")
        return set()


def check_url_validity(url):
    """Check if a URL is valid."""
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            print(f"Valid URL: {url}")
        else:
            print(f"Invalid URL (status code {response.status_code}): {url}")
    except requests.RequestException as e:
        print(f"Error checking URL {url}: {e}")


def main():
    website_url = input("Enter the website URL: ").strip()
    print(f"Fetching links from {website_url}...")
    links = get_all_links(website_url)
    print(f"Found {len(links)} links. Checking validity...")
    for link in links:
        check_url_validity(link)


if __name__ == "__main__":
    main()
