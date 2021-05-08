slouch
======

*[not actively supported outside of internal Venmo usage]*

Slouch is a lightweight Python framework for building cli-inspired Slack bots.

Here's an example bot built with Slouch:

.. code-block:: python

    from slouch import Bot, help

    class PingBot(Bot):
        pass

    @PingBot.command
    def pingme(opts, bot, event):
        """Usage: pingme [--message=<message>]

        Respond with an at-mention to the sender.

        Pass _message_ to include a message in the response.
        """

        sender_slack_id = event['user']
        message = opts['<message>']
        response = ""

        if message is not None:
            response = message

        return "<@%s> %s" % (sender_slack_id, response)

And here's a test for that bot:

.. code-block:: python

    from slouch import testing

    class TestPingBot(CommandTestCase):

        bot_class = PingBot

        def test_ping(self):
            response = self.send_message('pingme', user='123')
            self.assertEqual(response, '<@123> ')



Install with ``pip install slouch``.
Run tests with ``py.test tests``.

For more details, check out the docs at https://slouch.readthedocs.io or see a `full example bot <https://github.com/venmo/slouch/blob/master/example.py>`__.
