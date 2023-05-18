# Birthday Months

import json
from collections import Counter

MONTHS = [
  "January",  "February", "March",
  "April",    "May",      "June",
  "July",     "August",   "September",
  "October",  "November", "December"
]

if __name__ == "__main__":
  with open("34.json", 'r') as f:
    birthdays = json.load(f)

    # counts = {}
    # for name, birthday in birthdays.items():
    #   month, day, year = birthday

    #   month = MONTHS[month]
    #   if month not in counts:
    #     counts[month] = 0
    #   counts[month] += 1

    # print(counts)
      
    months = []
    for name, birthday in birthdays.items():
      month, day, year = birthday

      months.append(MONTHS[month])

    print(Counter(months))