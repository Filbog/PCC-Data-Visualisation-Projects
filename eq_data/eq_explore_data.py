from pathlib import Path
import json

import plotly.express as px


def convert_to_obj(path):
    # read data as a string and convert to a Python object
    # path = Path("Projects/Data Visualisation/eq_data/eq_data_1_day_m1.geojson")
    path = Path(path)
    contents = path.read_text()
    all_eq_data = json.loads(contents)
    return all_eq_data


def create_readable_ver(data):
    # create a more readable versio of the data file
    path = Path("Projects/Data Visualisation/eq_data/readable_eq_data.geojson")
    readable_contents = json.dumps(data, indent=4)
    path.write_text(readable_contents)


def get_title(data):
    title = data["metadata"]["title"]
    print(title)
    return title


def get_earthquakes(data):
    all_ex_dicts = data["features"]
    # print(len(all_ex_dicts))
    return all_ex_dicts


def get_eq_info(eq_dicts):
    mags, lons, lats, eq_titles = [], [], [], []
    for eq_dict in eq_dicts:
        mags.append(eq_dict["properties"]["mag"])
        lons.append(eq_dict["geometry"]["coordinates"][0])
        lats.append(eq_dict["geometry"]["coordinates"][1])
        eq_titles.append(eq_dict["properties"]["title"])

    return mags, lons, lats, eq_titles


def generate_eq_map(mags, lons, lats, eq_titles, data_title="placeholder"):
    title = data_title
    fig = px.scatter_geo(
        lat=lats,
        lon=lons,
        size=mags,
        title=title,
        color=mags,
        color_continuous_scale="Icefire",
        labels={"color": "Magnitude"},
        projection="natural earth",
        hover_name=eq_titles,
    )
    fig.show()


all_eq_data = convert_to_obj(
    "Projects/Data Visualisation/eq_data/eq_data_30_day_m1.geojson"
)
eqs = get_earthquakes(all_eq_data)
title = get_title(all_eq_data)
print(title)
mags, lons, lats, eq_titles = get_eq_info(eqs)
generate_eq_map(mags, lons, lats, eq_titles, title)
