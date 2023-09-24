import requests
import urllib.parse


def get_wikipedia_page_info(title):
    # Construct the Wikipedia API URL
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": title,
        "prop": "extracts|info",
        "exintro": True,
        "explaintext": True,
        "inprop": "url",
    }

    # Make the API request
    response = requests.get(api_url, params=params)
    data = response.json()

    # Extract page information
    pages = data.get("query", {}).get("pages", {})
    if not pages:
        print("Page not found.")
        return

    page_info = list(pages.values())[0]

    title = page_info.get("title")
    summary = page_info.get("extract")
    url = page_info.get("fullurl")

    return title, summary, url


while True:
    user_input = input("Enter a page title or search phrase (or press Enter to exit): ")
    if not user_input:
        break

    try:
        title, summary, url = get_wikipedia_page_info(user_input)
        print("Title:", title)
        print("Summary:", summary)
        print("URL:", url)
    except Exception as e:
        print("An error occurred:", str(e))
