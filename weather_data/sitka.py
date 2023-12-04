from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
# with this line we get the first line in the .csv file which contains headers
header_row = next(reader)
# for i, col in enumerate(header_row):
#     print(i, col)
dates = []
highs = []
lows = []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", linewidth="1")
ax.plot(dates, lows, color="blue", linewidth="1")
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title("Daily high and low temps, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
# this line makes dates appear diagonally, so they don't overlap
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
# make the scale on Y-axis bigger
ax.set_ylim([10, 140])
plt.show()
