import csv 
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    ## Parse header row
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot the high and low temperatures.
    # print(plt.style.available)
    plt.style.use("seaborn-v0_8-pastel")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c="red")
    ax.plot(dates, lows, c="blue")

    # Shade area between two y-value series.
    ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.2)

    # Format plot.
    ax.set_title("Daily high and low temperatures, 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis="both", which="major", labelsize=16)

    # Draw the date labels diagonally to prevent them from overlapping.
    fig.autofmt_xdate()

    plt.show()
