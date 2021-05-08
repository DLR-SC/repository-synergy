This repository contains three python files for creating time maps and downloading tweets. The python files require a few packages. See below for details. To download tweets, you will need to set up your own Twitter account and paste the credentials into the top of tm_tools.py.

Post cool time maps to Twitter!  #time_map_viz

Here is a description of each file:

heated_time_map_howto.py — this creates a heated time map using randomly generated points. It only requires numpy and scipy to run. 

tweet_timemap.py — this file, along with tm_tools.py, downloads tweets and creates a corresponding time map. Within tweet_timemap.py, you specify the user account whose tweets you wish to download, and whether you want a heated time map or a normal time map (scatter plot). When the program is executed, an .eps file will be created containing the plot. The file's name is the user name whose tweets you downloaded. 

tm_tools.py — contains the functions required to actually build the time map and grab the tweets. It requires the following packages: numpy, scipy, matplotlib, twython and colour. You will also need to paste your twitter credentials near top of this file. You’ll see where.

For a quick read on time maps, check out 
[District Data Labs] (https://districtdatalabs.silvrback.com/time-maps-visualizing-discrete-events-across-many-timescales).

I also wrote a longer [article] (http://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=7363824) with more in-depth examples and connections to probability.
