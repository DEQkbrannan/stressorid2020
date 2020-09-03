import rasterio.crs as rscrs
import rasterio as rsio

# check some properties of the source raster
# gonna need it in projected to calculate slope 
with rsio.open("data/LiDAR/be44123f8-2011") as ds:
    print(ds.crs)
    print(ds.crs.is_geographic)
    print(ds.crs.is_projected)

crs = rscrs.CRS.from_epsg(2992)

