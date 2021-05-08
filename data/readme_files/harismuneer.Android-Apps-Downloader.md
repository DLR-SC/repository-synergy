# 📱 Android Apps Scraper/Downloader
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2537131.svg)](https://doi.org/10.5281/zenodo.2537131)

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](#)
[![GitHub Forks](https://img.shields.io/github/forks/harismuneer/Android-Apps-Downloader.svg?style=social&label=Fork&maxAge=2592000)](https://www.github.com/harismuneer/Android-Apps-Downloader/fork)
[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/Android-Apps-Downloader.svg?style=flat&label=Issues&maxAge=2592000)](https://www.github.com/harismuneer/Android-Apps-Downloader/issues)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat&label=Contributions&colorA=red&colorB=black	)](#)




I did a research project on comparison of Official Play Store Apps and their 3rd Party App Stores counterparts to analyze what modifications are done to the 3rd Party versions of an app. For this purpose, I wrote this script to download pairs of an app from Google Play Store and Xiaomi App Store (a famous 3rd Party Chinese App Store). It downloads an app from Xiaomi and Google Play store only when that app is available on both stores. This way it creates a dataset of pairs of an app.

I am open-sourcing this tool so that it can be utilized by the research community for research in Android Security. 

Moroever, to compare two Android Apps I wrote another tool named [AndroCompare](https://github.com/harismuneer/AndroCompare). I have open-sourced it as well.

For details regarding **citing/referencing** this tool for your research, check the 'Citation' section below.


## Approach
The download URL of an app on Xiaomi App Store is like http://app.mi.com/download/23 
The number at the end of the URL can be incremented to download as many apps as you want. So, theoretically you can download each and every app on the Xiaomi App Store. Hence there's a variable named 'target' in the tool. If target = 1000 then the tool will scan first 1000 urls for the apps. You can change the target to any number you want.


## Features
* download all apps from the famous Xiaomi App Store
* download pairs of an app from Play Store and Xiaomi App Store
* the record of all downloaded apps is maintained in a SQLite database
* if the code is interrupted using CTRL + Z then the current progress is saved so that next time the code resumes downloading from where it left previously
* incase the script is running and there occurs some internet connectivity issue then all current progress is saved and the script waits until the internet is connected again and resumes from where it left

## How to Run Code
The code is in ready to run condition. It can be run on both Windows/Ubuntu Linux. 
Its written in Python 3. Moreover it uses [gplaycli](https://github.com/matlink/gplaycli), so install it using pip.

You can use [DB Browser for SQLite](http://sqlitebrowser.org/) to view the database.

----------------------------------------------------------------------------------------------------------------------------------------
## Note
This script can be easily modified to meet your specific needs e.g currently it first checks whether an app is present on both stores and if yes then it downloads it from each store. You can remove this constraint to download every possible app from Xiaomi App Store.

This code is for research purposes only.

----------------------------------------------------------------------------------------------------------------------------------------

## Citation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2537131.svg)](https://doi.org/10.5281/zenodo.2537131)

If you use this tool for your research, then kindly cite it. Click the above badge for more information regarding the complete citation for this tool and diffferent citation formats like IEEE, APA etc.

---------------------------------------------------------------------------------------------------------------------------------------

## Author
You can get in touch with me on my LinkedIn Profile: [![LinkedIn Link](https://img.shields.io/badge/Connect-harismuneer-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect
)](https://www.linkedin.com/in/harismuneer)

You can also follow my GitHub Profile to stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-harismuneer-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/harismuneer)

If you liked the repo then kindly support it by giving it a star ⭐!

## Contributions Welcome
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](#)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.

## Issues
[![GitHub Issues](https://img.shields.io/github/issues/harismuneer/Android-Apps-Downloader.svg?style=flat&label=Issues&maxAge=2592000)](https://www.github.com/harismuneer/Android-Apps-Downloader/issues)

If you face any issue, you can create a new issue in the Issues Tab and I will be glad to help you out.

## License
[![MIT](https://img.shields.io/cocoapods/l/AFNetworking.svg?style=style&label=License&maxAge=2592000)](../master/LICENSE)

Copyright (c) 2018-present, harismuneer                                                        


