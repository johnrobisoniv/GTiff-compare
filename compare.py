import gdal
from gdalconst import *

filename1 = "Your GeoTiff 1 Here"
filename2 = "Your GeoTiff 2 Here"

# Open GeoTIFF1 with gdal, gather information
dataset1 = gdal.Open(filename1, GA_ReadOnly)

cols1 = dataset1.RasterXSize
rows1 = dataset1.RasterYSize
bands1 = dataset1.RasterCount
driver1 = dataset1.GetDriver().LongName

# Open GeoTIFF2 with gdal, gather information
dataset2 = gdal.Open(filename2, GA_ReadOnly)

cols2 = dataset2.RasterXSize
rows2 = dataset2.RasterYSize
bands2 = dataset2.RasterCount
driver2 = dataset2.GetDriver().LongName

# Pull raster band info from both images - in DEM GTiff there is only 1 band
band1 = dataset1.GetRasterBand(1)
data1 = band1.ReadAsArray(0,0,cols1,rows1)

band2 = dataset2.GetRasterBand(1)
data2 = band2.ReadAsArray(0,0,cols2,rows2)


# Prepare variables for the main function
difference = []                     # create empty, "receptacle" array
subdiff = []                        # create subarray to build each row of differences in 
row_count = rows1 - 1               # set count as indices
col_count = cols1 - 1

while row_count >= 0:               # the key feature: our double while loop that /
    while col_count >= 0:           # allows you to run through all the values (really cols) in a row
        value1 = data1[col_count, row_count]
        value2 = data2[col_count, row_count]
        subdiff.append(value1 - value2) # our key function - the difference between pixel elev values
        col_count -= 1              # move on to the next index in both data1 and data2
    difference.append(subdiff)      # once row is built, append subarray to main array
    subdiff = []                    # reset subarray to take next row's differences
    row_count -= 1                  # and then move on to the next row
    col_count = cols1 - 1                # reset the col count - we need to go through all rows for each col

print difference
