# Bash completion with Python

## A bit of background

When I first learned of tab-completion in Bash, on my first day in a programming job, I was elated. It was absolutely wonderful to have my terminal act like an IDE and save me huge amounts of time on typing paths and parameters.

What was not wonderful however, was when I wanted to make my own custom completion functions. Most people write completion specifications ("comp specs") as bash functions and add them via `complete -F function`. There is good reason for this; `/usr/share/bash-completion/` contains hundreds of examples in bash to work with, and it's easy to define a completion function next to the function it's made for.

There is a little-used variant however: `complete -C command`. This lets you just run an arbitrary program and use its stdout to generate completions. I don't mean to bash bash, but if you want write a completion in a language that's more readable, popular, and comes with a ton of functionality baked into its standard library, this option is a godsend. The lack of examples doesn't help matters much, though. Seriously, just [try googling it](https://www.google.com/search?q="complete+-C+command") or something similar.

Or you could just read on.

## The answer

[Here's the manual entry](https://www.gnu.org/software/bash/manual/html_node/Programmable-Completion.html):

> When the command or function is invoked, the COMP_LINE, COMP_POINT, COMP_KEY, and COMP_TYPE variables are assigned values as described above (see Bash Variables). If a shell function is being invoked, the COMP_WORDS and COMP_CWORD variables are also set. When the function or command is invoked, the first argument ($1) vis the name of the command whose arguments are being completed, the second argument ($2) is the word being completed, and the third argument ($3) is the word preceding the word being completed on the current command line. No filtering of the generated completions against the word being completed is performed; the function or command has complete freedom in generating the matches.
> ...
> Next, any command specified with the -C option is invoked in an environment equivalent to command substitution. It should print a list of completions, one per line, to the standard output. Backslash may be used to escape a newline, if necessary. 

Summarized, you need to make a program that accepts three command-line arguments, (maybe four environment variables too), and prints stuff that matches one of the parameters to stdout. Easy enough. Here's the template in Python:

```python
#!/usr/bin/env python3
import sys

def foobar():
    return ["a", "bunch", "of", "potential", "matches"]


def completion_hook(cmd, curr_word, prev_word):
    potential_matches = foobar()
    matches = [k for k in potential_matches if k.startswith(curr_word)]
    return matches


def main():
    results = completion_hook(*sys.argv[1:])
    if len(results):
          print("\n".join(results))


if __name__ == "__main__":
    main()
```
And here's the demo:

```bash
$ chmod +x ./completion_example.py
$ complete -C ./completion_example.py heylook
$ heylook
a          bunch      matches    of         potential
```

It's that easy and comes with free alphabetization! I should note this is specifically for bash though. Zsh, fish, and whatever other shells are out there may have different ways of supporting non-shell-script completion. I highly encourage you to look into your shell's documentation on it and try to implement whatever fits your needs.

## The catch

While your eyes are lighting up with possibilities for easy completions in any language other than bash, I should mention there are a few gotchas that show up when you start writing complex completions:

- Your program is executed by `complete`, whenever you trigger tab completion. That means to test output for n different lines, you need to trigger tab completion n times as well. Manually.
- The fact that it's run by complete means you don't have direct control over the seven variables, so you can't just pass in the current command line and get the output you expect.
- `complete` is a bash builtin, so you can't call it via subprocess as you would a typical binary to inspect its output.
- The program used to generate completions needs to run with zero interaction (it'll just hang if it tries to read stdin. Blame complete for that.), and it lasts for only as long as it takes to compute the completions, so attaching to it with a debugger is... difficult.

For the most part, you can trial-and-error your way towards a robust completion script writing variables out to a file to inspect them. If you're like me, you feel like it'd be nice if there was a way you could simulate `complete` by calling it with the necessary parameters and environment variables programmatically... like so:

```python
#!/usr/bin/env python3
import shlex
import subprocess

def bash_complete(comp_line, comp_exe):
    """
    This is an approximation of how bash's complete function generates matches.
    ``comp_line`` Is the line assumed to be at the terminal.
    ``comp_exe`` is the path to an executable file that will generate matches.
    Returns the stdout of comp_exe after running with parameters normally
    supplied by complete.
    """
    cmd_line_args = shlex.split(comp_line)
    cmd = cmd_line_args[0]
    comp_point = str(len(comp_line))
    curr_word = ""
    prev_word = cmd
    if comp_line.endswith(" "):
        curr_word = ""
        prev_word = cmd_line_args[-1]
    else:
        curr_word = cmd_line_args[-1]
        prev_word = cmd_line_args[-2] if len(cmd_line_args) >= 2 else ""

    os.environ.update({"COMP_LINE": comp_line, "COMP_POINT": comp_point})
    finished_process = subprocess.run(
        [comp_exe, cmd, curr_word, prev_word],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    return finished_process.stdout.strip()
```

There's a lot going on here, and I commented the best I could.

[shlex](https://docs.python.org/3/library/shlex.html)'s `split` function will split the value of `comp_line` in nearly the same way that the shell would, and provide an array of the substrings that result. There's a reason I say "nearly" though. The next few lines involve setting the three values that would be passed as parameters by `complete`. For REASONS, `complete` may pass an empty string as the value of curr_word, but to shlex, that's just one less string in the list.

The rest is mostly self-explanatory. Extract variables from `comp_line`, set some environment variables, call [subprocess](https://docs.python.org/3/library/subprocess.html) to execute `comp_exe`, and return its output. With a version of complete that can be executed from within a program, that means we can control the input, observe the output, and write some unit tests for our completions.

## The rest of the owl

With those unit tests, I can just use `watch -n1 python3 -m unittest complete_up.py` to test whatever oddball situations I want to throw at the completion script all at once automatically in a separate window, and use test-driven-development to rapidly iterate on the completion hook itself.

So as a practical example, here's a script I made recently to be a replacement for typing `cd ../../..` or similar. I have an alias for `cd` I've named `up`. Because comp specs are specified by command, I can use `complete -C complete_up.py up` to make a completion for up that's different from what `cd` typically uses. In this case, instead of the current directories and whatever's in `$CDPATH`, I'm going to list the parent directory, its parents, and so on to the root.

In addition, I'm adding a little twist: For a path like `/mnt/c/Users/U/Userutils/foobar` (where you're currently in foobar), you can type `up U/` to get to `mnt/c/Users/U` and `up Us` to get suggested completions of "Users/" and "Userutils/". Note that the first case returns a full path, but the second returns parts of the path.

Without further ado:

```python
#!/usr/bin/env python3
import pathlib
import os
import unittest
import shlex
import sys


def bash_complete(comp_line, comp_exe):
    """
    This is an approximation of how bash's complete function generates matches.
    ``comp_line`` Is the line assumed to be at the terminal.
    ``comp_exe`` is the path to an executable file that will generate matches.
    Returns the stdout of comp_exe after running with parameters normally
    supplied by complete.
    """
    cmd_line_args = shlex.split(comp_line)
    cmd = cmd_line_args[0]
    comp_point = str(len(comp_line))
    curr_word = ""
    prev_word = cmd
    if comp_line.endswith(" "):
        curr_word = ""
        prev_word = cmd_line_args[-1]
    else:
        curr_word = cmd_line_args[-1]
        prev_word = cmd_line_args[-2] if len(cmd_line_args) >= 2 else ""

    os.environ.update({"COMP_LINE": comp_line, "COMP_POINT": comp_point})
    finished_process = subprocess.run(
        [comp_exe, cmd, curr_word, prev_word],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    return finished_process.stdout.strip()


class CompletionTestCase_up(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.exe = __file__
        self.path = "/mnt/c/Users/U/Userutils/foobar"

    @property
    def path(self):
        # Set an environment variable to contain the path and decouple the test
        # results from the current directory.
        return os.environ["COMPLETE_UP_TEST_DIRECTORY"]

    @path.setter
    def path(self, path):
        os.environ["COMPLETE_UP_TEST_DIRECTORY"] = path

    def assert_completion(self, comp_line, expected):
        """
        A custom assertion specifically to deal with bash completion for paths
        """
        with self.subTest(comp_line=comp_line, path=self.path):
            stdout = bash_complete(comp_line, self.exe)
            actual_list = repr(sorted(stdout.splitlines()))
            expected_list = repr(sorted(expected.splitlines()))
            err = f"\nExpected: {expected_list}\nActual: {actual_list}"
            assert actual_list == expected_list, err

    def test_blank(self):
        # Exact match should show EVERYTHING
        self.assert_completion("up ", "/\nc/\nmnt/\nU/\nUsers/\nUserutils/")

    def test_specifics_give_exact_path(self):
        # Exact match should give the path.
        self.assert_completion("up U/", "/mnt/c/Users/U")

    def test_ambiguity_gives_keys(self):
        # Ambiguous match should give keys that start with the input.
        self.assert_completion("up Us", "Users/\nUserutils/")

    def test_you_are_here_already(self):
        # The script shouldn't bother suggesting the current directory.
        self.assert_completion("up foobar", "")


def completion_hook(cmd, curr_word, prev_word):
    matches = []
    # If you set this evironment variable outside of the test case above that
    # does so, you deserve whatever happens to you.
    test_path = os.environ.get("COMPLETE_UP_TEST_DIRECTORY")
    curr_path = None
    if test_path:
        curr_path = pathlib.Path(test_path)
    else:
        curr_path = pathlib.Path().absolute()

    paths = list(curr_path.parents)

    comp_line = os.environ["COMP_LINE"]
    cmd_args = comp_line[len(cmd) + 1:]

    # Map path parts to parent paths, prioritizing things closer to the end as
    # keys.
    path_dict = {}
    for p in reversed(paths):
        # p.stem returns "" for a path of "/", so we use p.parts[-1] instead
        key = p.parts[-1]
        if not key.endswith("/"):
            key += "/"
        key = shlex.quote(key) if " " in key else key
        path_dict[key] = p

    matches = [s for s in path_dict.keys() if s.startswith(cmd_args)]

    # Return the path if it's been narrowed down.
    if len(matches) == 1:
        matches = [str(path_dict[matches[0]])]

    return matches


def main():
    results = completion_hook(*sys.argv[1:])
    if len(results):
        print("\n".join(results))


if __name__ == "__main__":
    main()
```

It's a lot to take in, but some is just copy/paste to make it convenient to run it as one module. `CompletionTestCase_up` contains a few simple test cases for the general functionality I want. Below that, completion hook uses the EXQUISITE [pathlib](https://docs.python.org/3/library/pathlib.html) library to generate a list of paths from either the current path or the environment variable I'm using for testing. It also grabs the contents of `COMP_LINE`, set by `complete` as according to the manual excerpt). From there, it creates a dictionary of path parts to parent paths and the dictionary's keys are matched against most of `comp_line`. If there's only one match, it returns the path.

So to summarize:

1. Thanks to the `complete -C command` option of complete, bash completion scripts can be written in any language, and that's incredibly underrated.
2. It's understandably underrated because the `complete` function doesn't lend itself well to automation, let alone debugging, and documentation is accessed via `man builtins` instead of `man complete`.
3. By approximating `complete`'s functionality, you can write unit tests to allow for completions of higher complexity.

Lastly, I've included all the above in the form of [completion_utils](https://github.com/CarvellScott/completion_utils) here. It has a bunch of convenience functions to help you write your completions: The bash_completion function from earlier, a decorator you can place around `completion_hook` to take care of passing arguments and provide installation instructions of a sort, and likely more stuff over time.

Thanks for reading, and happy coding!
