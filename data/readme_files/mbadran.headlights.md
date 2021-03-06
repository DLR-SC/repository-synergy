![Headlights in Action][2]

Headlights adds a `Bundles` [^1] menu to Vim, revealing your bundles (aka.
plugins) and the features they provide.

Headlights creates a menu for each currently loaded [^2] bundle, grouping
together docs, commands, mappings, abbreviations, functions, highlights, and
plugin files.

Combined with a powerful bundle manager, Headlights will improve your ~~Vim
user experience~~ quality of life.

## Get Headlights

__NOTE:__ Headlights requires Vim 7+ compiled with Python 2.6+ support.

#### The Recommended Way

Using [Vundle] [3]:

1. Add the following line to the Vundle section in your `.vimrc`:

    `Bundle 'mbadran/headlights'`

2. Run the following Vim command:

    `BundleInstall`

#### The Manual Way

1. [Download the latest package] [4].

2. Expand the archive's contents into your `vim` directory.

3. Run the following Vim command:

    `helptags <vim_dir>/<plugin_dir>/<headlights_dir>/doc/`

## Explore the Options

`let g:headlights_use_plugin_menu = 0` (Disabled)

`let g:headlights_smart_menus = 1` (Enabled)

`let g:headlights_show_commands = 1` (Enabled)

`let g:headlights_show_mappings = 1` (Enabled)

`let g:headlights_show_abbreviations = 0` (Disabled)

`let g:headlights_show_functions = 0` (Disabled)

`let g:headlights_show_highlights = 0` (Disabled)

`let g:headlights_show_files = 0` (Disabled)

`let g:headlights_show_load_order = 0` (Disabled)

`let g:headlights_debug_mode = 0` (Disabled)

`let g:headlights_run_on_startup = 0` (Disabled)

`let g:headlights_spillover_menus = 0` (Disabled)

## Go Deeper

Refer to the Headlights help document:

`Bundles > a - i > headlights > Help`

`:help headlights`

#### Protip

If you use MacVim, you can quickly access any plugin by typing its name. For
example, hit `CMD-?` to bring up a search dialog for menu items, then type `fug
open` to reveal the `fugitive.vim` file as the first result. You can also type
`fug help` to quickly access the documentation. I do this, like, _all the time_.

* * *

[^1]: Headlights is inspired by TextMate's Bundles menu.

[^2]: Headlights mirrors Vim's `scriptnames` command, revealing only the
      bundles that are currently loaded. This is fast because it avoids file
      system access, but the trade off is that autoload and ftplugin scripts
      are not revealed until they are needed. (This is Good Enough ???.)

[1]: http://www.vim.org/

[2]: https://github.com/mbadran/headlights/raw/master/headlights_ss.png

[3]: https://github.com/gmarik/vundle

[4]: https://github.com/mbadran/headlights/downloads
