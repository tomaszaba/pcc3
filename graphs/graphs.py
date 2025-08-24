# ==============================================================================
#                                   MAKING PLOTS
# ==============================================================================

import matplotlib.pyplot as plt

## ---- Basic graphs -----------------------------------------------------------

squares = [1, 4, 9, 16, 25]
plt.style.use("seaborn-v0_8-dark-palette")
fig, ax = plt.subplots()
ax.plot(squares, linewidth=2, linestyle="dashed", color="pink")
ax.set_title("Square Numbers", fontsize=30)
ax.set_xlabel("Value", fontsize=12, color="green")
ax.set_ylabel("Square of Value", fontsize=20, color="red")
ax.tick_params(labelsize=12)
plt.show()

plt.style.use("seaborn-v0_8-dark")
fig, ax = plt.subplots()
ax.scatter(x=2, y=4, s=200, c="red")
ax.scatter(
    x=range(1,1002),
    y=[x**2 for x in range(1, 1002)],
    c=[x**2 for x in range(1, 1002)]
)
ax.ticklabel_format(style="plain")

## ---- Downloading data -------------------------------------------------------

from pathlib import Path
import csv
import pandas as pd

path = Path("data/sitka_weather_2021_simple-original.csv")
lines = path.read_text(encoding="utf-8").splitlines()
reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

temp = []
for row in reader:
    high = int(row[4])
    temp.append(high)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(temp, color="red")
ax.set_title("Daily Temperatures, July 2021", fontsize="16")
ax.set_xlabel(xlabel="", fontsize=12)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="y", which="minor", color="blue")
plt.show()

## ---- Dealing with the datatime module ---------------------------------------
``
from datetime import datetime

first_date = datetime.strptime("2021-07-01", "%Y-%m-%d")
print(first_date)

### Extract the dates ----
datesx = []
for da in reader:
    datesx.append(datetime.strptime(da[2], "%Y-%m-%d"))

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot("DATE", "TMAX", data=df, color="pink")
ax.plot("DATE", "TMIN", data=df, color="grey")
ax.set_xlabel("Month [M]")
ax.tick_params(labelsize=12)
ax.fill_between("DATE", "TMAX", "TMIN", data=df, facecolor="blue", alpha=0.1)

df = pd.read_csv("data/sitka_weather_2021_simple-original.csv")

date, high_temp, low_temp = [], [], []

for row in reader:
    date.append(datetime.strptime(row[2], "%Y-%m-%d"))
    high_temp.append(int(row[4]))
    low_temp.append(int(row[5]))

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.plot(date, high_temp)
ax.plot(date, low_temp)
ax.fill_between(date, low_temp, high_temp, facecolor="red", alpha=0.3)


## ---- Exercise 16.1 ----------------------------------------------------------

### Read-in data ----
path2 = Path("data/death_valley_2021_full.csv")
lines2 = path2.read_text("utf-8").splitlines()
data = csv.reader(lines2)

prcp, date = [], []

for row in data:
    date.append(datetime.strptime(row[2], "%Y-%m-%d"))
    prcp.append(float(row[3]))

## ---- Working with json files ------------------------------------------------
import json

path3 = Path("data/eq_data_1_day_m1.geojson")
df = json.loads(path3.read_text(encoding="utf-8"))

### Create a more readable version of the data ----
readable_content = json.dumps(df, indent=4)
path3.write_text(readable_content)

### Examine all earthquakes in the dataset ----
all_dict = df["features"]
print(len(all_dict))

### Extract magnitudes ----
mags = []
for x in all_dict:
    mag = x["properties"]["mag"]
    mags.append(mag)

### Extract location data ----
mags, lons, lats = [], [], []

for x in all_dict:
    mag = x["properties"]["mag"]
    mags.append(mag)
    lon = x["geometry"]["coordinates"][0]
    lat = x["geometry"]["coordinates"][1]
    lons.append(lon)
    lats.append(lat)

### Build a map ----
import plotly.express as px

fig = px.scatter_geo(
    lat=lats, 
    lon=lons, 
    title="Global Earthquakes",
    size=mags,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth"
)
fig.show()
