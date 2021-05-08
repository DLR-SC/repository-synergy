# Find++

Find code quickly in [Sublime Text][subl].

This was built to allow quick shuffling between search directories. It is useful for projects using multiple repositories to isolate noise in search results.

[subl]: http://www.sublimetext.com/

- `Find: In Current File` - Opens `Find in Files` with `Where` as the current file
- `Find: In Current Folder` - Opens `Find in Files` with `Where` as the folder of the current file
- `Find: In Open Files` - Opens `Find in Files` with `Where` as `<open files>`
- `Find: In Project` - Opens `Find in Files` with `Where` as `<open files>,<open folders>`
- `Find: In...` - Shows panel to pick directory to open `Find in Files` with as its `Where`
- `Find: Show Results Panel` - Reveals the `Find Results` panel

![Find in Files example](https://f.cloud.github.com/assets/902488/860977/39331c12-f5c2-11e2-9de7-9769e885d111.png)

## Installation
`Find++` is available via [Package Control][pkg-ctrl] and can be found as `Find++`.

[pkg-ctrl]: http://wbond.net/sublime_packages/package_control

For manual installation, run the following script in the Sublime Text terminal (``ctrl+` ``) which utilizes `git clone`.

```python
import os; path=sublime.packages_path(); (os.makedirs(path) if not os.path.exists(path) else None); window.run_command('exec', {'cmd': ['git', 'clone', 'https://github.com/twolfson/FindPlusPlus', 'Find++'], 'working_dir': path})
```

Packages can be uninstalled via `Package Control: Remove Package`, located in the Command Palette.

## Documentation
All commands are accessible via the Command Palette, `Ctrl + Shift + P` on Windows/Linux, `Command + Shift + P` on Mac.

![Find Palette](https://f.cloud.github.com/assets/902488/279674/a552365a-9134-11e2-8c89-603fbb89b606.png)

The `Find: In...` command opens a quick panel with relevant paths and the ability to filter.

![Find in current file panel](https://f.cloud.github.com/assets/902488/860987/ba97f2b4-f5c2-11e2-9b8d-c53060cd0f59.png)

When you search, the normal `Find in Files` search will be executed with one modification. The `Delete` and `Backspace` key will delete an entire row rather than a single character.

![Find in files results](https://f.cloud.github.com/assets/902488/279676/acdae412-9134-11e2-9c3d-10cdaaa6daff.png)

## Donating
Support this project and [others by twolfson][twolfson-projects] via [donations][twolfson-support-me].

<http://twolfson.com/support-me>

[twolfson-projects]: http://twolfson.com/projects
[twolfson-support-me]: http://twolfson.com/support-me

## Inspiration
As the name of this project suggests, this plugin was started to gain the same `Find` functionality of [Notepad++][npp].

[npp]: http://notepad-plus-plus.org/

## License
Copyright (c) 2013 Todd Wolfson

Licensed under the MIT license.
