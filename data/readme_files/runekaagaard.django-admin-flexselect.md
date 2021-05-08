## About Django Admin FlexSelect ##

FlexSelect is a small app for the Django Admin that makes it trivial to have
foreign keys depend on each other. By depend I mean that choices and additional 
content of one field updates dynamically when another is changed.

## Usage example ##

See the video at http://www.youtube.com/watch?v=ooii3iCTZ6o.

In the following we will define a Case model with two foreign key fields, a 
base field `client` and a trigger field `company_contact_person`. When we 
change the client on the Case change view the company_contact_person updates 
accordingly. Furthermore we will display the customer_contact_persons company 
and email as additional details. 

In "models.py":

```python
from django.db import models as m
from django.core.exceptions import ValidationError

"""
No changes to the models are needed to use flexselect.
"""

class Company(m.Model):
    name = m.CharField(max_length=80)
    
    def __unicode__(self):
        return self.name

class CompanyContactPerson(m.Model):
    company = m.ForeignKey(Company)
    name = m.CharField(max_length=80)
    email = m.EmailField()
    
    def __unicode__(self):
        return self.name
    
class Client(m.Model):
    company = m.ForeignKey(Company)
    name = m.CharField(max_length=80)
    
    def __unicode__(self):
        return self.name
     
class Case(m.Model):
    client = m.ForeignKey(Client)
    company_contact_person = m.ForeignKey(CompanyContactPerson)
    
    def clean(self):
        """
        Makes sure the company for client is the same as the company for the 
        customer contact person. Note that you need to check for `None` too
        if the fields are not required.
        """
        if not self.client.company == self.company_contact_person.company:
            raise ValidationError('The clients and the contacts company does'
                                  ' not match.')
    
    def __unicode__(self):
        return u'Case: %d' % self.id
```

In "admin.py":

```python
from django.contrib import admin
from flexselect import FlexSelectWidget
from test_flexselect.tests.models import (Company, Case, Client, 
                                          CompanyContactPerson,)

class CompanyContactPersonWidget(FlexSelectWidget):
    """
    The widget must extend FlexSelectWidget and implement trigger_fields, 
    details(), queryset() and empty_choices_text().
    """
    
    trigger_fields = ['client']
    """Fields which on change will update the base field."""
    
    def details(self, base_field_instance, instance):
        """
        HTML appended to the base_field.
        
        - base_field_instance: An instance of the base_field.
        - instance: A partial instance of the parent model loaded from the
                    request.
                    
        Returns a unicoded string.
        """
        return u"""\
        <div>
            <dl>
                <dt>%s</dt><dd>%s</dd>
                <dt>%s</dt><dd>%s</dd>
            </dl>
        </div>
        """ % ('Company', base_field_instance.company,
               'Email',  base_field_instance.email,
              )
        
    def queryset(self, instance):
        """
        Returns the QuerySet populating the base field. If either of the
        trigger_fields is None, this function will not be called.
        
        - instance: A partial instance of the parent model loaded from the
                    request.
        """
        company = instance.client.company
        return CompanyContactPerson.objects.filter(company=company)
    
    def empty_choices_text(self, instance):
        """
        If either of the trigger_fields is None this function will be called
        to get the text for the empty choice in the select box of the base
        field.
        
        - instance: A partial instance of the parent model loaded from the
                    request.
        """
        return "Please update the client field"
    
class CaseAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Alters the widget displayed for the base field.
        """
        if db_field.name == "company_contact_person":
            kwargs['widget'] =  CompanyContactPersonWidget(
                base_field=db_field,
                modeladmin=self,
                request=request,
            )
            kwargs['label'] = 'Contact'
        return super(CaseAdmin, self).formfield_for_foreignkey(db_field, 
            request, **kwargs)

class ClientAdmin(admin.ModelAdmin):
    pass

class CompanyContactPersonAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Case, CaseAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(CompanyContactPerson, CompanyContactPersonAdmin)
admin.site.register(Company, CompanyAdmin)
```

## Installation ##

    sudo pip install django-admin-flexselect
    
## Configuration ##

1. Add `"flexselect",` to `INSTALLED_APPS` in "settings.py".

2. Add `url(r'^flexselect/', include('flexselect.urls')),` to "urls.py".

### Options ###
As of yet, flexselect only have one configuration option, namely 
"include_jquery" that if set to true will include jQuery and jQueryUI from 
the google ajax CDN. It defaults to false and the entire FLEXSELECT dict can
be omitted.

```python
# Flexselect settings.
FLEXSELECT = {
    'include_jquery': True,
}
```

### Static files ###
FlexSelect requires "django.contrib.staticfiles" installed to work 
out of the box. If it is not then include "jQuery", "jQueryUI" and 
"flexselect/static/flexselect/js/flexselect.js" manually. Read more about 
"django.contrib.staticfiles" at 
https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/.
