# 💡 SublimeCodeIntel LSP

This is the experimental fork with Language Server Protocol support of
SublimeCodeIntel. The following languages are available:

+ **CSS-CodeIntel** -> CSS/SCSS/Sass/Less
+ **Cpp-CodeIntel** -> C/C++/Objective-C/Objective-C++
+ **HTML-CodeIntel** -> HTML
+ **JSON-CodeIntel** -> JSON/JSONC
+ **JavaScript-CodeIntel** -> JavaScript/TypeScript/Node.js
+ **Markdown-CodeIntel** -> Markdown
+ **OCaml-CodeIntel** -> OCaml
+ **PHP-CodeIntel** -> PHP
+ **Python-CodeIntel** -> Python2/Python3
+ **Rust-CodeIntel** -> Rust
+ **YAML-CodeIntel** -> YAML


## Installation

For the moment, SublimeCodeIntel LSP isn't available in Package Control yet,
to install you need to directly add repositories as well as adding the
installed packages.

From command palette add SublimeCodeIntel and the relevant repositories:

Ex.:
`Package Control: Add Repository` -> `https://github.com/Kronuz/SublimeCodeIntel`
`Package Control: Install Package` -> `SublimeCodeIntel`

`Package Control: Add Repository` -> `https://github.com/Kronuz/Python-CodeIntel`
`Package Control: Install Package` -> `Python-CodeIntel`

Or directly modify your `Packages/User/Package Control.sublime-settings`:

```json
{
	"installed_packages": [
		"SublimeCodeIntel",
		"CSS-CodeIntel",
		"Cpp-CodeIntel",
		"HTML-CodeIntel",
		"JSON-CodeIntel",
		"JavaScript-CodeIntel",
		"Markdown-CodeIntel",
		"OCaml-CodeIntel",
		"PHP-CodeIntel",
		"Python-CodeIntel",
		"Rust-CodeIntel",
		"YAML-CodeIntel"
	],
	"repositories": [
		"https://github.com/Kronuz/SublimeCodeIntel",
		"https://github.com/Kronuz/CSS-CodeIntel",
		"https://github.com/Kronuz/Cpp-CodeIntel",
		"https://github.com/Kronuz/HTML-CodeIntel",
		"https://github.com/Kronuz/JSON-CodeIntel",
		"https://github.com/Kronuz/JavaScript-CodeIntel",
		"https://github.com/Kronuz/Markdown-CodeIntel",
		"https://github.com/Kronuz/OCaml-CodeIntel",
		"https://github.com/Kronuz/PHP-CodeIntel",
		"https://github.com/Kronuz/Python-CodeIntel",
		"https://github.com/Kronuz/Rust-CodeIntel",
		"https://github.com/Kronuz/YAML-CodeIntel"
	]
}
```
