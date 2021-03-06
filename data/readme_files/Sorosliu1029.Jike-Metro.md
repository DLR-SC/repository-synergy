==================
Jike Metro ð
==================

.. image:: https://img.shields.io/travis/Sorosliu1029/Jike-Metro.svg
    :alt: Travis
    :target: https://travis-ci.org/Sorosliu1029/Jike-Metro

.. image:: https://img.shields.io/pypi/v/jike.svg
    :alt: PyPI
    :target: https://pypi.org/project/jike/

.. image:: https://img.shields.io/pypi/l/jike.svg
    :alt: PyPI - License
    :target: https://pypi.org/project/jike/

.. image:: https://img.shields.io/pypi/pyversions/jike.svg
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/jike/

.. image:: https://img.shields.io/pypi/status/jike.svg
    :alt: PyPI - Status
    :target: https://pypi.org/project/jike/

.. image:: https://img.shields.io/github/contributors/Sorosliu1029/Jike-Metro.svg
    :alt: GitHub contributors
    :target: https://github.com/Sorosliu1029/Jike-Metro/graphs/contributors

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
    :alt: Say Thanks
    :target: https://saythanks.io/to/Sorosliu1029

.. image:: https://img.shields.io/github/stars/Sorosliu1029/Jike-Metro.svg?style=social&label=Stars
    :alt: GitHub stars
    :target: https://github.com/Sorosliu1029/Jike-Metro/

Jike Metro ð æ¯å³å»éçå°éå·¥ç¨ï¼æ¨å¨æé«å³åçåºè¡æ¸¸è§æçã

**å®å¨æé**ï¼Jike Metro ð ç®åæ¯å°ä¸å·¥ä½ï¼éå®æ¹ææï¼éæ¶å¯è½ç¿»è½¦ï¼ç»ææ ð ä¹°å°é±¼å¹²å¯ä¿å¹³å®ã

.. image:: https://cdn.ruguoapp.com/Ftub2jUf092k6GYua0DTV8t-PMoR.jpg?imageView2/0/w/2000/h/400/q/50

å¾çæ¥æº: `å³å»ä¹å·å·¥åâææâåå°ä¼ä¼´ä»¬ <https://web.okjike.com/topic/55d6de4660b2719eb447649a/official>`_

Jike Metro ð ç®æä¹è½¦æå
==========================

.. code-block:: python

    >>> c = jike.JikeClient()
    >>> c.get_my_profile()
    User(id='58cf99696a34ae0015b9f5d5', screenName=æå°éç)
    >>> my_collection = c.get_my_collection()
    >>> my_collection[0]
    OfficialMessage(id='55dd572f41904d0e00fc58f8', content=å³å»ææ: åäº«ä¸åªæ¾ç»çç«¥æï¼å·²åéæé¿ï¼)
    >>> news_feed = c.get_news_feed()
    >>> news_feed[0]
    OfficialMessage(id='5ac347a30799810017977041', content=DeepMind åå¸æ°æ¶æ  è®©AI è¾¹ç©æ¸¸æè¾¹å¼ºåå­¦ä¹ )
    >>> ceo = c.get_user_profile(username='82D23B32-CF36-4C59-AD6F-D05E3552CBF3')
    >>> ceo
    User(screenName=ç¦æ)
    >>> c.create_my_post(content='Jike Metro ð released!', link='https://github.com/Sorosliu1029/Jike-Metro')
    True

æ´è¯¦ç»çä¹è½¦æåè¯·ç§»æ­¥ ð `Jike Metro ð ä¹è½¦æå <https://www.0x2beace.me/Jike-Metro/>`_

Jike Metro ð ä¹è½¦ä½éª
======================

Jike Metro ð ç®åæ¯æï¼

- è·åèªå·±çæ¶èï¼æ¥çèªå·±çç¨æ·ä¿¡æ¯
- æµå¼è·åé¦é¡µæ¶æ¯åå¨æ
- è·åæä¸ªç¨æ·çç¨æ·ä¿¡æ¯ãåå¸çå¨æãåå»ºçä¸»é¢ãå³æ³¨çä¸»é¢ãTAå³æ³¨çäººåå³æ³¨TAçäºº
- è·åææ¡æ¶æ¯/å¨æçè¯è®º
- è·åæä¸ªä¸»é¢ä¸çç²¾éåå¹¿åº
- åå¸ä¸ªäººå¨æï¼å¯å¸¦å¾ãå¸¦é¾æ¥ãå¸¦ä¸»é¢ï¼ï¼å é¤ä¸ªäººå¨æ
- ç¹èµãæ¶èãè¯è®ºãè½¬åææ¡æ¶æ¯/å¨æ
- å¨æµè§å¨ä¸­æå¼ææ¡æ¶æ¯çåå§é¾æ¥
- æ ¹æ®å³é®è¯æç´¢ä¸»é¢
- æ ¹æ®å³é®è¯æç´¢èªå·±çæ¶è
- è·åå³å»é¦é¡µçæ¨èå³æ³¨ä¸»é¢åè¡¨ï¼ä¸éäºé¦é¡µæ¾ç¤ºç5ä¸ªï¼

Jike Metro ð ç°å¨æ¯æ Python 3.4-3.6

Jike Metro ð å¥å£
==================

å¯éè¿ pip å®è£ Jike Metro ð

.. code-block:: bash

    $ pip install jike

æ³¨æå®å¨ï¼å°å¿è¡é©¶ï¼ä¸è¦å½±åå¶ä»å³åçåºè¡ã

Jike Metro ð åºç¡è®¾æ½
======================

Jike Metro ð åºäºï¼

- `å³å»Webç <https://web.okjike.com>`_
- `requests <https://github.com/requests/requests>`_
- `qrcode <https://github.com/lincolnloop/python-qrcode>`_
