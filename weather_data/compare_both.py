from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_weather_data(path, highs_index, lows_index):
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
        try:
            high = int(row[highs_index])
            low = int(row[lows_index])
        except ValueError:
            print(f"no value for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


sitka_path = Path("weather_data/sitka_weather_2021_simple.csv")
valley_path = Path("the_csv_file_format/weather_data/death_valley_2021_simple.csv")

s_dates, s_highs, s_lows = get_weather_data(sitka_path, 4, 5)
v_dates, v_highs, v_lows = get_weather_data(valley_path, 3, 4)

fig, ax = plt.subplots()

# Plot the high temperatures for both locations
ax.plot(s_dates, s_highs, c="red", alpha=0.5, label="Sitka Highs")
ax.plot(v_dates, v_highs, c="blue", alpha=0.5, label="Valley Highs")

# Plot the low temperatures for both locations
ax.plot(s_dates, s_lows, c="pink", alpha=0.5, label="Sitka Lows")
ax.plot(v_dates, v_lows, c="lightblue", alpha=0.5, label="Valley Lows")

ax.fill_between(s_dates, s_highs, s_lows, facecolor="blue", alpha=0.1)
ax.fill_between(v_dates, v_highs, v_lows, facecolor="blue", alpha=0.1)

# Set the chart title and label axes
ax.set_title("Daily high and low temperatures - 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

# Add a legend
ax.legend()

plt.show()
