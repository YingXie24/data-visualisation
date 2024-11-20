import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_column_index(header_row, required_column_name):
    """Get columnn index of required_column_name from header_row."""
    for index, column_name in enumerate(header_row):
        if column_name == required_column_name:
            required_index = index
    return required_index


with open('data/death_valley_2018_simple.csv') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Automate index of required rows.
    index_station = get_column_index(header_row, 'NAME')
    index_date = get_column_index(header_row, 'DATE')
    index_high = get_column_index(header_row, 'TMAX')
    index_low = get_column_index(header_row, 'TMIN')

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