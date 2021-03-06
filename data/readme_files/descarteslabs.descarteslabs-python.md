[![Build Status](https://travis-ci.org/descarteslabs/descarteslabs-python.svg?branch=master)](https://travis-ci.org/descarteslabs/descarteslabs-python)

Descarteslabs
=============

The documentation for the latest release can be found at [https://docs.descarteslabs.com](https://docs.descarteslabs.com)

Changelog
=========

## Pending

## [1.1.2] - 2020-03-12

1.1.2 fixes a bug which caused Workflows map layers to behave erratically when changing colormaps.

## [1.1.1] - 2020-03-11

1.1.1 fixes a packaging issue that caused `import descarteslabs.workflows` to fail.

It also makes NumPy an explicit dependency. NumPy was already a transitive dependency, so this shouldn't cause any changes.

You should _NOT_ install version 1.1.0; 1.1.1 should be used instead in all circumstances.

## [1.1.0] - 2020-03-11

### Catalog client

- `Image.upload()` now emits a deprecation warning if the image has a `cs_code` or `projection` property.
  The projection defined in the uploaded file is always used and applied to the resulting image in the Catalog.
- `Image.upload_ndarray()` now emits a deprecation warning if the image has both a `cs_code` and a `projection`
  property. Only one of them may be supplied, and `cs_code` is given preference.

### Scenes
- `SceneCollection.download_mosaic` has new default behavior for `mask_alpha` wherein the `alpha` band will be
  used as a mask by default if it is available for all scenes in the collection, even if it is not specified in
  the list of bands.

### Workflows (channel `v0-12`) - Added
- **Experimental Array API** following the same syntax as NumPy arrays. It supports vectorized operations, broadcasting,
  and multidimensional indexing.
  - `ndarray` attribute of `Image` and `ImageCollection` will return a `MaskedArray`.
  - Over 60 NumPy ufuncs are now callable with Workflows `Array`.
  - Includes other useful `Array` functions like `min()`, `median()`, `transpose()`, `concatenate()`, `stack()`, `histogram()`, and `reshape()`.
- **`ImageCollection.sortby_composite()`** for creating an argmin/argmax composite of an `ImageCollection`.
- **Slicing** of `List`, `Tuple`, `Str`, and `ImageCollection`.
- `wf.range` for generating a sequence of numbers between start and stop values.
- `ImageCollectionGroupby.mosaic()` for applying `ImageCollection.mosaic` to each group.
- `wf.exp()`, `wf.square()`, `wf.log1p()`, `wf.arcsin()`, `wf.arccos()`, and `wf.arctan()`
- `Datetime.is_between()` for checking if a `Datetime` falls within a specified date range
- `FeatureCollection.contains()`
- Container operations on `GeometryCollection` including:
  - `GeometryCollection.contains()`
  - `GeometryCollection.sorted()`
  - `GeometryCollection.map()`
  - `GeometryCollection.filter()`
  - `GeometryCollection.reduce()`
- `List` and `Tuple` can now be compared with other instances of their type via `__lt__()`, `__eq__()` etc.
- `List.__add__()` and `List.__mul__()` for concatenating and duplicating `List`s.

### Workflows - Changed
- Products without alpha band and `nodata` value are rejected, instead of silently producing unwanted behavior.
- `ImageCollection.concat_bands` now throws a better error when trying to concatenate bands from another `ImageCollection` that is not the same length.
- `Any` is now promotable to all other types automatically.
- Better error when trying to iterate over Proxytypes.
- Interactive map: calls to `visualize` now clear layer errors.
- Interactive map: when setting scales, invalid values are highlighted in red.
- Interactive map: a scalebar is shown on the bottom-left by default.
- `ImageCollection.mosaic()` now in "last-on-top" order, which matches with GDAL and `dl.raster`. Use `mosaic(reverse=True)` for the same ordering as in v1.0.0.

### Workflows - Fixed
- Better errors when specifying invalid type parameters for Proxytypes that require them.
- Field access on `Feature`, `FeatureCollection`, `Geometry`, and `GeomeryCollection` no longer fails.
- In `from_id`, processing level 'cubespline' no longer fails.


## [1.0.0] - 2020-01-20

| As of January 1st, 2020, the client library no longer supports Python 2. For more information, please contact support@descarteslabs.com. For help with porting to Python 3, please visit https://docs.python.org/3/howto/pyporting.html. |
| --------- |

### Catalog client
- There is an entirely new backend supporting asynchronous uploads of image files and ndarrays with
  the catalog client. There are minor changes to the `ImageUpload` class (a new `events` field has subsumed
  `errors`, and the `job_id` field has been removed) but the basic interface is unchanged so most
  code will keep functioning without any changes.
- It is now possible to cancel image uploads.
- Errors messages are now easier to read.
- Many improvements to the documentation.
- You can now create or retrieve an existing object using the `get_or_create` method.
- Retrieving a `Band` or `Image` by name is now possible by calling `get_band` or `get_image` on the
  `Product` instance. You can also use the Product's `named_id` function to get a complete id for
  images and bands.
- A new convenience function `make_valid_name` on `Image` and `Band` classes will return a sanitized
  name without invalid characters.
- A new property `ATTRIBUTES` enumerates which attributes are available for a specific catalog object.
- Trying to set an attribute that does not exist will now raise `AttributeError`.
- `update_related_objects_permissions()` should no longer fail with a JSON serialization error.
- Setting a read-only attribute will now raise an `AttributeValidationError`.
- Saving a new object while one with the same id already exists will now raise a `ConflictError`
  instead of `BadRequestError`.
- If a retrieved object has since been deleted from the catalog, saving any changes or trying to
  reload it will now raise a `DeletedObjectError`.
- Resolution fields now accept string values such as "10m" or "0.008 degrees". If the value cannot
  be parsed, an `AttributeValidationError` will be raised.
- Changes to the `extra_properties` attribute are now tracked correctly.

### Packaging
- This release no longer supports Python 2.
- This package is now distributed as a Python 3 wheel which will speed up installation.

### Workflows (channel `v0-11`) - Added
- **Handling of missing data** via empty ImageCollections
  - `ImageCollection.from_id` returns an empty ImageCollection if no data exist for the given time/place, rather than an error
  - `ImageCollection.filter` returns an empty ImageCollection if the predicate is False for every Image, rather than an error
  - `Image.replace_empty_with` and `ImageCollection.replace_empty_with` for explicitly filling in missing data
  - See the [Workflows guide](https://docs.descarteslabs.com/guides/workflows.html) for more information
- **Docstrings and examples** on every class and function!
- **Assigning new metadata to Image properties** & bandinfo: `Image.with_properties()`, `Image.with_bandinfo()`
- Interactive map: **colorbar legends** on layers with colormaps (requires matplotlib)
- **`Dict.from_pairs`**: construct a Dict from a sequence of key-value pairs
- Map displays a **fullscreen button** by default (**[breaking]** if your code adds one, you'll now get two)
- **`wf.concat`** for concatentating `Image` and `ImageCollection` objects
  - `ImageCollection.concat` now accepts `Image` objects; new `Image.concat` accepts `Image` or `ImageCollection`
- **`ImageCollection.mosaic()`**
- `FeatureCollection.sorted()`, `FeatureCollection.length()`, `FeatureCollection.__reversed__()`
- `GeometryCollection.length()`, `GeometryCollection.__reversed__()`

### Workflows - Changed
- **`wf.zip` now supports `ImageCollection`**, `FeatureCollection`, `GeometryCollection` as well as `List` and `Str`
- **Get a GeoContext for the current bounds of the map in any resolution, shape, or CRS** (including `"utm"`, which automatically picks the right UTM zone for you) with `wf.map.geocontext`. Also now returns a Scenes GeoContext for better introspection and use with Raster.
- Better backend type-checking displays the possible arguments for most functions if called incorrectly
- `arr_shape` included when calling `wf.GeoContext.compute()`
- More readable errors when communication with the backend fails
- Interactive map: layout handles being resized, for example setting `wf.map.layout.height = '1000px'`
- `Any` is no longer callable; `Any.cast` encouraged
- `remove_layer` and `clear_layers` moved from `wf.interactive.MapApp` class to `wf.interactive.Map` (non-breaking change)
- **[possibly breaking]** band renaming in binary operators only occurs when broadcasting: `red + red` is just `red`, rather than `red_add_red`. `red + blue` is still `red_add_blue`. Code which depends on accessing bands by name may need to change.

### Workflows - Fixed
- `wf.where` propagates masks correctly, and handles metadata correctly with multi-band inputs
- `processing_level="surface"` actually returns surface-reflectance-processed imagery
- `ImageCollection.sorted()` works properly
- Viewing global-extent WGS84 images on the Workflows map no longer causes errors
- `List` proxytype no longer infinitely iterable in Python
- Repeated use of `axis="bands"` works correctly
- `ImageCollection.from_images` correctly aligns the bands of the inputs
- Numeric casting (`wf.Int(wf.Float(2.2))`) works as expected
- More descriptive error when constructing an invalid `wf.Datetime`
- Computing a single `Bool` value derived from imagery works correctly


## [0.28.1] - 2019-12-10

### Changed
- Update workflows client channel
- Workflows map UI is more stable: errors and layers won't fill the screen

## [0.28.0] - 2019-12-09
### Added
- Catalog client: Added an `update()` method that allows you to update multiple attributes at once.

### Changed
- Catalog client: Images and Bands no longer reload the Product after calling `save`
- Catalog client: Various attributes that are lists now correctly track changes when modifying them with list methods (e.g. `Product.owners.append("foo")`)
- Catalog client: Error messages generated by the server have a nicer format
- Catalog client: Fix a bug that caused waiting for tasks to never complete
- The minimum `numpy` version has been bumped to 1.17.14 for Python version > 3.5, which addresses a bug with `scenes.display`

### Workflows (channel `v0-10`) - Added
- `.compute()` is noticeably faster
- Most of the Python string API is now available on `workflows.Str`
- Interactive map: more descriptive error when not logged in to iam.descarteslabs.com
- Passing the wrong types into functions causes more descriptive and reliable errors

### Workflows - Fixed
- `RST_STREAM` errors when calling `.compute()` have been eliminated
- `Image/ImageCollection.count()` is much faster
- `.buffer()` on vector types now works correctly
- Calling `.compute()` on a `GeometryCollection` works

## [0.27.0] - 2019-11-18
### Added

- Catalog client: Added a `MaskBand.is_alpha` attribute to declare alpha channel behavior for a band.

### Changed

- The maximum number of `extra_properties` allowed for Catalog objects has been increased from 10 to 50.
- Fixed bug causing `SceneCollection.download` to fail.

### Workflows (channel `v0-9`) - Added
- When you call `.compute()` on an `Image` or `ImageCollection`, the `GeoContext` is included on the result object (`ImageResult.geocontext`, `ImageCollectionResult.geocontext`)

### Workflows - Fixed
- Passing a Workflows `Timedelta` object (instead of a `datetime.timedelta`) into functions expecting it now behaves correctly
- Arguments to the reducer function for `reduce` are now in the correct order

## [0.26.0] - 2019-10-30
### Added

- A new catalog client in `descarteslabs.catalog` makes searching and managing products, bands and images easier. This client encompasses functionality previously split between the `descarteslabs.Metadata` and `descarteslabs.Catalog` client, which are now deprecated. Learn how to use the new API in the [Catalog guide](https://docs.descarteslabs.com/guides/catalog_v2.html).
- Property filtering expressions such as used in `scenes.search()` and `FeatureCollection.filter()` now support an `in_()` method.

### Changed

- `SceneCollection.download` previously always returned successfully even if one or more of the downloads failed. Now if any of the downloads fail, a RuntimeError is raised, which will detail which destination files failed and why.
- Fixed a bug where geometries used with the Scenes client had coordinates with reduced precision.

### Workflows (channel `v0-8`) - Added
- **Interactive parameters**: add parameters to map layers and interactively control them using widgets
- **Spatial convolution** with `wf.conv2d`
- Result containers have helpful `repr`s when displayed
- `Datetime` and `Timedelta` are unpacked into `datetime.datetime` and `datetime.timedelta` objects when computed.

### Workflows - Changed
- **[breaking]** Result containers moved to `descarteslabs/workflows/results` and renamed, appending "Result" to disambiguate (e.g. ImageResult and ImageCollectionResult)
- **[breaking] `.bands` and `.images` attributes of ImageResult and ImageCollectionResult renamed `.ndarray`**
- **[breaking]** When `compute`-ing an `Image` or `ImageCollection`, **the order of `bandinfo` is only correct for Python >= 3.6**
- Interactive maps: coordinates are displayed in lat, lon order instead of lon, lat for easier copy-pasting
- Interactive maps: each layer now has an associated output that is populated when running autoscale and deleted when the layer is removed
- Interactive maps: `Image.visualize` returns a `Layer` object, making it easier to adjust `Layer.parameters` or integrate with other widgets

### Workflows - Fixed
- Composing operations onto imported Workflows no longer causes nondeterministic errors when computed
- Interactive maps: `remove_layer` doesn't cause an error
- No more errors when creating a `wf.parameter` for `Datetime` and other complex types
- `.where` no longer causes a backend error
- Calling `wf.map.geocontext()` when the map is not fully initialized raises an informative error
- Operations on numbers computed from raster data (like `img_collection.mean(axis=None)`) no longer fail when computed
- Colormap succeeds when the Image contains only 1 value

## [0.25.0] - 2019-08-22
### Added

### Changed
- `Raster.stack` `max_workers` is limited to 25 workers, and will raise a warning and set the value to 25 if a value more than 25 is specified.

### Workflows (channel `v0-7`) - Added
- Interactive maps: `clear_layers` and `remove_layer` methods
- ImageCollections: `reversed` operator
- ImageCollections: `concat` and `sorted` methods
- ImageCollections: `head`, `tail`, and `partition` methods for slicing
- ImageCollections: `where` method for filtering by condition
- ImageCollections `map_window` method for applying sliding windows
- ImageCollections: Indexing into ImageCollections is supported (`imgs[1]`)
- **[breaking]** Statistics functions are now applied to named axes
- DateTime, Timedelta, Geocontext, Bool, and Geometry are now computable
- ImageCollectionGroupby ProxyObject for grouping ImageCollection by properties, and applying functions over groups
- ImageCollections: `groupby` method
- `parameter` constructor

### Workflows - Changed
- Interactive maps: autoscaling is now done in the background
- Tiles requests can now include parameters
- `median` is noticeably faster
- `count` is no longer breaks colormaps
- `map`, `filter`, and `reduce` are 2x faster in the "PREPARING" stage
- Significantly better performance for functions that reference variables outside their scope, like
```
overall_comp = ndvi.mean(axis="images")
deltas = ndvi.map(lambda img: img - overall_comp)
```
- Full support for floor-division (`//`) between Datetimes and Timedeltas (`imgs.filter(lambda img: img.properties['date'] // wf.Timedelta(days=14)`)

### Workflows - Removed
- **[breaking]** `ImageCollection.one` (in favor of indexing)

## [0.24.0] - 2019-08-01
### Added
- `scenes.DLTile.assign(pad=...)` method added to ease creation of a tile in all ways indentical except for the padding.

### Changed
- The parameter `nbits` has been deprecated for catalog bands.

### Workflows (channel `v0-6`) - Added
- New interactive map, with GUI controls for multiple layers, scaling, and colormaps.
- Colormaps for single-band images.
- Map interface displays errors that occur while the backend is rendering images.
- ImageCollection compositing no longer changes band names (`red` does not become `red_mean`, for example).
- `.clip()` and `.scale()` methods for Image/ImageCollection.
- Support specifying raster resampler method.
- Support specifying raster processing level: `toa` (top-of-atmosphere) or `surface` [surface reflectance).
- No more tiles 400s for missing data; missing/masked pixels can optionally be filled with a checkerboard pattern.

### Workflows - Changed
- Workflows `Image.concat` renamed `Image.concat_bands`.
- Data are left in `data_range` values if `physical_range` is not set, instead of scaling to the range `0..1`.
- Selecting the same band name twice (`img.pick_bands("vv vv")`) properly raises an error.
- Reduced `DeprecationWarning`s in Python 3.7.

## [0.23.0] - 2019-07-12
### Added
- Alpha Workflows API client has been added. Access to the Workflows backend is restricted; contact [support](https://descarteslabs.atlassian.net/servicedesk/customer/portals) for more information.
- Workflows support for Python 3 added in channel v0-5.

### Changed

## [0.22.0] - 2019-07-09
### Added
- Scenes API now supports band scaling and output type specification for rastering methods.
- Methods in the Metadata, Raster, and Vector service clients that accepted GeoJSON geometries now also accept Shapely geometries.

### Changed

## [0.21.0] - 2019-06-19
### Added
- Add support for user cython modules in tasks.

### Changed
- Tasks webhook methods no longer require a `group_id` if a webhook id is provided.
- `catalog_id` property on images is no longer supported by the API
- Fix `scenes.display` handling of single band masked arrays with scalar masks
- Fix problems with incomplete `UploadTask` instances returned by `vectors.FeatureCollection.list_uploads`

## [0.20.0] - 2019-06-04
### Added
- Metadata, Catalog, and Scenes now support a new `storage_state` property for managing image metadata and filtering search results. `storage_state="available"` is the default for new images and indicates that the raster data for that scene is available on the Descartes Labs platform. `storage_state="remote"` indicates that the raster data has not yet been processed and made available to client users.
- The following additional colormaps are now supported for bands ??? 'cool', 'coolwarm', 'hot', 'bwr', 'gist_earth', 'terrain'. Find more details about the colormaps [here](https://matplotlib.org/gallery/color/colormap_reference.html).
- `Scene.ndarray`, `SceneCollection.stack`, and `SceneCollection.mosaic` now support passing a string as the `mask_alpha` argument to allow users to specify an alternate band name to use for masking.
- Scenes now supports a new `save_image` function that allows a user to save a visualization given a filename and extension.
- Tasks now allows you to unambiguously get a function by group id using `get_function_by_id`.
- All Client APIs now accept a `retries` argument to override the default retry configuration. The default remains
the same as the prior behavior, which is to attempt 3 retries on errors which can be retried.

### Changed
- Bands of different but compatible types can now be rastered together in `Scene.ndarray()` and `Scene.download()` as well as across multiple scenes in `SceneCollection.mosaic()`, `SceneCollection.stack()` and `SceneCollection.download()`. The result will have the most general data type.
- Vector client functions that accept a `geometry` argument now support passing Shapely shapes in addition to GeoJSON.

### Fixed

## [0.19.0] - 2019-05-06
### Changed
- Removed deprecated method `Metadata.sources()`
- `FeatureCollection.filter(geometry)` will now raise an `InvalidQueryException` if you
  try to overwrite an existing geometry in the filter chain.  You can only set the
  geometry once.

### Fixed

## [0.18.0] - 2019-04-18
### Changed
- Many old and obsolete examples were removed from the package.
- `Scene.ndarray`, `SceneCollection.stack`, and `SceneCollection.mosaic` now will automatically mask alpha if the alpha band is available in the relevant scene(s), and will set `mask_alpha` to `False` if the alpha band does not exist.
- `FeatureCollection.add`, `FeatureCollection.upload`, `Vector.create_feature`, `Vector.create_features`, and `Vector.upload_features` all accept a `fix_geometry` string argument that determines how to handle certain problem geometries
including those which do not follow counter-clockwise winding order (which is required by the GeoJSON spec but not many
popular tools). Allowed values are ``reject`` (reject invalid geometries with an error), ``fix`` (correct invalid
geometries if possible and use this corrected value when creating the feature), and ``accept`` (the default) which will
correct the geometry for internal use but retain the original geometry in the results.
- `Vector.get_upload_results` and `Vector.get_upload_result` now accept a `pending` parameter to include pending uploads
in the results. Such pending results will have `status: PENDING` and, in lieu of a task id, the `id` attribute will contain
the upload id as returned by `Vector.upload_features`
- `UploadTask.status` no longer blocks until the upload task is completed, but rather returns the current status of the
upload job, which may be `PENDING`, `RUNNING`, `SUCCESS`, or `FAILURE`.
- The `FutureTask.ready` and `UploadTask.ready` property has been added to test whether the task has completed.
A return value of `True` means that if `get_result(wait=True)` were to be called, it would return without blocking.
- You can now export features to a storage `data` blob.  To export from the
`vector` client, use `Vector.export_product_from_query()` with a storage key
and an optional query.  This returns the task id of the export task.  You
can ask for status using `Vector.get_export_results()` for all export tasks
or `Vector.get_export_result()` for a specific task by task id.
- FeatureCollection has been extended with this functionality with a
`FeatureCollection.export()` method that takes a storage key.  This operates
on the filter chain that FeatureCollection represents, or the full product
if there is no filter chain.  It returns an `ExportTask` which behaves
similar to the `FutureTask`.
- `Catalog.upload_image()` and `Catalog.upload_ndarray()` now will return an `upload_id` that can be used to query the status of that upload using `Catalog.upload_result()`.  Note that the upload id is the image id and if you use identical image ids `Catalog.upload_result()` will only show the result of the most recent upload.

### Fixed
- Several typical kinds of non-conforming GeoJSON which previously caused errors can now be accepted or
fixed by the `FeatureCollection` and `Vector` methods for adding or uploading new vector geometries.

## [0.17.3] - 2019-03-06
### Changed
- Fixed issues with `Catalog.upload_ndarray()` under Windows
- Added header to client requests to better debug retries

### Fixed
- Improved error messages for Catalog client upload methods

## [0.17.2] - 2019-02-26
### Changed
- Tasks methods `create_function`, `create_or_get_function`, and `new_group` now have image as a required parameter
- The `name` parameter is renamed to `product_id` in `Vector.create_product`, and `FeatureCollection.create` and `FeatureCollection.copy`.  The 'name' parameter is renamed to `new_product_id` in `Vector.create_product_from_query`.  Using `name` will continue to work, but will be removed completely in future versions.
- The `name` parameter is no longer required, and is ignored for `Vector.replace_product`, `Vector.update_product`, `FeatureCollection.update` and `FeatureCollection.replace`.  This parameter will be removed completely in future versions.

### Added
- `Metadata.paged_search` has been added and essentially supports the original behavior of `Metadata.search` prior to release 0.16.0.
This method should generally be avoided in favor of `Metadata.features` (or `Metadata.search`).

## [0.17.1] - 2019-02-11
### Added

### Changed
- Fixed typo in `UploadTask.status` which caused exception when handling certain failure conditions
- `FeatureCollection.upload` parameter `max_errors` was not being passed to Vector client.
- Ensure `cloudpickle==0.4.0` is version used when creating `Tasks`.
- Eliminate redundant queries from `FeatureCollection.list`.

## [0.17.0] - 2019-02-07
### Added
- `FeatureCollection.upload` and `Vector.upload_features` now accept an optional `max_errors` parameter to control how many errors are acceptable before declaring an upload a failure.
- `UploadTask` (as returned by `FeatureCollection.upload` and `Vector.list_uploads`) now has added attributes to better identify what was processed and what errors occurred.
- `Storage` now has added methods `set_file` and `get_file` to allow for better uploading and downloading, respectively, of large files.
- `Storage` class now has an `exists()` method that checks whether an object exists in storage at the location of a given `key` and returns a boolean.
- `Scenes.search` allows `limit=None`
- `FeatureCollection.delete_features` added to support deleting `Feature`s that match a `filter`
- `FeatureCollection.delete_features` and `FeatureCollection.wait_for_copy` now use `AsyncJob` to poll for asynchronous job completion.
- `Vector.delete_features_from_query` and `Vector.get_delete_features_status` added to support new `FeatureCollection` and `AsyncJob` methods.

### Changed
- Fixed tasks bugs when including modules with relative paths in `sys.path`

## [0.16.0] - 2019-01-28
### Added
- Tasks now support passing modules, data and requirements along with the function code, allowing for a more complex and customized execution environment.
- Vector search query results now report their total number of results by means of the standard `len()` function.

### Changed
- `Metadata.search` no longer has a 10,000-item limit, and the number of items returned will be closer to `limit`. This
method no longer accepts the `continuation_token` parameter.

## [0.15.0] - 2019-01-09
### Added
- Raster client can now handle arbitrarily large numbers of tiles generated from a shape using the new `iter_dltiles_from_shape()` method which allows you to iterate over large numbers of tiles in a time- and memory-efficient manner. Similarly the existing `dltiles_from_shape()` method can now handle arbitrarily large numbers of tiles although it can be very slow.
- Vector client `upload_features()` can now upload contents of a stream (e.g. `io.IOBase` derivative such as `io.StringIO`) as well as the contents of a named file.
- Vector FeatureCollection `add()` method can now handle an arbitrary number of Features. Use of the `upload_features()` method is still encouraged for large collections.
- Vector client now supports creating a new product from the results of a query against an existing product with the `create_product_from_query()` method. This support is also accessible via the new `FeatureCollection.copy()` method.
- XYZTile GeoContext class, helpful for rendering to web maps that use XYZ-style tiles in a spherical Mercator CRS.

### Changed
- Tasks client FutureTask now instantiates a client if none provided (the default).
- Catalog client methods now properly handle `add_namespace` parameter.
- Vector Feature now includes valid geojson type 'Feature'.
- Tasks client now raises new GroupTerminalException if a task group stops accepting tasks.
- General documentation fixes.

## [0.14.1] - 2018-11-26
### Added
- Scenes and raster clients have a `processing_level` parameter that can be used to turn on surface reflectance processing for products that support it

## [0.14.0] - 2018-11-07
### Changed
- `scenes.GeoContext`: better defaults and `bounds_crs` parameter
  - `bounds` are no longer limited to WGS84, but can be expressed in any `bounds_crs`
  - New `Scene.default_ctx` uses a Scene's `geotrans` to more accurately determine a `GeoContext` that will result in no warping of the original data, better handling sinusoidal and other non-rectilinear coordinate reference systems.
  - **Important:** the default GeoContexts will now return differently-sized rasters than before!
    They will now be more accurate to the original, unwarped data, but if you were relying on the old defaults, you should now explicitly set the `bounds` to `geometry.bounds`,
    `bounds_crs` to `"EPSG:4326"`, and `align_pixels` to True.
- `Scene.coverage` and `SceneCollection.filter_coverage` accept any geometry-like object, not just a `GeoContext`.

## [0.13.2] - 2018-11-06
### Changed
- `FutureTask` inheritance changed from `dict` to `object`.

### Added
- Can now specify a GPU parameter for tasks.
- `Vectors.upload` allows you to upload a JSON newline delimited file.
- `Vectors.list_uploads` allows you to list all uploads for a vector product.
- `UploadTask` contains the information about an upload and is returned by both methods.

## [0.13.1] - 2018-10-16
### Changed
- `Vector.list_products` and `Vector.search_features` get `query_limit` and `page_size` parameters.

### Fixed
- `Vector.upload_features` handles new response format.

### Added
- Vector client support for retrieving status information about upload jobs. Added methods `Vector.get_upload_results` and `Vector.get_upload_result`.

## [0.13.0] - 2018-10-05
### Changed
- Shapely is now a full requirement of this package. Note: Windows users should visit https://docs.descarteslabs.com/installation.html#windows-users for installation guidance.
- Reduced the number of retries for some failure types.
- Resolved intermittent `SceneCollection.stack` bug that manifested as `AttributeError: 'NoneType' object has no attribute 'coords'` due to Shapely thread-unsafety.
- Tracking system environment to improve installation and support of different systems.

### Added
- The vector service is now part of the public package. See `descarteslabs.vectors` and `descarteslabs.client.services.vector`.


## [0.12.0] - 2018-09-12
### Changed
- Fixed SSL problems when copying clients to forked processes or sharing them among threads
- Removed extra keyword arguments from places client
- Added deprecation warnings for parameters that have been renamed in the Metadata client
- Scenes now exposes more parameters from raster and metadata
- Scenes `descarteslabs.scenes.search` will take a python datetime object in addition to a string
- Scenes will now allow Feature and FeatureCollection in addition to GeoJSON geometry types
- Fixed Scenes issue preventing access to products with multi-byte data but single-byte alpha bands

### Added
- `Scene.download`, `SceneCollection.download`, and `SceneCollection.download_mosaic` methods
- Colormaps supported in `descarteslabs.scenes.display`
- Task namespaces are automatically created with the first task group


## [0.11.2] - 2018-08-24
### Changed
- Moved metadata property filtering to common
- Deprecated `create_or_get_function` in tasks
- Renamed some examples

## [0.11.1] - 2018-08-17
### Added
- Namespaced auth environment variables: `DESCARTESLABS_CLIENT_SECRET` and `DESCARTESLABS_CLIENT_ID`. `CLIENT_SECRET` and `CLIENT_ID` will continue to work.
- Tasks runtime check for Python version.

### Changed
- Documentation updates
- Example updates

## [0.11.0] - 2018-07-12
### Added
- Scenes package
- More examples

### Changed
- Deprecated `add_namespace` argument in catalog client (defaults to `False`
  now, formerly `True`)

## [0.10.1] - 2018-05-30
### Changed
- Added org to token scope
- Removed deprecated key usage

## [0.10.0] - 2018-05-17
### Added
- Tasks service

## [0.9.1] - 2018-05-17
### Changed
- Patched bug in catalog service for py3

## [0.9.0] - 2018-05-11
### Added
- Catalog service
- Storage service

## [0.8.1] - 2018-05-03
### Changed
- Switched to `start_datetime` argument pattern instead of `start_date`
- Fixed minor regression with `descarteslabs.ext` clients
- Deprecated token param for `Service` class

### Added
- Raster stack method

## [0.8.0] - 2018-03-29
### Changed
- Removed deprecated searching by `const_id`
- Removed deprecated raster band methods
- Deprecated `sat_id` parameter for metadata searches
- Changed documentation from readthedocs to https://docs.descarteslabs.com

### Added
- Dot notation access to dictionaries returned by services

## [0.7.0] - 2018-01-24
### Changed
- Reorganization into a client submodule

## [0.6.2] - 2018-01-10
### Changed
- Fix regression for `NotFoundError`

## [0.6.1] - 2018-01-09
### Changed
- Reverted `descarteslabs.services.base` to `descarteslabs.services.service`

## [0.6.0] - 2018-01-08
### Changed
- Reorganization of services
- Places updated to v2 backend, provides units interface to statistics, which
  carries some backwards incompatibility.

### Added
- Places updated to v2 backend, provides units interface to statistics, which
  carries some backwards incompatibility.

## [0.5.0] - 2017-10-31
### Added
- Blosc Support for raster array compression transport
- Scrolling support for large metadata searches

### Changes
- Offset keyword argument in metadata.search is deprecated. Please use the
metadata.features for iterating over large search results

## [0.4.7] - 2017-10-09
### Added
- Complex filtering expressions for image attributes

### Fixes
- Raise explicitly on 409 response
- Keep retrying token refresh until token fully expired
- Fixed race condition when creating `.descarteslabs` directory

## [0.4.6] - 2017-09-08
### Added
- Added ext namespace
- Metadata multi-get

### Fixes
- Fix OpenSSL install on OSX

## [0.4.5] - 2017-08-29
### Fixes
- Automatic retry on 504
- Internal API refactoring / improvements for Auth

## [0.4.4] - 2017-08-03
### Added
- Add raster bands methods to metadata service.
- Deprecate raster band methods.
- Add `require_bands` param to derived bands search method.

### Fixes
- Test suite replaces original token when finished running script tests.

## [0.4.3] - 2017-07-18
### Added
- Support for derived bands endpoints.
- Direct access to `const_id` to `product` translation.

### Fixes
- `descarteslabs` scripts on windows OS.

## [0.4.2] - 2017-07-05
### Fixes
- Fix auth login

## [0.4.1] - 2017-07-05
### Added
- Add metadata.bands and metadata.products search/get capabilities.
- Add bands/products descriptions
- Additional Placetypes

### Fixes
- Better error messages with timeouts
- Update to latest version of `requests`

## [0.4.0] - 2017-06-22
### Changes
- Major refactor of metadata.search
  * Introduction of "Products" through `Metadata.products()`
  * metadata entries id now concatenate the product id and the old metadata
    keys. The original metadata keys are available through entry['key'].
  * Additional sorting available.

### Added
- Search & Raster using DLTile Feature GeoJSON or key. Uses output bounds,
  resolution, and srs to ease searching and rasterizing imagery over tiles.

### Fixes
- Better Error messaging

## [0.3.3] - 2017-06-20
### Added
- DLTile notebook
- `save` and `outfile_basename` in `Raster.raster()`

### Fixes
- Fix metadata.features


## [0.3.2] - 2017-05-27
### Fixes
- Strict "requests" versions needed due to upstream instability.


## [0.3.1] - 2017-05-17
### Fixes
- Fix python 3 command line compatibility


## [0.3.0] - 2017-05-15
### Changed
- API Change `descarteslabs`, `raster`, `metadata` have all been merged into
 '`descarteslabs`'. '`descarteslabs login`' is now '`descarteslabs auth
 login`', '`raster`'' is now '`descarteslabs raster`', etc.

### Added
- A Changelog
- Testing around command-line scripts

### Fixes
- Searching with cloud\_fraction = 0
- dltile API documentation

## [0.2.2] - 2017-05-04
### Fixes
- Fix login bug
- Installation of "requests\[security\]" for python < 2.7.9

## [0.2.1] - 2017-04-18
### Added
- Doctests

### Fixes
- Python 3 login bug

## [0.2.0] - 2017-04-11
### Added
- Search by Fractions

## [0.1.0] - 2017-03-24
### Added
- Initial release of client library
