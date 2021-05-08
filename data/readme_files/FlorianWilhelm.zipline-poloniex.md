=======================
Zipline Poloniex Bundle
=======================

**UNMAINTAINED: This project is no longer actively developed. If you are interested in taking over please send me a message.**

Poloniex data bundle for zipline_, the pythonic algorithmic trading library.


Description
===========

Just install the data bundle with pip::

    pip install zipline-poloniex

and create a file ``$HOME/.zipline/extension.py`` calling zipline's register_ function.
The ``create_bundle`` function returns the necessary ingest function for ``register``.
Use the ``Pairs`` record for common US-Dollar to crypto-currency pairs.


Alternatively, you can clone this repository and install with pip::

    git clone https://github.com/FlorianWilhelm/zipline-poloniex.git
    cd zipline-poloniex
    pip install -e .

Example
=======

1) Add following content to ``$HOME/.zipline/extension.py``:

.. code:: python

    import pandas as pd
    from zipline_poloniex import create_bundle, Pairs, register

    # adjust the following lines to your needs
    start_session = pd.Timestamp('2016-01-01', tz='utc')
    end_session = pd.Timestamp('2016-12-31', tz='utc')
    assets = [Pairs.usdt_eth]

    register(
        'poloniex',
        create_bundle(
            assets,
            start_session,
            end_session,
        ),
        calendar_name='POLONIEX',
        minutes_per_day=24*60,
        start_session=start_session,
        end_session=end_session
    )

2) Ingest the data with::

    zipline ingest -b poloniex

3) Create your trading algorithm, e.g. ``my_algorithm.py`` with:

.. code:: python

    import logging

    from zipline.api import order, record, symbol
    from zipline_poloniex.utils import setup_logging

    __author__ = "Florian Wilhelm"
    __copyright__ = "Florian Wilhelm"
    __license__ = "new-bsd"

    # setup logging and all
    setup_logging(logging.INFO)
    _logger = logging.getLogger(__name__)
    _logger.info("Dummy agent loaded")


    def initialize(context):
        _logger.info("Initializing agent...")
        # There seems no "nice" way to set the emission rate to minute
        context.sim_params._emission_rate = 'minute'


    def handle_data(context, data):
        _logger.debug("Handling data...")
        order(symbol('ETH'), 10)
        record(ETH=data.current(symbol('ETH'), 'price'))

4) Run your algorithm in ``my_algorithm.py`` with::

    zipline run -f ./my_algorithm.py -s 2016-01-01 -e 2016-12-31 -o results.pickle --data-frequency minute -b poloniex

5) Analyze the performance by reading ``results.pickle`` with the help of Pandas.


Note
====

This project has been set up using PyScaffold 2.5.7. For details and usage
information on PyScaffold see http://pyscaffold.readthedocs.org/.

.. _register: http://www.zipline.io/appendix.html?highlight=register#zipline.data.bundles.register
.. _zipline: http://www.zipline.io/
