# GTiff-compare
Compare Two Rectified GeoTIFF Images

A quick-and-dirty comparison of bands between two rectified GeoTiffs can be a really handy tool - I was inspired by the work Dr Sang-Ho Yun did NASA's Jet Propulsion Lab to help direct rescuers to the areas that sustained the most damage after the 2015 Nepal earthquakes. (Link to further info below)

This script will work with two images that are rectified - that is, each pixel on Image A corresponds exactly on the earth's surface with the pixel drawn from the same index on Image B.

Our workflow is as follows:

1 Using the GDAL library, we open our GeoTIFFs and gather information to be used in our main function. 
2 We then pull the raster band info as an array, enabling simple comparison of the pixels by index. 
3 Finally, we perform our band math and append the result to our receptacle array.

Et voila! Return an array that holds values representing the differences between two GeoTIFFs. 

I am new here and always open to suggestions as to how to improve my code. Thanks!



The Economist on Dr Yun's work at the JPL, 14 Nov 2015: http://www.economist.com/news/science-and-technology/21678207-better-way-use-satellite-images-save-lives-after-tremors-compare-and
