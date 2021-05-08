[![codeq](https://codeq.io/github/gkuhn1/django-admin-multiupload/badges/master.png)](https://codeq.io/github/gkuhn1/django-admin-multiupload/branches/master)
django-admin-multiupload
========================

Multi file upload for django-admin app

Installation
------------

pip install git+git://github.com/gkuhn1/django-admin-multiupload.git

Requeriments
------------

Django1.4 ~ 1.7 : Use release v1.7

Django1.8 ~ 1.9 : Use release v1.8

Django1.10 ~ 1.11 : Use master


Usage
-----

1. Add ``'multiupload'`` to your ``INSTALLED_APPS``
2. Inherit Your ModelAdmin from ``multiupload.admin.MultiUploadAdmin``
    ```python
    from multiupload.admin import MultiUploadAdmin
    class MyModelAdmin(MultiUploadAdmin):
        # default value of all parameters:
        change_form_template = 'multiupload/change_form.html'
        change_list_template = 'multiupload/change_list.html'
        multiupload_template = 'multiupload/upload.html'
        # if true, enable multiupload on list screen
        # generaly used when the model is the uploaded element
        multiupload_list = True
        # if true enable multiupload on edit screen
        # generaly used when the model is a container for uploaded files
        # eg: gallery
        # can upload files direct inside a gallery.
        multiupload_form = True
        # max allowed filesize for uploads in bytes
        multiupload_maxfilesize = 3 * 2 ** 20 # 3 Mb
        # min allowed filesize for uploads in bytes
        multiupload_minfilesize = 0
        # limit concurrent uploads in order to avoid timeouts (try 6–10 if experiencing problems)
        multiupload_limitconcurrentuploads = None
        # tuple with mimetype accepted
        multiupload_acceptedformats = ( "image/jpeg",
                                        "image/pjpeg",
                                        "image/png",)

        def process_uploaded_file(self, uploaded, object, request):
            '''
            Process uploaded file
            Parameters:
                uploaded: File that was uploaded
                object: parent object where multiupload is
                request: request Object
            Must return a dict with:
            return {
                'url': 'url to download the file',
                'thumbnail_url': 'some url for an image_thumbnail or icon',
                'id': 'id of instance created in this method',
                'name': 'the name of created file',

                # optionals
                "size": "filesize",
                "type": "file content type",
                "delete_type": "POST",
                "error" = 'Error message or jQueryFileUpload Error code'
            }
            '''
            # example:
            title = kwargs.get('title', [''])[0] or uploaded.name
            f = self.model(upload=uploaded, title=title)
            f.save()
            return {
                'url': f.image_thumb(),
                'thumbnail_url': f.image_thumb(),
                'id': f.id,
                'name': f.title
            }

        def delete_file(self, pk, request):
            '''
            Function to delete a file.
            '''
            # This is the default implementation.
            obj = get_object_or_404(self.queryset(request), pk=pk)
            obj.delete()

```

Checkout some full example project in example folder.
Superuser: Login: demo Pass: demo
