openstack.nose_plugin - Nose plugin for openstack style test output
===================================================================

openstack.nose_plugin provides a nose plugin that allow's nosetests output to
mimic the output of openstack's run_tests.py.

Installation
------------
    pip install openstack.nose_plugin

Usage
-----

The following options are available:

    --with-openstack      Enable plugin Openstack: Nova style output
                          generator
                          [NOSE_WITH_OPENSTACK]
    --openstack-red=OPENSTACK_RED
                          Colorize run times greater than value red.
                          [NOSE_OPENSTACK_RED] or 1.0
    --openstack-yellow=OPENSTACK_YELLOW
                          Colorize run times greater than value yellow.
                          [NOSE_OPENSTACK_RED] or 0.25
    --openstack-show-elapsed
                          Show the elaped runtime of tests.
                          [NOSE_OPENSTACK_SHOW_ELAPSED]
    --openstack-color     Colorize output. [NOSE_OPENSTACK_COLOR]
    --openstack-nocolor   Disable colorize output. [NOSE_OPENSTACK_COLOR]
    --openstack-num-slow=OPENSTACK_NUM_SLOW
                          Number top slowest tests to report.
                          [NOSE_OPENSTACK_NUM_SLOW]
