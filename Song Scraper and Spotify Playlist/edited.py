from bs4 import BeautifulSoup
import requests

# Input date for Billboard URL
date = "2019-08-12"
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
request_call = requests.get(URL)

web_page = request_call.text
soup = BeautifulSoup(web_page, "html.parser")

# Find all 'h3' tags with id 'title-of-a-story'
all_tags_h3 = soup.find_all(name="h3", id="title-of-a-story")

# Extract and clean text from valid elements
song_titles = []
for h3 in all_tags_h3:
    text = h3.get_text(strip=True)
    # Add logic to filter out unwanted texts
    if "Songwriter" not in text and "Producer" not in text and "Imprint" not in text:
        song_titles.append(text)

# Print valid song titles
for title in song_titles:
    print(title)
