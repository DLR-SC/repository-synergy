# PHP code formatter for Sublime Text editor with Pear php_beautifier
#### [Sublime Text 2](http://www.sublimetext.com/2)
#### [Php_beautifier](http://pear.php.net/package/PHP_Beautifier)

## About
This is a Sublime Text 2 plugin allowing you to format your PHP code. 
It uses php beautifier.

## Installation
Install php-pear and php-cli with your package manager :
 * php-pear & php5-cli with Debian
 * php-pear & php with Archlinux

Install php beautifier from pear channel :
`sudo pear install --alldeps  channel://pear.php.net/php_beautifier-0.1.15`

Clone or download the files and copy them to your `Packages` folder. You can access it via Preferences -> Browse Packages in sublime text.

## Usage
ctrl + shift + P and type `Format: PHP`, or you can use the ctrl + alt + f keybinding.

## Customize
You can define some options in the script `php_beautifier.py`. 
Default options are : `PHP_OPTIONS = "-s4 -l 'ArrayNested()' "` (indent with 4 spaces and nested arrays).

