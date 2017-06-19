### Aim
To reverse engineer chloropleth maps and extract data from them

### Pipeline
* User shall pass arguments specifying whether the map contains text labels(for states/districts) or not
* If yes, then phase 1 of the pipeline shall be skipped.

1. Merge map with text-labeled map. This step shall ensure that maps of all dimensions can be used.
2. Create bounding boxes for the text labels and identify text using OCR, identify the background colour(range) of the text box(or a point rather) using CV techniques.
3. User will input the legend(for now) and then the text labels and their corresponding values shall be written to a csv file.
