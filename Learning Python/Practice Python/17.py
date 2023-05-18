# Decode A Web Page

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
  url = "https://www.nytimes.com/"
  html = requests.get(url).text

  soup = BeautifulSoup(html)

  h3_list = soup.find_all("h3")
  h3_string_list = list(map(lambda x: x.string, h3_list))

  print(h3_string_list)