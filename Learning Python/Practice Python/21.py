# Write To A File

from bs4 import BeautifulSoup
import requests
import codecs

EXTRA = 0

if __name__ == "__main__":
  url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
  html = requests.get(url).text

  soup = BeautifulSoup(html)

  p_list = soup.find_all("p", {"class": "paywall"})
  p_string_list = list(filter(lambda x: x != None, map(lambda x: x.string, p_list)))
  p_string = "\n".join(p_string_list)

  filename = ""
  if EXTRA == 0:
    filename = "21.txt"

  elif EXTRA == 1:
    filename = input("File Name: ")

  # with codecs.open(filename, 'w', "utf-16") as f:
  with open(filename, 'w') as f:
    f.write(p_string)