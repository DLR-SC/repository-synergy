# NOTE: This auto buyer is no longer being actively maintained in favor of my [other project](https://github.com/hunterjm/fifa-autobuyer/releases).

# Releases
Download pre-built releases on the [releases](https://github.com/hunterjm/futgui/releases) page.

## Contributors
[Jason Hunter](https://github.com/hunterjm) - Core Development

[Piotr Staroszczyk](https://github.com/oczkers) & others - FUT API Library

[Fabiano Francesconi](https://github.com/elbryan)

### Requirements
This has only been tested and built with Python 3.5.
```
pip install -r requirements.txt
```

### Build (Mac):
```
make macbundle
```

### Build (Windows):
Make sure to delete `build` and `dist` folders before re-building.
```
pyinstaller '.\FIFA 17 Auto Buyer.spec'
```
