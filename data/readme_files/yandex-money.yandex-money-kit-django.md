## yanexmoney-kit-django

Модуль оплаты yanexmoney-kit-django необходим для интеграции с сервисом [Яндекс.Касса](http://kassa.yandex.ru/) на базе фраймворка [Django](https://www.djangoproject.com).

 Доступные платежные методы, если вы работаете как юридические лицо:
* **Банковские карты** -  Visa (включая Electron), MasterCard и Maestro любого банка мира
* **Электронные деньги** - Яндекс.Деньги, WebMoney и QIWI Wallet
* **Наличные** - [Более 170 тысяч пунктов](https://money.yandex.ru/pay/doc.xml?id=526209) оплаты по России
* **Баланс телефона** - Билайн, МегаФон и МТС
* **Интернет банкинг** - Альфа-Клик, Сбербанк Онлайн, MasterPass и Промсвязьбанк
* **Кредитование**

### Минимальные требования:
* Django версии 1.5 или выше
* South версии 1.0 или выше
* lxml версии 3.3.4

### Установка модуля
* Установить пакет:
```
        pip install git+https://github.com/yandex-money/yandex-money-kit-django.git
```
* Добавить ``yandex_money`` в ``settings.INSTALLED_APPS``:
```
        INSTALLED_APPS = (
            ...
            'yandex_money',
            ...
        )
```
* Выполнить синхронизацию с БД:
```
        python manage.py syncdb
        python manage.py migrate # для тех, кто использует south
```
* Добавить в ``urls.py``:
```
        urlpatterns = patterns('',
            # ...
            url(r'^fail-payment/$', TemplateView.as_view(template_name='fail.html'), name='payment_fail'),
            url(r'^success-payment/$', TemplateView.as_view(template_name='success.html'), name='payment_success'),
            url(r'^yandex-money/', include('yandex_money.urls')),
        )
```
* Указать в settings.py следующие параметры:
```
        YANDEX_MONEY_DEBUG = False
        YANDEX_MONEY_SCID = 12345
        YANDEX_MONEY_SHOP_ID = 56789
        YANDEX_MONEY_SHOP_PASSWORD = 'password'
        YANDEX_MONEY_FAIL_URL = 'https://example.com/fail-payment/'
        YANDEX_MONEY_SUCCESS_URL = 'https://example.com/success-payment/'
        # информировать о случаях, когда модуль вернул Яндекс.Кассе ошибку
        YANDEX_MONEY_MAIL_ADMINS_ON_PAYMENT_ERROR = True
```
* Указать в личном кабинете Яндекс.Деньги настройки для приема уведомлений:

* paymentAvisoURL: `https://example.com/yandex-money/aviso/`
* checkURL: `https://example.com/yandex-money/check/`
* failURL: `https://example.com/fail-payment/`
* successURL: `https://example.com/success-payment/`


### Использование
[Полный пример использования](<https://github.com/DrMartiner/django-yandex-money/tree/develop/example>)

* Представление платежной формы:
```
        from django.views.generic import TemplateView
        from yandex_money.forms import PaymentForm
        from yandex_money.models import Payment


        class OrderPage(TemplateView):
            template_name = 'order_page.html'

            def get_context_data(self, **kwargs):
                payment = Payment(order_amount=123)
                payment.save()

                ctx = super(OrderPage, self).get_context_data(**kwargs)
                ctx['form'] = PaymentForm(instance=payment)
                return ctx
```
* Шаблон платежной формы:
```
        <html>
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta charset="utf-8">
            </head>
            <body>
                <div style="border: 1px dotted gray; padding: 15px 15px 0; margin: 30px auto; width: 300px;">
                    <form name="ShopForm" method="POST" action="https://money.yandex.ru/eshop.xml">
                        <ul style="list-style: none;">
                            <li style="margin-bottom: 20px;">
                                Сумма заказа: <b>{{ form.sum.value }}</b>
                            </li>

                            {{ form.as_ul }}

                            <li style="margin-top: 20px;">
                                <input type="submit" value="Оплатить">
                            </li>
                        </ul>
                    </form>
                </div>
            </body>
        </html>
```
* Также вы можете определить logger 'yandex_money':
```
        LOGGING = {
            'version': 1,
            'disable_existing_loggers': True,
            'root': {
                'level': 'INFO',
                'handlers': ['default'],
            },
            'formatters': {
                'simple': {
                    'format': '[%(asctime)s] %(levelname)s: %(message)s',
                    'datefmt': '%d/%m/%Y %H:%M:%S',
                },
            },
            'handlers': {
                'default': {
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': os.path.join(LOGGING_DIR, 'messages.log'),
                    'maxBytes': 1024 * 1024 * 5,
                    'backupCount': 5,
                    'formatter': 'message',
                },
                'yandex_money': {
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',
                    'filename': os.path.join(LOGGING_DIR, 'yandex_money.log'),
                    'maxBytes': 1024 * 1024 * 5,
                    'backupCount': 5,
                    'formatter': 'standard',
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': 'INFO',
                    'propagate': True
                },
                'yandex_money': {
                    'handlers': ['yandex_money'],
                    'level': 'DEBUG',
                    'propagate': False
                },
            }
        }
```
### Лицензионный договор.

Любое использование Вами программы означает полное и безоговорочное принятие Вами условий лицензионного договора, размещенного по адресу https://money.yandex.ru/doc.xml?id=527132 (далее – «Лицензионный договор»). 
Если Вы не принимаете условия Лицензионного договора в полном объёме, Вы не имеете права использовать программу в каких-либо целях.

### Нашли ошибку или у вас есть предложение по улучшению модуля?
Пишите нам cms@yamoney.ru
При обращении необходимо:
* Указать наименование CMS и компонента магазина, а также их версии
* Указать версию платежного модуля (доступна в списке меню `Модули`)
* Описать проблему или предложение
* Приложить снимок экрана (для большей информативности)
