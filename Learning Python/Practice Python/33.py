# Birthday Dictionaries

import re

class BirthdaysAPI:
  MONTHS = [
    "January",  "February", "March",
    "April",    "May",      "June",
    "July",     "August",   "September",
    "October",  "November", "December"
  ]

  def __init__(self):
    self.birthdays = {}

  def __format_month(month):
    return BirthdaysAPI.MONTHS[month]
  
  def __format_day(day):
    tail = str(day)[-1]

    if tail == '1':
      return str(day) + "st"

    elif tail == '2':
      return str(day) + "nd"
    
    elif tail == '3':
      return str(day) + "rd"
    
    else:
      return str(day) + "th"
    
  def __format_birthday(birthday):
    month, day, year = birthday

    return f"{BirthdaysAPI.__format_month(month)} {BirthdaysAPI.__format_day(day)}, {year}"

  def add_birthday(self, name, month, day, year):
    self.birthdays[name] = (month, day, year)

  def has_birthday(self, name):
    return name in self.birthdays

  def get_birthday(self, name):
    return self.birthdays[name]
  
  def get_birthday_string(self, name):
    return BirthdaysAPI.__format_birthday(self.get_birthday(name))
  
  def get_birthdays(self):
    return self.birthdays
  
  def get_birthdays_string(self):
    if len(self.birthdays) == 0:
      return "None yet!"

    result = ""

    for name, birthday in self.birthdays.items():
      result += f"{name}: {BirthdaysAPI.__format_birthday(birthday)}\n"

    return result.strip()

class BirthdaysUI:
  MONTH_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  def __init__(self):
    self.api = BirthdaysAPI()

  def __get_month_index_by_number(month):
    month = month.strip()

    if re.search(r"^[0-9]+$", month) == None:
      return None

    if (month:=int(month) - 1) not in range(0, 12):
      return None
    
    return month
  
  def __get_month_index_by_name(month):
    month = month.strip().capitalize()

    if month not in BirthdaysAPI.MONTHS:
      return None

    return BirthdaysAPI.MONTHS.index(month)

  def __get_month_input():
    while True:
      month = input("Month: ")

      if (month_index:=BirthdaysUI.__get_month_index_by_number(month)) != None:
        return month_index

      if (month_index:=BirthdaysUI.__get_month_index_by_name(month)) != None:
        return month_index

  def __is_leap_year(year):
    if year % 100 == 0:
      return year % 400 == 0
    return year % 4 == 0

  def __get_month_length(month, year):
    if month == 1:
      return 29 if BirthdaysUI.__is_leap_year(year) else 28
    return BirthdaysUI.MONTH_LENGTHS[month]

  def __get_day_index(day, month, year):
    day = day.strip()

    if (day:=re.search(r"^[0-9]+", day)) == None:
      return None
    
    if (day:=int(day.group())) not in range(1, BirthdaysUI.__get_month_length(month, year) + 1):
      return None
    
    return day
  
  def __get_day_input(month, year):
    while True:
      day = input("Day: ")

      if (day_index:=BirthdaysUI.__get_day_index(day, month, year)) != None:
        return day_index

  def __get_year_index(year):
    year = year.strip()

    if re.search(r"^[0-9]+$", year) == None:
      return None
    
    return int(year)

  def __get_year_input():
    while True:
      year = input("Year: ")

      if (year_index:=BirthdaysUI.__get_year_index(year)) != None:
        return year_index
      
  def __get_name_input():
    return input("Name: ").strip()
      
  def __get_birthday_input():
    year = BirthdaysUI.__get_year_input()
    month = BirthdaysUI.__get_month_input()
    day = BirthdaysUI.__get_day_input(month, year)
    return (month, day, year)
  
  def run(self):
    while True:
      print("Birthdays in database:")
      print(self.api.get_birthdays_string())
      print()

      action = input("Add/get entry (or `exit` to exit): ").strip().lower()
      if action == "add":
        name = BirthdaysUI.__get_name_input()
        month, day, year = BirthdaysUI.__get_birthday_input()
        
        self.api.add_birthday(name, month, day, year)
        print("Added!")

      elif action == "get":
        name = BirthdaysUI.__get_name_input()

        if self.api.has_birthday(name):
          print(self.api.get_birthday_string(name))

        else:
          print("No birthday yet!")

      elif action == "exit":
        return
      
      print()

if __name__ == "__main__":
  birthdays = BirthdaysUI()
  birthdays.run()