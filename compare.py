import gdal
from gdalconst import *
gdal.UseExceptions()

tif = 'Your Tif Here'

# Open GeoTIFF with gdal
dataset = gdal.Open(tif,GA_ReadOnly)

# Set variables for easier calling later on
cols = dataset.RasterXSize
rows = dataset.RasterYSize
bands = dataset.RasterCount
driver = dataset.GetDriver().LongName

# Pull raster band info - in DEM GTiff there is only 1 band
band = dataset.GetRasterBand(1)
data = band.ReadAsArray(0,0,cols,rows) # now "data" is our array to iterate

# Prep for iteration
new_array = []                      # create empty, "receptacle" array
row_count = rows - 1
col_count = cols - 1

# Iterate through the array
while col_count >= 0:               # the key feature: our double while loop that -->

    while row_count >= 0:           # allows you to run through all the rows in a col
        value = data[col_count, row_count]
        new_array.append(value - 1) # (we will replace 1 with Tif2 value to find difference - when we get there)
        row_count -= 1
        
    col_count -= 1                  # and then move on to the next col
    row_count = rows - 1                # reset the row count - we need to go through all rows for each col

print new_array
