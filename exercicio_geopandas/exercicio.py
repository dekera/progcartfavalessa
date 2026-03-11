import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Ler CSV
df = pd.read_csv("pontos.csv")

# Criar GeoDataFrame
gdf = gpd.GeoDataFrame(df,
    geometry=gpd.points_from_xy(
    df.lon, df.lat),
    crs="EPSG:4326"
)

print(gdf.head())