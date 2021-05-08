EZTV API
========

This is the (unofficial) Python API for EZTV.it

Using this code, you can manage to get the information regarding any TV Show which is listed on EZTV.it
See how to use it thanks to the file "APIExample.py". 

### Installation

To use this API, you need BeautifulSoup installed. <br />
Then, you can start using the EZTV API.

### Usage

Start by importing the API file 
```
from eztv_api import EztvAPI
```

Then, you can search for a specific TV Show

```
test_api = EztvAPI().tv_show('Game Of Thrones')
```

The search is not case sensitive so : 
"_Game Of Thrones_" equals "_GaMe oF ThRoNeS_" equals "_game of thrones_" ...

## Iterate on all the seasons : 

```python
# get all the seasons from Game Of Thrones
seasons = test_api.seasons()
for season in seasons:
    for episode in seasons[season]:
        # will print the magnet link of all episodes, in all seasons
        print seasons[season][episode]
```

## Iterate on a specific season
```python
# specific season
episodes = test_api.season(3)
for episode in episodes:
    # will print the magnet link for all episodes
    print episodes[episode]
```

## Get a specific episode
```python
# specific episode
print test_api.episode(3, 10)
```

### Conclusion (& License)
Feel free to give feedbacks and ask for new features.  

API released under license GLPv3. 
