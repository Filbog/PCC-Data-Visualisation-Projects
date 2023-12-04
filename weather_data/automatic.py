from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# path = Path("weather_data/sitka_weather_2021_simple.csv")


def get_indexes(header_row):
    date_index = header_row.index("DATE")
    highs_index = header_row.index("TMAX")
    lows_index = header_row.index("TMIN")
    print(date_index, highs_index, lows_index)
    return date_index, highs_index, lows_index


def get_weather_data(path):
    lines = path.read_text().splitlines()

    reader = csv.reader(lines)
    # with this line we get the first line in the .csv file which contains headers
    header_row = next(reader)
    d, h, l = get_indexes(header_row)
    dates = []
    highs = []
    lows = []
    reader = list(reader)
    station_name = reader[1][1].split(",")[0].strip().title()
    for row in reader:
        current_date = datetime.strptime(row[d], "%Y-%m-%d")

        try:
            high = int(row[h])
            low = int(row[l])
        except ValueError:
            print(f"no value for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows, station_name


def generate_chart(dates, highs, lows, station_name):
    plt.style.use("bmh")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color="red", linewidth="1")
    ax.plot(dates, lows, color="blue", linewidth="1")
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    ax.set_title(f"Daily high and low temps for {station_name}, 2021", fontsize=16)
    ax.set_xlabel("", fontsize=16)
    # this line makes dates appear diagonally, so they don't overlap
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(labelsize=16)
    # make the scale on Y-axis bigger
    # ax.set_ylim([10, 140])
    plt.show()


sitka_path = Path("weather_data/sitka_weather_2021_simple.csv")
dates, highs, lows, station_name = get_weather_data(sitka_path)
generate_chart(dates, highs, lows, station_name)
