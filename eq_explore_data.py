import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data_1_day_m1.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

# Make list of all earthquakes.
all_eq_dicts = all_eq_data['features']

# Extract magnitudes.
mags, lons, lats = [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

    lon = eq_dict['geometry']['coordinates'][0]
    lons.append(lon)

    lat = eq_dict['geometry']['coordinates'][1]
    lats.append(lat)

# Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")