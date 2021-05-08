# Do for Vim

## Run asynchronous shell commands and display the output

![animation showing vim-do in action](http://www.mediafire.com/convkey/7734/1o4gb6rpgde2ycy9g.jpg?size_id=5)

The aim of this plugin is to provide a quick and simple way of running shell commands in the background, and displaying the results (output, exit status, etc) in a Vim buffer as the process is running. That means you can run several commands, carry on working in Vim, and swap between the processes at will or just keep them running hidden in the background.

It works nicely for both short- and long-running processes, and the great thing is that you don't have to swap between a terminal and Vim to run commands or see their output.

## Features

After installing (see below) you're given the `:Do` vim command, which allows you to run any shell command:

```vim
:Do echo "hi"
:Do rake
:Do find /
```

Oops, that last command is gonna take a while...

But don't worry, it's asynchronous! A new buffer will pop up while it's running and show the output. If you close it, it will keep running until the command finishes naturally. You can run as many commands at the same time as your computer can handle.

### Overview of all commands

```vim
" Execute a command in the background
:Do <command>

" Execute a command in the background without opening the process output window
:DoQuietly <command>

" Show all processes (running and finished)
:Doing

" Alias for :Doing
:Done

" Execute the command under visual selection
:'<,'>DoThis
```

### View running/finished processes and swap between them

You can see running and finished processes with the `:Doing` or `:Done` commands (different names for the same thing). It looks something like this:

![the command window](http://www.mediafire.com/convkey/319f/plvj08c83s030qjzg.jpg)

Pressing `<CR>` (the `Enter` key) on a line will open the process window which gives more detail and shows the output (standard out and standard error).

### Automatically updating output

While a process is running and the process window is open, the output from the process will automatically be written to the buffer. This is achieved with a combination of python threads, io select and Vim's autocommands.

### Re-run the last command

After running any command, run it again with the command `:DoAgain`.

### Run a command without the process window popping up

Execute a command with the `:DoQuietly` vim command instead of `:Do`, and it won't open the process window. Alternatively, you can turn it off permanently by setting `g:do_auto_show_process_window = 0`.

You can still view information and output for a process by opening the command window (`:Doing` or `:Done`) and selecting the process.

### Replacement for :make

If you're used to running `:make` and using `set makeprg=some\ command`, then you can use `:Do` as a replacement. Running `:Do` without any arguments will automatically run whichever command has been set by `makeprg`.

```vim
:Do
" Runs make
:set makeprg=rake
:Do
" Runs rake
```

### Run the command under selection

If you want to run a command selected under the cursor (in visual select mode), you can use the command `:'<,'>DoThis`.

## Install

**Requires Vim compiled with Python 2.4+ support**

### Classic

Clone or download a tarball of the plugin and move its content in your
`~/.vim/` directory.

Your `~/.vim/plugin/` directory should now contain do.vim, and your `~/.vim/autoload` directory should contain do.vim and a directory
called "python".

### Using git and Pathogen

Clone this repository in your `~/.vim/bundle` directory

### Using vundle

Add this to your `~/.vimrc` file:

```vim
Bundle 'joonty/vim-do.git'
```

Then, from the command line, run:

```bash
vim +BundleInstall +qall
```

## Configuration

Here are the available configuration options:

* `g:check_interval`: vim-do checks running processes for output and exit codes, and this value sets how often it will allow these checks to be made, in milliseconds (default 1000).
* `g:do_new_buffer_command_prefix`: when a process starts, a new window will open with the default command `:new`. This prefix will be added before the `new`, so, for example, you can change it to a vertical split by setting this to "vertical".
* `g:do_new_buffer_size`: set the size of the process window, no default.
* `g:do_refresh_key`: this should be set to a key combination _that you don't want to use_, as it's used to trigger Vim's autocommands, but shouldn't actually do anything. By default it's set to `<C-B>` (Control-B), which may conflict with other plugins. If it does, change it to another key combination that you don't ever use.
* `g:do_update_time`: used to change vim's `updatetime` setting, which determines how quickly vim-do will check and update running processes after you stop typing any keys, in milliseconds (default 500).

If you change an option after vim-do has loaded you'll need to tell it to reload the options. You can do this with the function `do#ReloadOptions()`, i.e.:

```vim
:let g:do_auto_show_process_window = 0
:call do#ReloadOptions()
```

## How does it work?

Vim is single-threaded, which is obviously a big challenge in running commands asynchronously. However, Vim almost always comes with Python support, which is multithreaded. With some trickery, we can use Python's threading to run processes and get Vim to periodically check these threads for the process' state.

When you run a command with `:Do <command>`, a new Python thread is created to run the process and capture the standard output/error line-by-line. This thread will run until the process finishes.

The challenge with this is getting Vim to keep going back to these threads and check their output, and ultimately their exit status when they eventually finish. I used autocommands, particularly `CursorHold` and `CursorHoldI`. These are used to trigger a Vim command or function when the user stops typing (in normal and insert mode respectively). This is great - I can get Vim to check my process threads and give the appearance of this being done in a completely multithreaded way. But this command only gets triggered once.

So to get round this, after checking the process threads I also send a dummy keystroke, which is mapped to a command that does nothing. This tricks Vim into thinking that the user has typed something, and triggers the `CursorHold` or `CursorHoldI` autocommands again. That means even if you're not typing anything, there are circular, periodic checks of the process threads. These autocommands are cleared when all the process threads finish, so it doesn't keep running Vim functions periodically when not needed.

If you understood this, then yay. If not, who cares? You can still use vim-do without knowing any of it. I wrote it down so I wouldn't forget in 3 months (weeks) time.

## License

This is released under the MIT license.
