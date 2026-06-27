from pathlib import Path
import json 

import plotly.express as px

path = Path("eq_data/all_week.geojson")
contents = path.read_text(encoding="utf-8")
all_data = json.loads(contents)

# make readable geojson-file
path = Path("eq_data/readalbe_all_week.geojson")
readable_contents = json.dumps(all_data, indent=4)
path.write_text(readable_contents)

# extract data
all_eq = all_data["features"]
mags, lons, lats, eq_names = [], [], [], []
for eq in all_eq:
    mag = eq["properties"]["mag"]
    if mag > 0:
        mags.append(mag)
        lons.append(eq["geometry"]["coordinates"][0])
        lats.append(eq["geometry"]["coordinates"][1])
        eq_names.append(eq["properties"]["title"])

# visualize data
fig = px.scatter_geo(lon=lons, lat=lats, size=mags)
fig.show() 