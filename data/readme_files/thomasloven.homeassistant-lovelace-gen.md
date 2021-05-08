# lovelace-gen.py A lovelace configuration generator for [homeassistant](https://www.home-assistant.io)

# This is deprecated. Use [lovelace_gen](https://github.com/thomasloven/hass-lovelace_gen) instead.

This script is a pre-processor for your lovelace configuration.

It will read the file `lovelace/main.yaml` and generate `ui-lovelace.yaml` from it.

Using this generator will allow you to use jinja2 templates in your lovelace yaml configuration.
It can also simplify cache invalidation when including scripts and images in your configuration.

## Usage

Create a directory `<homeassistant config dir>/lovelace` and the file `<homeassistant config dir>/lovelace/main.yaml`.

Inside your homeassistant config directory, run the command:

    python3 lovelace-gen.py

This will create the file `ui_lovelace.yaml`.

**Note:** `lovelace-gen` requires some non-standard python packages to be installed, namely ruamel and Jinja2. Those are all required by home-assistant, so by running the script in the same environment as hass, you'll get them for free. Also, python3 is required.

### Optional arguments

`lovelace-gen` will try to find the location of the `lovelace/` directory automatically. If you wish to specify it manually, you can do so as an argument:

    python3 lovelace-gen.py /opt/homeassistant/config/lovelace

By default `ui-lovelace` will be generated in the parent directory of the `lovelace/` directory. This can be changed with the `-o` flag:

    python3 lovelace-gen.py -o ui-lovelace-example.yaml

### Usage in Hass.io

In your configuration.yaml file, make a shell command:

```yaml
shell_command:
  lovelace_gen: 'python /config/lovelace-gen.py > /config/lovelace-gen.log'
```

Restart Home Assistant. Then run the service `shell_command.lovelace_gen`, preferably from `<hass_ip_address:port>/dev-service`.

This will create the file `/config/ui_lovelace.yaml`.
Any errors will be written to `/config/lovelace-gen.log` to help you find the problem.

#### Errors

If the processing fails, the script will try to tell you why.

However, if you are running it as a `shell_command` from Home Assistant, you will - by default - only get the return code in the log.

The possible return codes for errors are:

| Code | Problem |
|---|---|
| 2 | Could not find `lovelace/main.yaml`. |
| 3 | Something failed in the yaml processing. |
| 4 | Could not write `ui-lovelace.yaml`. |

However, you can probably get more information by setting your [log level](https://www.home-assistant.io/components/logger/) to `debug`.

## Special directives

The following directives can be used in `lovelace/main.yaml` or any file included using the `!include` directive.

### `!include <filename>`
Includes the file `lovelace/<filename>`. Works exactly the same way as the built-in include directive, except it's rooted in the `lovelace/` directory.

### `!file <path>`
Is replaced with `<path>?XXX` where `XXX` is a random number that changes each time you run `lovelace-gen`.
The reason for this is that e.g.

```yaml
image: !file /local/images/photo.png
```

may be replaced with

```yaml
image: /local/images/photo.png?234567890234567893456789.234567
```

which - to your browser is a totally different filename than e.g. `photo.png?09876540987654098765434567890.35783290` and thus **can not** be loaded from cache.

Incredibly useful if you like to play around with custom plugins or change your images and have problem with things not updating as you expected them to.

### Note about `!secret`
The built in `!secret` directive is of course also usable as normal. `lovelace-gen` ignores it, and it is instead processed by Home Assistant at run-time.

## Jinja2 templates
Lovelace-gen allows you to use jinja templating anywhere in your configuration:

`lovelace/main.yaml`:

```yaml
title: My Awesome Home

{% set plugins = [
  '/local/lovelace-fold-entity-row/fold-entity-row.js',
  '/local/lovelace-layout-card/layout-card.js',
  '/local/lovelace-player/lovelace-player.js',
  ] %}

# Copy resources from anywhere to www/lovelace and include them
resources:
  {% for p in plugins %}
  - url: !file {{ p }}
    type: js
  {% endfor %}

views:
  - title: Bottom floor
    cards:
      - !include floorplan.yaml
```

---

`lovelace/floorplan.yaml

```yaml
type: picture-elements
image: !file /local/bottom_floor.png
elements:
  {% set lamp = """
    type: state-icon
    tap_action: {action: toggle}
    """ %}
  {% set dimlamp = """
    type: state-icon
    tap_action: {action: toggle}
    hold_action: {action: more-info}
    """ %}

  - entity: light.ceiling_hallway
    style: { left: 50%, top: 50% }
    {{ lamp }}

  - entity: light.kitchen_table
    style: {left: 25%, top: 30% }
    {{ dimlamp }}

  - entity: light.her_bed
    style: {left: 75%, top: 30% }
    {{ lamp }}
  - entity: light.his_bed
    style: {left: 75%, top: 35% }
    {{ lamp }}
```
