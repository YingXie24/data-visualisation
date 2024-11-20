import csv
from datetime import datetime
import matplotlib.pyplot as plt

with open('data/death_valley_2018_simple.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        if column_header == 'TMAX':
            index_high = index
        if column_header == 'TMIN':
            index_low = index
        if column_header == "DATE":
            index_date = index
        if column_header == "NAME":
            index_station = index

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        station_name  = row[index_station]
        current_date = datetime.strptime(row[index_date], "%Y-%m-%d")
        try:
            high = int(row[index_high])
            low = int(row[index_low])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
# print(plt.style.available)
plt.style.use("seaborn-v0_8-pastel")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="blue")
print(station_name)

# Shade area between two y-value series.
ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.2)

# Format plot.
title = f"Daily high and low temperatures, 2018\n{station_name}"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.set_ybound(0, 150)
ax.tick_params(axis="both", which="major", labelsize=16)

# Draw the date labels diagonally to prevent them from overlapping.
fig.autofmt_xdate()

plt.show()