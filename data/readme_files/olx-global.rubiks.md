<p align="center">
  <img src="docs/logos/rubiks-logo-horizontal.png" title="Rubiks Logo">
</p>

# Rubiks - a kubernetes yaml file manager

Rubiks exists to help programmatically generate and maintain the yaml files associated with kubernetes configuration.

The rubiks compiler provides a [DSL](docs/Kube%20files%20and%20the%20DSL.md) (basically python) to help make this happen.

## Rubiks Licensing

Rubiks is available under the Apache 2.0 Licence (see the file [LICENCE](LICENCE) included in this distribution) and contains a distribution of PyYAML (see the file [PyYAML.LICENCE](PyYAML.LICENCE) for more information). It has been written by OLX, a part of the Naspers Group.

## Installing Rubiks

Installing Rubiks is easy, you can just clone this repository to your working space and then symlink the rubiks binary into somewhere (eg `~/bin`) that is on your executable search path (`$PATH`). Then you should be able to do `rubiks help` or `rubiks -h` to get a list of commands.

To use the [examples](https://github.com/olx-global/rubiks-examples), you can clone that repository, and then when you have cd-ed into it, you can run `rubiks generate` (or `/path/to/rubiks/rubiks generate` if it isn't on your path as above) to generate an `out` directory at the top-level of the repository with all the YAML files inside it.

## Using Rubiks

Rubiks is designed to point at a [Rubiks Repository](docs/Rubiks%20repositories%20and%20the%20.rubiks%20file.md), which is just a repository with some possible rubiks configuration (in the form of a .rubiks file in the repository root), and some rubiks source files.

Running `rubiks generate` while anywhere in such a repository (anywhere that `git` will detect the repository) will generate you all the YAML files (all relative to the repository root) which you can use to update your clusters. Right now, we can use `git status` / `git diff` and knowing what was changed to update these clusters, but in future this will be resolvable within rubiks itself.

See also `rubiks help` for more information on how to use it

## Full set of docs

- [Kube files and the DSL](docs/Kube%20files%20and%20the%20DSL.md)
- [Rubiks repositories and the .rubiks file](docs/Rubiks%20repositories%20and%20the%20.rubiks%20file.md)
- [Examples](https://github.com/olx-global/rubiks-examples)
- [Logo Variants](docs/logos/logos.md)
