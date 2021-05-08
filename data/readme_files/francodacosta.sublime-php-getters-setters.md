PHP Getters and Setters
=======================


With PHP Getters and Setters you can automatically generate _Getters_ and _Setters_ for your php classes.

Features:
---------

* Generate Getters, Setters or Both
* Can be applied to all class properties or just to a single one
* Description, Type and Type Hinting automatically discovered from the variable docblock
* fully customizable templates

Usage Instruction:
------------------

1. Generate PHP code

    ```php
    class test
    {
        /**
         * foo container
         *
         * @var AbcClass
         */
        private $foo;
    }
    ```

2. Go to Tools -> PHP Getters and Setter
3. Getter and Setter will be generated:

    ```php
    class test
    {
        /**
         * foo container
         *
         * @var AbcClass
         */
        private $foo;
    
        /**
         * Gets the foo container.
         *
         * @return AbcClass
         */
        public function getFoo()
        {
            return $this->foo;
        }
    
        /**
         * Sets the foo container.
         *
         * @param AbcClass $foo the foo
         */
        private function _setFoo(AbcClass $foo)
        {
            $this->foo = $foo;
            
            return $this;
        }
    }
    ```

As you can see if get to trouble of commenting your variables, the generated functions can be used without modification.

This is an huge time saver!

Usage
-----

Commands available are:

 * Generate Getters and Setters
 * Generate Getter
 * Generate Setter
 * Generate Getter for...
 * Generate Setter for...

These can be accesed via the context menu (right click on the source of any open PHP file) or the command pallette. The currently open file *must* be a PHP file.

Settings Reference
------------------

###ignore_visibility
_type_    : **boolean**

_default_ : **false**

_description_: ignore visibilty for setters generation

###registerTemplates
_type_   : **array**

_default_: **[]**

_description_: the user templates to load

###template
_type_   : **string**

_default_: **camelCaseFluent**

_description_: the template to use

### type_hint_ignore
_type_: **list of strings**

_default_: **["mixed", "int","integer", "double", "float", "number", "string", "boolean", "bool", "numeric", "unknown"]**

_description_: if the property has one of the types listed type hinting will not be used

### setter_before_getter
_type_: **boolean**

_default_: **false**

_description_: Set to true to generate setter code before getters

Creating your own template
--------------------------


[package-dir] is your [package directory](http://docs.sublimetext.info/en/sublime-text-3/basic_concepts.html#the-packages-directory).

* Make a directory called ```[package-dir]/PHP Getters and Setters```.
* Put the following in a file at ```[package-dir]/PHP Getters and Setters/user_templates.py```.
  ```
class myTemplate(object):
    name = "myTemplate"
    style = 'camelCase' # can also be snakeCase
    getter = """ 
    /**
    * Gets the %(description)s.
    *
    * @return %(type)s
    */
    public function get%(normalizedName)s()
    {
        return $this->%(name)s;
    }
"""

    setter = """ 
    /**
    * Sets the %(description)s.
    *
    * @param %(type)s $%(name)s the %(humanName)s
    *
    * @return self
    */
    public function set%(normalizedName)s(%(typeHint)s $%(name)s)
    {
        $this->%(name)s = $%(name)s;
    }
"""
  ```
* Edit the parts between setter and getter how you want.
* Edit your user settings for this package. On OSX that's ```Preferences | Package Settings | PHP Getters and Setters | Settings - User```.
* Add the following settings
  ```
    // user defined templates to load
    "registerTemplates" : [ "myTemplate" ],

    // the template used to generate code
    "template" : "myTemplate",
  ```
 * restart sublime to use the new template
  
