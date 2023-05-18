# Decode A Web Page Two

from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":
  url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
  html = requests.get(url).text

  soup = BeautifulSoup(html)

  p_list = soup.find_all("p", {"class": "paywall"})
  p_string_list = list(filter(lambda x: x != None, map(lambda x: x.string, p_list)))
  p_string = "\n".join(p_string_list)

  print(p_string)