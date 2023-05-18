# Birthday Plots

import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
  with open("36.json", 'r') as f:
    birthdays = json.load(f)

    plt.hist(birthdays.values())
    plt.show();