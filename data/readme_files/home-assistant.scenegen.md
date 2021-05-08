# SceneGen

Scenegen is a scene generation tool for [Home Assistant](https://home-assistant.io/) home automation software. It creates scenes by example, by reading the current states of devices and outputting a corresponding scene. Scenegen is written in python using Home Assistant's RESTFul API so can be run from anywhere. It currently supports lights and switches only.

To set up SceneGen and install it locally, run the following from a shell in
the checkout:

    $ make

Then the script can be run locally from the checkout:

    $ ./bin/scenegen --help

See the Home Assistant documentation for [full usage instructions and
documentation](https://home-assistant.io/ecosystem/scenegen).


## Exporting Multiple Scenes

Use the `$ make export` target to aid in exporting multiple scenes to YAML on
the filesystem.  This can be useful for "exporting" scenes from an
integration, such as SmartThings, to native Home Assistant themes:

    $ make EXPORT_ALL_SCENES=true URL=https://home-assistant.example.com:8123 TOKEN=... EXPORT_SCENE_DIR=../path/to/scenes export

If you don't want to export all the scenes, you can create a `.scenes` file in
the `EXPORT_SCENE_DIR` listing one scene per line to export and remove the
`EXPORT_ALL_SCENES` option.

Beyond these options, the `export*` targets in `Makefile` can be used as a
reference or starting point to automate exporting multiple scenes.
