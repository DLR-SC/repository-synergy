**This repository is deprecated in favor of the more recent versions by enaml's primary author, at https://github.com/nucleic/enaml.**

**To use those newer versions of enaml with Enthought Traits, see https://github.com/enthought/traits-enaml.**

----

----

Enaml is not a Markup Language

**E**\naml is **N**\ot **A** **M**\arkup **L**\anguage. Enaml is a library for
creating professional quality user interfaces with minimal effort. Enaml combines
a domain specific declarative language with a constraints based layout system to
allow users to easily define rich UIs with complex and flexible layouts. Enaml
applications can transparently run on multiple backends (Qt and Wx) and on
multiple operating systems (Windows, OSX, Linux).

Other great Enaml features include

    1) Declarative UI specification langauge that is a strict superset of Python
    2) Architecture design which encourages Model View separation
    3) Subscription based operators which allow state and events to freely flow between models and views
    4) Ability to easily subclass widgets to override functionality of builtin widgets
    5) Support for custom UI widgets
    6) Class based widget design encourages re-use of UI code
    7) Well documented code base that is easy to understand

Enaml is heavily inspired by Qt's QML system, but Enaml uses native
widgets (as opposed to drawing on a 2D canvas) and is toolkit independent.
Currently supported/in-development toolkits include Qt4 and Wx. The Qt
toolkit is strongly recommended over Wx.

Enaml is extensible and makes it extremely easy for the user to define
their own widgets, override existing widgets, create a new backend toolkit,
or even hook the runtime to apply their own expression dependency behavior.
About the only thing not hookable is the Enaml language syntax itself.

The enamldoc package provides a Sphinx extension for documenting Enaml objects.

Prerequisites

* Python >= 2.6 (not Python 3)
* Traits
* Casuarius (https://github.com/enthought/casuarius)
* PySide or PyQt4 (only if using the Qt backend)
* wxPython (only if using the wx backend)
* PLY (Python Lex-Yacc), for parsing *.enaml* files
* Sphinx (only if building the docs)
