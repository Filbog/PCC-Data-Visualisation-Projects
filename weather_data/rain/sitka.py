from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path("weather_data/rain/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
# with this line we get the first line in the .csv file which contains headers
header_row = next(reader)
for i, col in enumerate(header_row):
    print(i, col)

dates = []
rains = []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    rain = float(row[5])
    dates.append(current_date)
    rains.append(rain)

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.bar(dates, rains, color="skyblue")

ax.set_title("Daily rain, July 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
# this line makes dates appear diagonally, so they don't overlap
fig.autofmt_xdate()
ax.set_ylabel("amount", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
