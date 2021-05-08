About
====

Current Version: v2.1

Pomash is a lightweight blog system. Powered by Tornado Web Framework.

Build up
====

Note: The Python environment has been updated to 3.7.1. So I am not sure whether Pomash works properly under the 2.x version of Python.

How to get Pomash:

```shell
git clone https://github.com/JmPotato/Pomash.git
cd Pomash
pip install -r requirements.txt
```
You should edit the `settings.py` to set up before running `run.py`. Here is a explanation for `settings.py`:

* `blog_name` Your blog's name.
* `blog_author` Your name.
* `blog_url` Your blog's URL.
* `theme` The theme you're using.
* `dark_mode` The switch for dark mode. 0.Off & 1.On & 2.Auto. PS: Need theme support.
* `pygments_style_light` The pygments style for light mode.
* `pygments_style_dark` The pygments style for dark mode.
* `post_per_page` The number of articles you want to display on the home page.
* `twitter_card` Enable/Disable the twitter card function.
* `twitter_username` Your twitter username.
* `analytics` Google Analytics code. If you don't know what it is, just leave it empty.
* `comment_system` Pomash currently supports Disqus or Valine as the comment system. `0` means turn off the comment. `1` means using Disqus. `2` means using Valine.
* `disqus_name` If you choose Disqus as your comment system, please fill this with your own code.
* `valine_app_id/key` If you choose Valine as your comment system, please fill this with your own LeanCloud app id/key. You can look [this](https://valine.js.org/quickstart.html#%E8%8E%B7%E5%8F%96APP-ID-%E5%92%8C-APP-Key) as a reference.
* `dropbox_app_token` If you want to use the backup function, get a Dropbox app token [here](https://www.dropbox.com/developers/apps/create) first.
* `cookie_secret` The string used to encrypt your cookie. ***PLEASE CHANGE THIS TO YOUR OWN STRING.***
* `login_username` The admin username. Initial password of admin is `admin`. Please change it as soon as possible.
* `DeBug` Developer setting. Normal user could just ignore it.

After customizing `settings.py` and initialize the database, you could put Pomash online.

```shell
python init_db.py
python run.py --port=8080
```

Usage
====

Pomash uses Markdown to write posts and pages. LaTeX is also supported.

Note: To avoid conflict between LaTeX and Markdown, Pomash removed the emphasis syntax `*word*` and `_word_` which you should use `<em>word</em>` as an alternative.

    #Hello World

    ```python
    print('Hello, World!')
    ```
    
    Hello, World!

    Inline LaTeX: $\int_a^b f(x)\mathrm{d}x$

    New line LaTeX: $$\sum_{i=0}^{n}i^2$$
    
    <em>This is a emphasis.</em>
    
    **This is a double emphasis.**

    * Hello
    * World

Theme
====

Pomash's theme is called Potheme. Here is a Potheme list:

* [Potheme-Clean](https://github.com/JmPotato/Pomash/tree/master/Pomash/theme/clean)
* [Potheme-Maupassant](https://github.com/JmPotato/Potheme-Maupassant)
* [Potheme-Default](https://github.com/JmPotato/Potheme-Default)

Other Reference
====

A [Chinese guide](https://ipotato.me/article/16) for setting up.(Maybe a little outdated)

License
====

Please read the [MIT-LICENSE](./LICENSE)


