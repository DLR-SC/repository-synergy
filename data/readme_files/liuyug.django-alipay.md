=======
alipay
=======
|version| |download|

alipay api for django

testing pass on Django 1.10.5

Install
=======
::

    pip install -r requirements.txt
    pip install django-alipay


Quick start
-----------
.. note::

    create_partner_trade_by_buyer and send_goods_confirm_by_platform have been shutdown by Alipay.

    担保交易：已经被支付宝取消

    即时到账：因个人限制，无法签约即时到账服务，无法调试。

1. Add "alipay" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'alipay.create_direct_pay_by_user.dpn.apps.AlipayDPNConfig',
    )

2. Include the alipay URLconf in your project urls.py like this::

    url(r'^alipay/ptn/', include('alipay.create_partner_trade_by_buyer.ptn.urls')),

3. Run ``python manager.py migrate`` to create the alipay models.

4. Create admin user. ``python manager.py createsuperuser``

5. Start the development server and visit ``http://127.0.0.1:8000/admin/`` to create a poll (you'll need the Admin app enabled).

6. Visit ``http://127.0.0.1:8000/alipay/`` to participate in the poll.

Please see example!!

.. |version| image:: https://img.shields.io/pypi/v/django-alipay.png
    :target: https://pypi.python.org/pypi/django-alipay/
    :alt: Version

.. |download| image:: https://img.shields.io/pypi/dm/django-alipay.png
    :target: https://pypi.python.org/pypi/django-alipay/
    :alt: Downloads

LICENSE
---------
This is a INTERNET PAID code. For SECURITY reason, the company would not like to open their source code. To keep user out of paying danger, I change LICENSE to MIT from GPL.

BTW: You are welcome to submit your open code.
