# eCSStractor

Sublime Text plugin for extracting class names from HTML and generate CSS stylesheet for following work.

Default extracting:

![ecss_normal](https://cloud.githubusercontent.com/assets/654597/5896783/5ac44e42-a54c-11e4-8981-75456ac98f0b.gif)

With BEM nesting:

![ecss_bem](https://cloud.githubusercontent.com/assets/654597/5896785/60708c5c-a54c-11e4-963f-9e00ede168c3.gif)

With BEM nesting and class names as comments:
![ecss_bem_comments](https://user-images.githubusercontent.com/654597/35009441-d1de8982-faff-11e7-8281-7d4e85d4dc5a.gif)

## Usage

Open any document contain HTML and do one of the following:

* Press `Cmd+Shift+X` on Mac OS X or `Ctrl+Shift+X` on Windows/Linux.
* Go to **Tools → eCSStractor → Run**
* Right click and select **eCSStractor → Run**

Then you will see new tab with CSS selectors extracted from document.

Plugin can process either selected text or whole file.

You can explicit **Run (with BEM Nesting)** or **Run (without BEM Nesting)** regardless `bem_nesting` option from Command Palette, Menu or Context Menu.

## Options

The default settings can be viewed by accessing the **Preferences → Package Settings → eCSStractor → Settings – Default** menu entry. To ensure settings are not lost when the package is upgraded, make sure all edits are saved to **Settings – User**.

#### brackets

Add brackets. Useful for Sass syntax and Stylus.

_Default: **true**_

#### brackets_newline_after

Add new line after open bracket.

_Default: **true**_

#### attributes

HTML node attributes from which class names should be extracted.

_Default: **["class", "className"]**_

#### ignore

List of classnames to ignore. Useful for helper classes, that probably already described. Ex., `clearfix`. See **Settings – Default** for example.

_Default: **empty**_

#### ignore_regex

Similar to `ignore` option, but use [RegEx](https://docs.python.org/3.4/library/re.html#regular-expression-syntax) to ignore. Ex., `^js-` will ingore all classes started with `js-`. See **Settings – Default** for example.

_Default: **empty**_

#### destination

Where to put result: new tab (`tab`) or copy to clipboard (`clipboard`)

_Default: **tab**_

#### bem_nesting

BEM Nesting. Generate nested stylesheet for preprocessors rather simple stylesheet. See the difference in the [Examples](#examples) section.

_Default: **false**_

### Options only for BEM Nesting is on

#### indentation

Indentation.

_Default: **\t**_

#### bem.element_separator

Separator between block and element names.

_Default: ___

#### bem.modifier_separator

Separator between block or element and they modifier.

_Default: **--**_

#### preprocessor.parent_symbol

Parent symbol. Ex.: `&__element {}`

_Default: **&**_

#### empty_line_before_nested_selector

Add empty line before nested element/modifier.

_Default: **false**_

#### add_comments

Generate full class names as a comments before nested BEM elements and modifiers. This is useful for finding selectors by class names. See the difference in the [Examples](#examples) section.

_Default: **false**_

#### comment_style

Comment style shows `CSS` (`/* */`) or `SCSS` (`//`) style comments. Works with `add_comments` enabled.

_Default: **"CSS"**_

## Examples

Source:

```html
<ul class="nav nav--main">
    <li class="nav__item"><a href="" class="nav__link">Home</a></li>
    <li class="nav__item"><a href="" class="nav__link">Shop</a></li>
    <li class="nav__item"><a href="" class="nav__link nav__link--special">About</a></li>
</ul>
```

Run eCSStractor (BEM Nesting is off):

```css
.nav {
}
.nav--main {
}
.nav__item {
}
.nav__link {
}
.nav__link--special {
}
```

Run eCSStractor (BEM Nesting is on):

```scss
.nav {
    &--main {
    }
    &__item {
    }
    &__link {
        &--special {
        }
    }
}
```

Run eCSStractor (BEM Nesting and Comments are on):

```css
.nav {
    /* .nav--main */
    &--main {
    }
    /* .nav__item */
    &__item {
    }
    /* .nav__link */
    &__link {
        /* .nav__link--special */
        &--special {
        }
    }
}
```

Run eCSStractor (BEM Nesting and Comments are on and comment style is SCSS):

```scss
.nav {
    // .nav--main
    &--main {
    }
    // .nav__item
    &__item {
    }
    // .nav__link
    &__link {
        // .nav__link--special
        &--special {
        }
    }
}
```

# Installation

Most simple way it's install with [Package Control](https://packagecontrol.io/).

Open the Command Palette `Cmd+Shift+P` (OS X) or `Ctrl+Shift+P` (Linux/Windows) and select “Package Control: Install Package”, then search for `eCSStractor`.

# Similar tool

I've been inspired by [extractCSS](http://extractcss.com/) online tool. This tool have much more functions, but not very convenient for regular use.
