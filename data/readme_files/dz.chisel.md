# Chisel

Chisel is a simple python static blog generation utility by [David Zhou][dz].

## Usage

```bash
$ python3 chisel.py
```

## Sample entry

`sample.markdown`:

```markdown
Title
3/2/2009

This is now the body of the post.  By default, the body is evaluated and parsed with markdown.

Another line.
```

Entry format is described as follows:

- Line 1: Enter a title
- Line 2: Enter date in m/d/Y
- Line 3: Blank line
- Line 4: Content in Markdown here onward

## Adding Steps

Use the `@step` decorator. The main loop passes in the master file list and [jinja2][j2] environment.

## Settings

Change these settings:

- `SOURCE`: Location of source files for entries (must end with a `/`), e.g., `SOURCE = "./blog/"`
- `DESTINATION`: Location to place generated files (must end with a `/`), e.g., `DESTINATION = "./explort/"`
- `HOME_SHOW`: Number of entries to show on homepage, e.g., `HOME_SHOW = 15`
- `TEMPLATE_PATH`: Path to folder where tempaltes live (must end with a `/`), e.g., `TEMPLATE_PATH = "./templates/"`
- `TEMPLATE_OPTIONS`: Dictionary of options to give jinja2, e.g., `TEMPLATE_OPTIONS = {}`
- `TEMPLATES`: Dictionary of templates (required keys: 'home', 'detail', 'archive'), e.g.,
    ```python
    TEMPLATES = {
        'home': "home.html",
        'detail': "detail.html",
        'archive': "archive.html",
    }
    ```
- `TIME_FORMAT`: Format of human readable time stamp. Default: `"%B %d, %Y - %I:%M %p"`
- `ENTRY_TIME_FORMAT`: Format of date declaration in second line of posts. Default: `"%m/%d/%Y"`
- `FORMAT`: Callable that takes in text and returns formatted text. Default: `FORMAT = lambda text: markdown.markdown(text, extensions=['markdown.extensions.footnotes'])` 

[dz]: https://github.com/dz/chisel
[j2]: https://jinja.palletsprojects.com/en/
