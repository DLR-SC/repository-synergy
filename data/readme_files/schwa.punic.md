# punic [![Travis][image_1]][link_1] [![license][image_2]][link_2] [![tag][image_3]][link_3]

## IMPORTANT

Due to work restrictions I can no longer contribute or maintain this project. I'd be happy to pass over ownership onto any interested party who is willing to maintain it. Please let me know: [schwa@schwa.com](mailto:schwa@schwa.com)

---

[image_1]: https://img.shields.io/travis/schwa/punic.svg?maxAge=3600
[link_1]: https://travis-ci.org/schwa/punic/branches
[image_2]: https://img.shields.io/github/license/schwa/punic.svg?maxAge=3600
[link_2]: https://github.com/schwa/punic/blob/master/LICENSE
[image_3]: https://img.shields.io/github/tag/schwa/punic.svg?maxAge=3600
[link_3]: https://github.com/schwa/punic/releases

## Description

Punic is intended to be an easier to use, faster and more reliable implementation of the [Carthage](http://github.com/carthage/carthage) dependency management system.

## What's New?

See [VERSION_HISTORY.markdown](https://github.com/schwa/punic/blob/master/VERSION_HISTORY.markdown)

## Caveat!!!

<strike>Punic can be considered an early preview release and probably is not ready for production use. Use at your own peril.</strike>

Punic has been running on a production system for a while now. While bugs probably can and do exist it is ready to replace Carthage.

## Installation

### Homebrew (NEW!)

Punic can now be installed via [homebrew](http://brew.sh). This is the *preferred* installation method and does not require installation of any other dependencies. This method is also preferred for continuous integration.

```shell
$ brew tap schwa/punic
$ brew install punic
```

You keep punic up to date using the normal homebrew methods:

```shell
$ brew update
$ brew upgrade
```

### pypi.python.org

If you're prefer you can also install punic from [pypi] (https://pypi.python.org/pypi/punic/)

```shell
$ brew install libyaml
$ pip install punic           # or `pip3 install punic`
```

Note: Punic is python 3.6 compatible and should work the same in both versions of the language.

Note be careful installing punic (and in fact _all_ python software) with `sudo`. In fact installing with `sudo` is not explicitly supported.

Installing punic inside a python virtualenv is supported but you might have difficulty if you try to execute a virtualenv-ed punic from Xcode (e.g. `punic copy-frameworks`).

## Usage

Punic has built-in help:

```
$ punic --help
Usage: punic [OPTIONS] COMMAND [ARGS]...

Options:
  --echo                  Echo all commands to terminal.
  --verbose               Verbose logging.
  --color / --no-color    TECHNICOLOR.
  --timing / --no-timing  Log timing info
  --help                  Show this message and exit.

Commands:
  build            Fetch and build the project's dependencies.
  cache            Cache punic build artifacts to Amazon S3
  clean            Clean project & punic environment.
  copy-frameworks  In a Run Script build phase, copies each...
  fetch            Fetch the project's dependencies..
  graph            Output resolved dependency graph.
  init             Generate punic configuration file.
  list             Lists all platforms, projects, xcode...
  readme           Opens punic readme in your browser...
  resolve          Resolve dependencies and output...
  search           Search github for repositories and optionally...
  update           Update and rebuild the project's...
  version          Display the current version of Punic.
schwa@ungoliant ~/D/test>
```

Each sub-command also has built in help:

```
$ punic build --help

Usage: punic build [OPTIONS] [DEPS]...

  Fetch and build the project's dependencies.

Options:
  --configuration TEXT  Dependency configurations to build. Usually 'Release'
                        or 'Debug'.
  --platform TEXT       Platform to build. Comma separated list.
  --fetch / --no-fetch  Controls whether to fetch dependencies.
  --help                Show this message and exit.
```

To make your Xcode project consume other Carthage compatible dependencies add a file called `Cartfile` at the root level of your project. For example:

```
github "AlamoFire/AlamoFire"
github "realm/realm-cocoa"
```

Punic uses Carthage's syntax and structure for Cartfiles. For more information see the [Carthage documentation](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile) itself.

A `Cartfile` isn't required to exactly specify what version of which dependency it requires, To do that you can manually resolve your dependencies:

```shell
punic resolve
```

This resolve step creates a new file called `Carthage.resolved`. Using the above file as input the `Cartfile.resolved` contains the following:

```
github "AlamoFire/AlamoFire" "3.4.1"
github "realm/realm-cocoa" "v1.0.2"
```

Note that the resolve sub-command has to fetch all dependencies. This can take a while the first time you run it.

You generally do not need to manually invoke `punic resolve` - it is usually automatically performed for you as part of an update. See later.

To checkout and build your dependencies run `punic build`. For example

```shell
punic build --platform iOS --configuration Debug
```

This fetches the latest versions of all dependencies and then builds them.

You can only build your dependencies if your dependencies have been resolved (i.e. there's a `Cartfile.resolved` file in your project's directory).

You should run `punic build` when:

* You first clone a punic enabled project
* Your `Carthage.resolved` file has changed (perhaps you fetched some changes from another developer)

If you know punic already has the correct dependencies checked out you can run build with the `--no-fetch` switch:

```shell
punic build --platform iOS --configuration Debug --no-fetch
```

Note that you can specify a platform and a configuration for `punic build`. If you fail to specify a platform then all platforms will be compiled. If you fail to specify a configuration then the dependency's default will be used (this is usually "Release").

If you always specify the same platform and configuration for builds you can create a `punic.yaml` file in the same directory as your `Cartfile`:

```yaml
defaults:
  configuration: Debug
  platform: iOS
  xcode-version: 7.3.1
```

You can use `punic init` to help you generate a `punic.yaml` (TODO: We intend `punic.yaml` will increase in expressiveness over time)

If you want to perform a quick clean of a project (deleting the project's "Derived Data" directory) you can use the following:

```shell
punic clean
```

Running `punic resolve` then `punic build` together is a common operation and have been combined into the `punic update` sub-command:

```shell
punic update
```

See https://github.com/Carthage/Carthage for usage information


## New Features

### `punic.yaml` files.

As well as configuring your build dependencies with `Cartfile` you can also use a `punic.yaml` file to specify other options.

#### `punic.yaml` defaults

An example `punic.yaml` file follows:

```yaml
defaults:
  configuration: Debug
  platform: iOS
```

This example specifies both a default configuration and a default platform. This allows you to skip providing `--configuration` and `--platform` switches on the command-line.

Switches provided on the command line will override defaults in your `punic.yaml` file.

#### `punic.yaml` repo-overrides

Assume you have a project that depends on an external repository "ExampleOrg/Project-A" which in turns depends on another external repository "ExampleOrg/Project-B". If you wanted to fork and make changes to "Project-B" you would also have to fork and change the Cartfile within "Project-A" so that it refers to the forked URL of "Project-B".

With the `repo-overrides` section of `punic.yaml` you can globally replace the URL of any dependency without having to edit Cartfiles deep within your dependency hierarchy.

```yaml
repo-overrides:
  Project-B: git@github.com:MyOrg/Project-B.git
```

You can also use this feature to redirect a dependency to a local, on disk url. This is useful if you need to test changes inside a dependency.

```yaml
repo-overrides:
  Project-B: file:///Users/example/Projects/Project-B
```

Note that repositories pointed to by file URL are still cloned and fetched just like any other repository and your changes _must_ be committed for them to be picked up by Punic.

#### `punic.yaml` skip lists

Punic by default will build every scheme of every xcode project of every dependency, if the scheme's Build target builds a .framework of the correct platform architecture. This can often cause punic to build too many frameworks - some of which are not used by your root project.

You can use the `skips` section of your root project's `punic.yaml` to define what punic should skip during its build phase.

For example:

```yaml
defaults:
  configuration: Debug
  platform: iOS
skips:
- [ iOS, NMSSH, NMSSH.xcodeproj ]
- [ iOS, rxswift, Rx.xcodeproj, RxBlocking-iOS ]
- [ iOS, rxswift, Rx.xcodeproj, RxCocoa-iOS ]
- [ iOS, rxswift, Rx.xcodeproj, RxTests-iOS ]
- [ iOS, Eureka, Example.xcodeproj ]
- [ iOS, realm-cocoa, Realm.xcodeproj, Realm ]
```

A skips list is made of a list of filters. Each filter is a list of platform name, dependency name, Xcode project name and scheme name. You can leave out the scheme name if you want to skip all schemes in a particular xcode project.

## Roadmap

The punic roadmap is managed here: https://github.com/schwa/punic/projects

## Contributing

Bug reports, feature suggestions are most welcome. If you want improve punic yourself clone punic, and run `pip install -e .` from inside. You can then make changes inside your cloned repository and test them live.

## Differences between Punic & Carthage

Importantly: `carthage bootstrap` has been replaced by `punic build`. See the [FAQ](#where-did-the-bootstrap-command-go) for more information.

Aside from differences of implementation one of the fundamental differences is that Carthage always runs `xcodebuild clean` before building dependencies. Punic deliberately does not perform this clean step and provides an explicit `punic clean` command. The goal of this is to not force collaborators to sit through long clean builds when very little has changed. This can provide dramatic speed ups to a users workflow (during testing builds that can take Carthage 20-25 minutes to build on top-end hardware take less than a minute to do a 'dirty' build.)

Punic only supports "github" style dependency specifications.

For more detailed information see the [Punic documentation](https://github.com/schwa/punic/blob/master/documentation/Notes.markdown).

## Frequently Answer Questions

### Where did the `bootstrap` command go?

Bootstrap proved to be confusing with users believing they should only run it once per project and not whenever the `Cartfile.resolved` has changed. It has been replaced by the `build` subcommand. The previous behavior of the build subcommand can be reproduced with: `punic build --no-fetch`.

### Why can't I specify use the `--derived-data` switch?

It seems best to always use a custom derived data directory for punic builds. This keeps punic builds of dependencies separated from your own builds. It also allows punic to very quickly clean the derived-data directory.

### Where does punic store keep everything?

```
<project-dir>/
    Cartfile
    Cartfile.resolved
    Carthage/
        Build/
        Checkouts/
    punic.yaml
~/Library/Application Support/io.schwa.punic/
    DerivedData/
    cache.shelf
    repo_cache/
```

### Why rewrite Carthage?

Carthage has had some rather severe performance and stability issues that have made it very hard to reliably use in production. These issues have historically proven very hard for the maintainers of Carthage to address. Instead of contributing fixes to Carthage it was deemed quicker and easier to produce a new clean room implementation of the concepts pioneered by the Carthage developers

(TODO: Link to Carthage issues.)

### What about Swift Package Manager?

Swift Package Manager is currently in its very early days and it will be a while before SPM is ready to be used to ship software. Until then Carthage and Punic still serve an important role.

### Why not use Cocoapods?

No thank you.

### How can I use punic with circleci

Add the following to your circle.yml file:

```
machine:
  xcode:
    version: 8.3
dependencies:
  pre:
    - brew tap schwa/punic
    - brew install punic
    - punic build
```

## License

MIT
