**photobooth.py**

An automated photobooth script.

.. image:: http://lewk.org/img/photobooth1.jpg

*Features*

-  Uses gphoto2 to automatically detect your camera
-  When Enter is pressed, it snaps a photo and downloads it locally
-  A Fedora watermark is applied to the bottom right corner of the image
-  The photo is uploaded to a server
-  A QRCode is generated that points to the image URL
-  A TinyURL is generated for the image
-  HTML is generated that shows the image, the QRCode, and TinyURL
-  The page is then displayed in the web browser


*Announcement:* http://lewk.org/blog/photobooth.py

.. image:: http://lewk.org/img/photobooth0.jpg

*Requirements:*

- `python-imaging <http://www.pythonware.com/products/pil>`_
- `qrencode <http://megaui.net/fukuchi/works/qrencode/index.en.html>`_
- `gphoto2 <http://www.gphoto.org/>`_
- `surl <https://launchpad.net/surl>`_

*License*

.. image:: https://www.gnu.org/graphics/gplv3-127x51.png
   :target: https://www.gnu.org/licenses/gpl.txt
