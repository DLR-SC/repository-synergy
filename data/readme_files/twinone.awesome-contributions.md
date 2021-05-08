# awesome-contributions
Make your GitHub's contributions viewer awesome!

With this simple python script you can make your contributions viewer look however you want:

![screenshot from 2016-05-17 14 17 44](https://cloud.githubusercontent.com/assets/4309591/15321965/289f589c-1c3a-11e6-8551-40cb74521617.png)

You can use any image, it will be grayscaled and converted to commits for you:

![screenshot from 2016-05-17 12 40 33](https://cloud.githubusercontent.com/assets/4309591/15320322/2a2834cc-1c30-11e6-8cc3-dbacc9451757.png)

# Requirements

If you don't have pip, `apt-get install python-pip`

The script uses the Python Image Library (PIL)
```
pip install pillow
```

# Usage (Image)

* Clone **this repository** [it doesn't work on forks](https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile/):
<pre>
git clone https://github.com/twinone/awesome-contributions
cd awesome-contributions
</pre>
* Create a new empty github repository yourself on github, called `awesome-contributions`
* Add your repository as a remote:
<pre>
git remote add github https://github.com/<b>[YourUser]</b>/awesome-contributions
</pre>

* Replace the test.png image by the 52x7 image you want as background (can be other formats too)

* Run the generator:

```
# In the awesome-contributions directory:
python gen.py test.png
```
* Push the changes to **your** GitHub repository:
```
git push github master
```

# Usage (Text)
You can also generate an image containing whatever text you want:
```
python gen.py --text "AWESOME"
```
Will generate AWESOME.bmp for you:

![screenshot from 2016-05-18 22 43 41](https://cloud.githubusercontent.com/assets/4309591/15374320/fadf26ec-1d49-11e6-82c6-72dc8d6183f1.png)

Then you just run the program the normal way:
```
python gen.py AWESOME.bmp
```
## Important

Sometimes some commits don't make it into the contributions page, in this case you create another repository (for example called `awesome`) and follow this steps:
```
# Go to the cloned repository
cd awesome-contributions

# Add the second repository as a remote
git remote add helper https://github.com/[YourUser]/awesome

# Push the same commits there too...
git push helper master
```

This will make GitHub refresh the commits correctly. If you refresh your profile page and see the commits are there, you can delete this helper repository again, and the commits from the original (forked) repository will stay visible.

# Notes
* Each week the image will be shifted to the left, so if you leave some padding you can update once every two months or so.
* Make sure to leave at least a few weeks of space at the right so you don't spam the people who follow you.
