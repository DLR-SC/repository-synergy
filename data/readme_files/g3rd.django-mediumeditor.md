# Django Medium Editor
Adds [Medium Editor](https://yabwe.github.io/medium-editor/) to [Django](https://www.djangoproject.com/).

## Supported Environments

* Django 1.10+
* Python 3.6

## Installation

1. Install **django-mediumeditor**

    via PyPi:
    ```
    pip install django-mediumeditor
    ```
    via GIT:

    ``` 
    pip install git+https://github.com/g3rd/django-mediumeditor.git
    ```

2. Install app
    ```
    INSTALLED_APPS = [
        ...
        'mediumeditor',
    ]
    ```

## Usage

### Django Admin

Add to Admin class

```
from mediumeditor.admin import MediumEditorAdmin

@admin.register(MyModel)
class MyModelAdmin(MediumEditorAdmin, admin.ModelAdmin):
    ...
    mediumeditor_fields = ('my_text_field', )
    ...
```

### Forms

1. Override the Widget for the field

    ```
    from mediumeditor.widgets import MediumEditorTextarea

    class MyForm(forms.ModelForm):
        ...
        class Meta:
            model = MyModel
            widgets = {
                'my_text_field': MediumEditorTextarea(),
            }
    ```

2. In the ```<head>``` of the template
    ```
    {{ form.media }}
    ```

### Settings
Optionaly change theme or change medium editor options in your settings.py
```
# Theme options `default`, `roman`, `mani`, `flat`, `bootstrap`, `tim`, `beagle`
MEDIUM_EDITOR_THEME = 'beagle' # `default` is default theme
MEDIUM_EDITOR_OPTIONS = {..}
```
[Available Options](https://github.com/yabwe/medium-editor/blob/master/OPTIONS.md)

Example:
```
MEDIUM_EDITOR_THEME = 'bootstrap'
MEDIUM_EDITOR_OPTIONS = {
    'toolbar': {
        'static': True,
        'buttons': [
            'bold',
            'italic',
            'underline',
            'strikethrough',
            'subscript',
            'superscript',
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'h6',
        ]
    },
    'paste': {
        'forcePlainText': True,
        'cleanPastedHTML': False,
        'cleanReplacements': [],
        'cleanAttrs': ['class', 'style', 'dir'],
        'cleanTags': ['meta']
    }
}
```

## Contributing

[Take out some bugs](https://github.com/g3rd/django-mediumeditor/issues)

[Report issues or feature requests](https://github.com/g3rd/django-mediumeditor/issues)


## License
MIT: https://github.com/g3rd/django-mediumeditor/blob/master/LICENSE
