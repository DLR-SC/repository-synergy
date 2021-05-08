# Overview

Harold and Harold's Code Salon are tools for coordinating software development,
code review, and deployment. They were made for reddit.com's dev team to use
and have grown over the years.

# Development

For reddit employees, you can use the OneVM to develop harold. Enable it with

    vagrant enable-repo harold

and then provision with

    vagrant provision

To test slack communciation, you'll need to generate a Slack API token by going
to

    https://<myslackdomain>.slack.com/apps/manage/custom-integrations

and setting up a "bot" integration. Put the resulting value into the
appropriate field in the `example.ini`.

# Testing

To simulate webhooks firing, use the `tests/fire-webhook` script with payloads
in `tests/webhookpayloads`.

    tests/fire-webhook tests/webhookpayloads/push-multiple-nonsender.request
