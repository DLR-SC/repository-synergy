nhlscrapi: NHL Scraper API
===============================

.. image:: https://badge.fury.io/py/nhlscrapi.svg
    :target: https://badge.fury.io/py/nhlscrapi


All good things ...
-------------------

I wrote this as a way to learn python seemingly forever ago. Back then parsing horrendously structured HTML files from the NHL site was basically the only way to go. No longer.

The NHL's backend API is `public <https://www.kevinsidwar.com/iot/2017/7/1/the-undocumented-nhl-stats-api>`_. Just use that. 

For example, if you put https://statsapi.web.nhl.com/api/v1/teams/1 in your browser you'll get some nice JSON about the NJ Devils. While it seems inexplicable that they'd be the first team anyone would put into their database, it's the NHL. Blame Bettman. Better yet, if you want the game feed for the first game of the 2017-2018 season? Go `here <https://statsapi.web.nhl.com/api/v1/game/2017020001/feed/live>`_.

Best of all, the `nhlapi <https://gitlab.com/dword4/nhlapi>`_ project on GitLab is working to uncover and document the endpoints.

So please, someone just write a nice client for that API.


Purpose
--------

Provide a Python API for accessing NHL game data including play by play, game summaries, player stats et c. The library hides the guts of the NHL website scraping process and encapsulates not only the data gathering, but data output. This project is inspired by the `R <http://www.r-project.org>`_ package *nhlscrapr*, an all around must for NHL analytics geeks and R power users.

nhlscrapi is in the early/initial stages, but will be updated regularly. Currently, the package support most of the game summary reports, but all of the important and essential ones.

Related projects:
  - `nhlscrapr <http://cran.r-project.org/web/packages/nhlscrapr/index.html>`_
  - `py-nhl <https://github.com/wellsoliver/py-nhl>`_

Installation
------------

Getting started is as easy as::

    pip install nhlscrapi

For more information on the setup, see the `PyPi: nhlscrapi <https://pypi.python.org/pypi/nhlscrapi/>`_. The documentation for the package can be found at `nhlscrapi: NHL Scraper API <http://pythonhosted.org/nhlscrapi/>`_.

Usage Example
--------------
Scrape data for game 1226 of 2014, Ottawa vs Pittsburgh.

.. code-block:: python

  from nhlscrapi.games.game import Game, GameKey, GameType
  from nhlscrapi.games.cumstats import Score, ShotCt, Corsi, Fenwick

  season = 2014                                    # 2013-2014 season
  game_num = 1226                                  #
  game_type = GameType.Regular                     # regular season game
  game_key = GameKey(season, game_type, game_num)

  # define stat types that will be counted as the plays are parsed
  cum_stats = {
    'Score': Score(),
    'Shots': ShotCt(),
    'Corsi': Corsi(),
    'Fenwick': Fenwick()
  }
  game = Game(game_key, cum_stats=cum_stats)

  # also http requests and processing are lazy
  # accumulators require play by play info so they parse the RTSS PBP
  print('Final         : {}'.format(game.cum_stats['Score'].total))
  print('Shootout      : {}'.format(game.cum_stats['Score'].shootout.total))
  print('Shots         : {}'.format(game.cum_stats['Shots'].total))
  print('EV Shot Atts  : {}'.format(game.cum_stats['Corsi'].total))
  print('Corsi         : {}'.format(game.cum_stats['Corsi'].share()))
  print('FW Shot Atts  : {}'.format(game.cum_stats['Fenwick'].total))
  print('Fenwick       : {}'.format(game.cum_stats['Fenwick'].share()))

  # http req for roster report
  # only parses the sections related to officials and coaches
  print('\nRefs          : {}'.format(game.refs))
  print('Linesman      : {}'.format(game.linesman))
  print('Coaches')
  print('  Home        : {}'.format(game.home_coach))
  print('  Away        : {}'.format(game.away_coach))

  # scrape all remaining reports
  game.load_all()

Current Release: v0.4.4
------------------------
This is a pre-release and is not stable and fully fit for production. The first full stable release (v1.0.0) will be made available once the framework for all `NHL game reports <http://www.nhl.com/ice/gamestats.htm?fetchKey=20142ALLSATAll&sort=gameDate&viewName=teamRTSSreports>`_ are completed. Currently, Play-by-Play, Home/Away TOI, Roster, Face-off Comparison and Event Summary reports are functional.

License
--------
The NHL Scraper API is a free Python library provided under Apache License version 2.0.

  - Free software: Apache License, v2.0
  - Documentation: `nhlscrapi: NHL Scraper API <http://pythonhosted.org/nhlscrapi/>`_
