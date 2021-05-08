## Lynda.com Video Downloader
This Lynda.com Video Downloader written with Python 3 will help you download all specified course videos in separate folders. You need to be an existing Lynda.com user in order to use it.

### Dependencies
Script uses [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [youtube-dl](https://github.com/rg3/youtube-dl). You can install them with commands:

```sudo pip3 install youtube-dl```

```sudo pip3 install beautifulsoup4```

For more info on installation visit their respective web pages.


### Usage
1. Add your credentials (Lynda.com username and password) to settings in download.py
2. Add course URLs in links.txt (first remove sample URLs)
3. Go to file directory where `download.py` and `links.txt` are saved and run `download.py` from the terminal with:
```python download.py```
or
```python3 download.py```
4. Wait until all videos are downloaded and have fun watching them.

### Extra
#### Subtitles
By default the subtitles are downloaded. If you wish to download videos without subtitles replace `SUBTITLES = True` with `SUBTITLES = False`

#### Downloader
Default downloader is aria2c. If you wish to change it edit `EXTERNAL_DL = 'aria2c'`

#### Archive
By default ids of all downloaded videos will be placed in `archive.txt`. To disable archive comment it out from the options. Example:`#'download_archive' : ARCHIVE,`.
