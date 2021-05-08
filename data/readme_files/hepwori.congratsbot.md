# congratsbot

A Twitter bot with the mission of congratulating those being congratulated.

## Notes

This is the code which powers [@congratsbot](https://twitter.com/congratsbot). You can read its birth story at https://medium.com/@isaach/the-birth-of-congratulatron-ba9fb313e543.

It uses the Twitter Streaming API to gather all tweets containing the words 'congrats' or 'congratulations'. It discards those which aren't replies; with the remainder it tallies up which tweets are being replied to with messages of congratulations. When it sees a tweet which has garnered five congratulatory replies it throws in its own congrats (with a few heuristically determined exceptions).

Some things:

- obviously the `reply_count` dictionary grows without limit. In practice the bot will stall (see below) before that becomes an issue. Nonetheless it'll probably offend your sense of properness like it does mine;
- by design the bot shrugs at most exceptions and just moves on. The main priority of the bot is staying connected to the stream and processing messages as best it can;
- we start the bot with a blacklist of users comprising those which have been recently @-replied. Ideally this blacklist would expire; in practice, though, it mostly doesn't matter because of stalls;
- the Twitter stream will occasionally "stall", ie. remain connected but deliver no more messages. I use an external process to monitor this condition and restart the bot as necessary; and finally
- this is the most Python I've ever written in one place. I'm keen to learn about Pythonic idioms I missed, and so much more, but be gentle.

Some ideas:

- this thing obviously generalizes into a "wtf-bot" or a "omg-bot". From my early tinkering these seem harder to get right (require more heuristics) but are perfectly within reach; and
- bot-as-a-service.

## Important

Twitter bots which spend their life @-replying users who aren't following them enjoy a precarious existence on Twitter—this is a behavior pattern which, surprise surprise, looks like spam. If users commonly mark you as spam, or block you, you *will* get suspended. Be respectful, delightful, and fun… and perhaps you won't.
