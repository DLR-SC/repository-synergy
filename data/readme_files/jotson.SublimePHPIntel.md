# SublimePHPIntel

PHP code scanner and analyzer for code intelligence within PHP projects.

*Sublime Text 3: Checkout branch `st3` for Sublime Text 3 compatible version*

## Setup

0. Install using Package Control
1. Create or open a project with PHP files
2. Run the PHPIntel: Scan Project command from the command palette

After the initial scan, PHP files will be automatically re-scanned whenever you save them.

## Go to declaration

To open a class declaration, place your cursor on the class name and press `Ctrl+f5` or `Cmd+f5`

## Magic and factory methods

You can teach SublimePHPIntel about magic and factory methods using regular
expression matching. Some expressions for Magento and the Yii framework are already included. Please send pull requests with additional expressions for other frameworks that you'd like to see included out of the box.

For example, your code might have a factory method that returns a model:

```php
App::getModel('modelname')->doSomething();
```

To get code completion for this, define a template for the factory in the configuration settings (Preferences | Package Settings | SublimePHPIntel | Settings - User).

Factory patterns are defined like so:

```json
{
    "customfactories":
        [
            { "pattern": "<Regular expression>", "class": "<Class name>", option, ..., option },
            { "pattern": "<Regular expression>", "class": "<Class name>", option, ..., option },
            ...
            { "pattern": "<Regular expression>", "class": "<Class name>", option, ..., option }
        ]
}
```

* Patterns are just regular expressions.
* Class names are strings with optional numbered expressions that match capturing groups in the regular expressions.
* You need to double escape backslashes to preserve them.

For example, this:
```json
{ "pattern": "getModel\\('(.*?)'\\)", "class": "Model_%1", "capitalize": true }
```
...will cause this:
```php
getModel('abc')
```
...to be interpreted as:
```php
Model_Abc
```

**Options**

capitalize: *true|false* — *Uppercase the first letter of the captured expression*

## Known issues

I'm working on these issues:

- Variable assignment is not detected (for example: <code>$var = CODE</code> where CODE returns an object.
- Files are not removed from the index when they are deleted. For now, you'll need to rescan to remove them.
- Files added to the project from outside of the editor are not added to the index. For now, you'll either need to open the file and save it or rescan the project.
- I'm not completely happy with the way it deals with cases where the same class is declared more than once. Need to do some research to see how others deal with that.
