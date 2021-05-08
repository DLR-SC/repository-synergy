# Captivox

![Captivox heading example gif](captivox.gif)

make a whole lot of cool dot animations using the Power of Parametric™ Maths™ Equations

I want to try!
-----
Just run `pip install --user PyQt5` and then `python3 captivox.py`.

Optionally, run `pip install --user imageio` and ensure you have `ffmpeg` on your computer if you want to export videos. To install both in one command, use `pip install --user -r requirements.txt`.

Oh, and be sure to use pip for python3, not python2. This project is python3 only. This might mean using `pip3` instead of `pip`.

PS: if you need ffmpeg on a non-linux system, you may want to take a look at https://imageio.readthedocs.io/en/latest/format_ffmpeg.html as there are some imageio-specific ffmpeg installation methods.

What does it look like?
-----

[Here are some exported animations from it](https://imgur.com/a/WJXby), [and here is a more updated screencast of Captivox in use.](https://gfycat.com/ScentedDefiantAsianpiedstarling)

Can I contribute?
-----

the code is in `captivox.py`, you're welcome to make pull requests. I know I'm not the best designer in the world so I would especially welcome improvements in that area.

Final notes
-----

When exporting video, beware that the result will look a lot faster than it does when you're playing around with it. This is because when displaying live, there is an extra delay to actually render each frame before it is shown, but in the video the frames are all pre-rendered and thus it appears much faster. You may want to increase 'delay' to compensate.

Also, reduced period values will reduce video length and hence filesize. A trick to getting nice output with small period values is to increase the X and Y multipliers - if multiplier * period is a nice significant number, and especially if it is 180, you can avoid the sometimes-annoying bounce.

Also, if you **really** want a GIF instead of an mp4, despite the larger filesize and worse quality, you can use `ffmpeg` to convert it (some variant of `ffmpeg -i captivox.mp4 out.gif`).
