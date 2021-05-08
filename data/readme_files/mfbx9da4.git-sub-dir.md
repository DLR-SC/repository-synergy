Downloads git sub dir

## Usage
    python get_git_sub_dir.py user/repo <options>
    python get_git_sub_dir.py user/private_repo --private <options>

## Options Flags:
- `--private`: the repo is private (default is `False`, username and password will be requested)
- `-r`: recursive download (default is `True`)
- `-p`: filepath
- `-b`: branch

## Example

Let's download the docs from twitter bootstrap https://github.com/twbs/bootstrap/tree/master/docs

    python get_git_sub_dir.py twbs/bootstrap -p docs

If we don't want it to be recursive

    python get_git_sub_dir.py twbs/bootstrap -p docs -r False

If we want a specific file

    python get_git_sub_dir.py twbs/bootstrap -p docs/examples/blog/index.html

If we want to download from a specific branch (say `fix-15534`)

    python get_git_sub_dir.py twbs/bootstrap -p docs/examples/blog/index.html -b fix-15534
