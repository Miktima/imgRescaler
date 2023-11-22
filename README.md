# imgRescaler
## Prepares photographies to upload their to public site, for example, TIMA PHOTOS (https://tmphotos.ru/) 

There are parameters of the result photos in the 'config.json' file for high resolution photography and thumbnail. The parameters are follow:
- maximal width for landscape photos;
- maximal height for portrait photos;
- quality (maximal - 100);
- dpi (dots per inch).
Addition parameters:
- suffix for thumbnails;
- folder for result photos.
Supported formats of photohraphies: JPEG, PNG
Photos are resized to new size with LANCZOS filter (https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-filters)
Aspect ratio is not changed.
