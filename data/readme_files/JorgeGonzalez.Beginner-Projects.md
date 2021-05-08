# Beginner Projects
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/beginner-projects/Lobby)

A list of projects for beginners.

## Table of Contents
- [Getting Started](#getting-started)
- [Project List](#project-list)
- [Projects](#projects)
- [Solutions](#solutions)
- [Contributing](#contributing)
- [Credits](#credits)

## Getting Started
If you're completely new to programming, you may want to look into a [tutorial](https://www.codecademy.com/learn/python). Before starting, you should already know the basics of programming such as variables, loops, dictionaries, and how to define functions, as well as how to run programs on your own machine.

Each project idea has a basic goal for you to achieve, as well as subgoals that require a bit more thought, but help make your program more interesting. The overall intent for this repository is to serve as a learning resource for everyone and to help transition learners from a beginning level to an intermediate level. In addition, learners are encouraged to contribute their solutions to this repository and thereby learn the basics of Git.

Almost all projects can be completed in any language, but some were specifically written to be completed with Python.

Remember, if you don't know how to do something, Google is your friend.

### Gitter Community
Feel free to join us on our [Gitter channel](https://gitter.im/beginner-projects/Lobby) where we can code together, chat, and get help on just about anything.

## Project List
*Projects are somewhat ordered by increasing difficulty.*
- [99 Bottles](#99-bottles)
- [Armstrong Number](#Armstrong-Number)
- [Magic 8 Ball](#magic-8-ball)
- [Pythagorean Triples Checker](#pythagorean-triples-checker)
- [Rock Paper Scissors Game](#rock-paper-scissors-game)
- [Coin Estimator By Weight](#coin-estimator-by-weight)
- [Mad Libs Story Maker](#mad-libs-story-maker)
- [Change Calculator](#change-calculator)
- [Mean, Median, and Mode](#mean-median-and-mode)
- [Higher Lower Guessing Game](#higher-lower-guessing-game)
- [Multiplication Table](#multiplication-table)
- [Fibonacci Sequence](#fibonacci-sequence)
- [Base Jumper](#base-jumper)
- [Hangman Game](#hangman-game)
- [Menu Calculator](#menu-calculator)
- [Seat Reservation](#seat-reservation)
- [Dice Rolling Simulator](#dice-rolling-simulator)
- [Count and Fix Green Eggs and Ham](#count-and-fix-green-eggs-and-ham)
- [What's My Number?](#whats-my-number)
- [Factors of a Number](#factors-of-a-number)
- [Countdown Clock](#countdown-clock)
- [Turn Based Pokemon Style Game](#turn-based-pokemon-style-game)
- [A Variation of 21](#a-variation-of-21)
- [Compare Recent reddit Karma](#compare-recent-reddit-karma)
- [Watch for New TIL Facts](#watch-for-new-til-facts)
- [Random Wikipedia Article](#random-wikipedia-article)
- [What's the Weather?](#whats-the-weather)
- [Sierpinski Triangle](#sierpinski-triangle)
- [Two Numbers](#two-numbers)
- [Chickens and Rabbits](#chickens-and-rabbits)
- [FLAMES Game](#FLAMES-Game)
- [Pomodoro Timer](#Pomodoro-Timer)
- [Scarne's Dice](#scarnes-dice)
- [GoogleCase](#GoogleCase)
- [Chess](#ChessGame)
- [Movie of the day](#movie-of-the-day)
- [Website Scraper / Analyzer](#website-scraper--analyzer)
- [Palidrome](#Palindrome)

## Projects

### 99 Bottles
- Create a program that prints out every line to the song "99 bottles of beer on the wall."
- Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
- Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
- Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

### Armstrong Number
- Learn about armstrong numbers [here](https://en.wikipedia.org/wiki/Narcissistic_number).
- Define a function that allows the user to check whether a given number is armstrong number or not.
- Hint: To do this, first determine the number of digits of the given number. Call that n. Then take every digit in the number and raise it to the nth power. Add them, and if your answer is the original number then it is an Armstrong number.
- Example: Take 1634. Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634. So 1634 is an Armstrong number.
- Tip: All single digit numbers are Armstrong numbers.


### Magic 8 Ball
- Simulate a magic 8-ball.
- Allow the user to enter their question.
- Display an in progress message(i.e. "thinking").
- Create 20 responses, and show a random response.
- Allow the user to ask another question or quit.
- Bonus:
  - Add a gui.
  - It must have box for users to enter the question.
  - It must have at least 4 buttons:
    - ask
    - clear (the text box)
    - play again
    - quit (this must close the window)

### Pythagorean Triples Checker
- If you do not know how basic right triangles work, or what a Pythagorean Triple is read these articles on Wikipedia[¹](https://en.wikipedia.org/wiki/Right_triangle) [²](https://en.wikipedia.org/wiki/Pythagorean_triple).
- Allows the user to input the sides of any triangle in any order.
- Return whether the triangle is a Pythagorean Triple or not.
- Loop the program so the user can use it more than once without having to restart the program.

### Rock Paper Scissors Game
- Create a rock-paper-scissors game.
- Ask the player to pick rock, paper or scissors.
- Have the computer chose its move.
- Compare the choices and decide who wins.
- Print the results.
- Subgoals:
  - Give the player the option to play again.
  - Keep a record of the score (e.g. Player: 3 / Computer: 6).

### Coin Estimator By Weight
When some people receive change after shopping, they put it into a container and let it add up over time. Once they fill up the container, they'll roll them up in [coin wrappers](https://en.wikipedia.org/wiki/Coin_wrapper) which can then be traded in at a bank for what they are worth. While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you will need. Instead of counting how many coins you have, it's easier to separate all of your coins, weigh them, and then estimate how many of each type you have and then how many wrappers you'll need.
For example, if you weigh all of your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is 2.268g) and you would be able to fill 11 dime wrappers.

Here is the [weight of each coin](https://en.wikipedia.org/wiki/Coins_of_the_United_States_dollar#Coins_in_circulation) and [how many fit inside each type of wrapper](https://en.wikipedia.org/wiki/Coin_wrapper#Amount_in_a_roll_in_the_United_States).
- Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
- Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total value of all of their money.
- Subgoals:
  - Round all numbers printed out to the nearest whole number.
  - Allow the user to select whether they want to submit the weight in either grams or pounds.

### Mad Libs Story Maker
Ever played [Mad Libs](https://en.wikipedia.org/wiki/Mad_Libs)? If you haven't, here are the basics:

"Mad Libs consist of a book that has a short story on each page with many key words replaced with blanks. Beneath each blank is specified a lexical or other category, such as "noun," "verb," "place," or "part of the body." One player asks the other players, in turn, to contribute some word for the specified type for each blank, but without revealing the context for that word. Finally, the completed story is read aloud. The result is usually comic, surreal and somewhat nonsensical."

- Create a Mad Libs style game, where the program asks the user for certain types of words, and then prints out a story with the words that the user inputted.
- The story doesn't have to be too long, but it should have some sort of story line.
- Tip: it's easiest to write out a quick story on a piece of paper or a word document, and then go back through and see which words the user should be able to change.
- Subgoals:
  - If the user has to put in a name, change the first letter to a capital letter.
  - Change the word "a" to "an" when the next word in the sentence begins with a vowel.

### Change Calculator
- Imagine that your friend is a cashier, but has a hard time counting back change to customers.
- Create a program that allows him to input a certain amount of change, and then print how how many quarters, dimes, nickels, and pennies are needed to make up the amount needed.
Example: if he inputs 1.47, the program will say that he needs 5 quarters, 2 dimes, 0 nickels, and 2 pennies.
- Subgoals:
  - So your friend doesn't have to calculate how much change is needed, allow him to type in the amount of money given to him and the price of the item. The program should then tell him the amount of each coin he needs like usual.
  - To make the program even easier to use, loop the program back to the top so your friend can continue to use the program without having to close and open it every time he needs to count change.

### Mean, Median, and Mode
In a set of numbers, the mean is the average, the mode is the number that occurs the most, and if you rearrange all the numbers numerically, the median is the number in the middle.
- Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.
- Subgoals
  - In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to.
  - If there is an even number of numbers in the list, return both numbers that could be considered the median.
  - If there are multiple modes, return all of them.

### Higher Lower Guessing Game
- Create a simple game where the computer randomly selects a number between 1 and 100 and the user has to guess what the number is.
- After every guess, the computer should tell the user if the guess is higher or lower than the answer.
- When the user guesses the correct number, print out a congratulatory message.
- Subgoals:
  - Add an introductory message that explains to the user how to play your game.
  - In addition to the congratulatory message at the end of the game, also print out how many guesses were taken before the user arrived at the correct answer.
  - At the end of the game, allow the user to decide if they want to play again (without having to restart the program).

### Multiplication Table
- Create a program that prints out a multiplication table for the numbers 1 through 9.
- It should include the numbers 1 through 9 on the top and left axises, and it should be relatively easy to find the product of two numbers. Do not simply write out every line manually (ie print('7 14 21 28 35 49 56 63') ).
- Subgoals:
  - As your products get larger, your columns will start to get crooked from the number of characters on each line. Clean up your table by evenly spacing columns so it is very easy to find the product of two numbers.
  - Allow the user to choose a number to change the size of the table (so if they type in 12, the table printed out should be a 12x12 multiplication table).

### Fibonacci Sequence
If you do not know about the Fibonacci Sequence, read about it [here](https://en.wikipedia.org/wiki/Fibonacci_number).
- Define a function that allows the user to find the value of the nth term in the sequence.
- To make sure you've written your function correctly, test the first 10 numbers of the sequence.
- You can assume either that the first two terms are 0 and 1 or that they are both 1.
- There are two methods you can employ to solve the problem. One way is to solve it using a loop and the other way is to use recursion.
- Try implementing a solution using both methods.

### Base Jumper
- Create a program that converts an integer to the specified base.
- The program should ask for 3 inputs. The number to convert. The base the number is in. And the base to convert the number to.
- The program should accept a base that is in the range of 2 to 16 inclusive.
- Display the result to the user and ask if they want to exit or convert another number.
- Subgoals:
  - Do not display leading zero's in the result.
  - Validate that the number entered is valid for the specified base

### Hangman Game
- Create a program that selects a random word and then allows the user to guess it in a game of hangman.
- Like the real game, there should be blank spots for each letter in the word, and a part of the body should be added each time the user guesses a letter than is not in the answer.
- You may choose how many wrong turns the user can make until the game ends.
- Subgoals:
  - If the user loses, print out the word at the end of the game.
  - Create a "give up" option.

### Menu Calculator
Imagine you have started up a small restaurant and are trying to make it easier to take and calculate orders. Since your restaurant only sells 9 different items, you assign each one to a number, as shown below.
- 1. Chicken Strips - $3.50
- 2. French Fries - $2.50
- 3. Hamburger - $4.00
- 4. Hotdog - $3.50
- 5. Large Drink - $1.75
- 6. Medium Drink - $1.50
- 7. Milk Shake - $2.25
- 8. Salad - $3.75
- 9. Small Drink - $1.25

To quickly take orders, your program should allow the user to type in a string of numbers and then it should calculate the cost of the order. For example, if one large drink, two small drinks, two hamburgers, one hotdog, and a salad are ordered, the user should type in 5993348, and the program should say that it costs $19.50. Also, make sure that the program loops so the user can take multiple orders without having to restart the program each time.
- Subgoals:
  - If you decide to, print out the items and prices every time before the user types in an order.
  - Once the user has entered an order, print out how many of each item have been ordered, as well as the total price.
  - If an item was not ordered at all, then it should not show up.

### Seat Reservation
If you've ever been in a concert, you are aware that you buy tickets to be able to reserve a seat inside a stadium. The seat you will be on will have a specific number or code that would enable you to know exactly how far or how close you are to the stage. 

Note: if you are kind of uncomfortable with lists, here's a [reference](https://www.w3schools.com/python/python_lists.asp) to get you started. 

- Create a simple seat reservation program
- Create a list that would store dashes '-' as a symbol that the seat is still available to take.
- Define a function that would loop over the list and print out the seats horizontally or in a 3 x 3 position. Refer to [this](https://image.shutterstock.com/image-vector/stadium-chairs-vector-icon-arenabench-260nw-1056480272.jpg) image for reference.
- Define a second function that would check if the seats are occupied. This should check if the list contains "X" in each element, which is the symbol that we will use if the seat is taken that you will store in a variable. If the variable is equal to 9 (the total number of seats), return True (and break from the loop), and False if not.
- Create a loop that would have to (1) ask the user for the number of seat he would want to reserve, (2) print out the chairs, (3) check if all the seats are occupied and (4) ask the user now if he/she wants to reserve again.

### Dice Rolling Simulator
By using the random module, Python can do things like pseudo-random number generation.
- Allow the user to input the amount of sides on a dice and how many times it should be rolled.
- Your program should simulate dice rolls and keep track of how many times each number comes up (this does not have to be displayed).
- Finally, print out how many times each number came up.
- Subgoals:
  - Adjust your program so that if the user does not type in a number when they need to, the program will keep prompting them to type in a real number until they do so.
  - Put the program into a loop so that the user can continue to simulate dice rolls without having to restart the entire program.
  - In addition to printing out how many times each side appeared, also print out the percentage it appeared. If you can, round the percentage to 4 digits total OR two decimal places.
- Bonus:
  - You are about to play a board game, but you realize you don't have any dice. Fortunately you have this program.
  - 1. Create a program that opens a new window and draws 2 six-sided dice
  - 2. Allow the user to quit, or roll again
  - Allow the user to select the number of dice to be drawn on screen(1-4) 2. Add up the total of the dice and display it

### Count and Fix Green Eggs and Ham
Some of you may remember the Dr. Sues story "Green Eggs and Ham". For those of you that don't remember it or have never heard of it, [here](http://pastebin.com/XMY48CnN) is the story. However, there is a problem with the story I gave you - every time the word I is used, it is lowercase.
Because of this problem, your job is to do the following:
- Copy the story I gave you into a regular text file.
- Create a program that reads through the story and makes the letter i uppercase any time it should be. (Make sure to change it when it's used in sam-I-am's name too.)
- Have your program make a new file, and have it write out the story correctly.
- Print out how many errors were corrected.
- When you're finished, you should have corrected [this many](https://i.imgur.com/GRkj3yz.jpg) errors.

### Whats My Number?
Between 1 and 1000, there is only 1 number that meets the following criteria:
- The number has two or more digits.
- The number is prime.
- The number does NOT contain a 1 or 7 in it.
- The sum of all of the digits is less than or equal to 10.
- The first two digits add up to be odd.
- The second to last digit is even and greater than 1.
- The last digit is equal to how many digits are in the number.

To find out if you have the correct number, click [here](https://i.imgur.com/jbz4nJ4.jpg).

### Factors of a Number
- Define a function that creates a list of all the numbers that are factors of the user's number.
- For example, if the function is called factor, `factor(36)` should return `[1, 2, 3, 4, 6, 9, 12, 18, 36]`.
- The numbers in your list should be sorted from least to greatest, and 1 and the original number should be included.
- Remember to consider negative numbers as well as 0.
- Bonus:
  - Have the program print the factors of the users number in a comma separated string, without a comma after the last number, and without the brackets of a Python list.
  - If the user's number is prime, note it.

### Countdown Clock
- Create a program that allows the user to choose a time and date, and then prints out a message at given intervals (such as every second) that tells the user how much longer there is until the selected time.
- Subgoals:
  - If the selected time has already passed, have the program tell the user to start over.
  - If your program asks for the year, month, day, hour, etc. separately, allow the user to be able to type in either the month name or its number.
  - TIP: Making use of built in modules such as time and datetime can change this project from a nightmare into a much simpler task.

### Turn Based Pokemon Style Game
- Write a simple game that allows the user and the computer to take turns selecting moves to use against each other.
- Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:
  - The first move should do moderate damage and has a small range (such as 18-25).
  - The second move should have a large range of damage and can deal high or low damage (such as 10-35).
  - The third move should heal whoever casts it a moderate amount, similar to the first move.
- After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. Once the user or the computer's health reaches 0, the game should end.
- Subgoals:
  - When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
  - When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
  - Give each move a name.

### A Variation of 21
If you do not know how 21 (AKA Blackjack) is played, reading the first couple of paragraphs of [this](https://en.wikipedia.org/wiki/Blackjack) wikipedia article may be beneficial.

In this project, you will make a game similar to Blackjack. In this version:
- There is only one player.
- There are two types of scores: the game score and the round score.
- The game score will begin at 100, and the game will last for five rounds.
- At the beginning of the round, the player is given two random cards from a deck and they will be added together to make the player's round score.
- From here, the player has two options - draw another card to try to get their round score closer to 21, or they can end the round.
- The player can draw as many cards as they want until they end the round or their round score exceeds 21.
- At the end of the round, the difference between 21 and the round score is subtracted from the game score, and then the next round begins. After the five rounds, the player is given their total score and the game is over.
---Other Information About The Game---
- Aces are only worth 1.
- If a player busts, 21 is subtracted from their total score.
- All face cards are worth 10.
- So the point of your program is to allow the user to play the game described above.
- Subgoals:
  - At the beginning of each round, print the round number (1 to 5).
  - Since this is a text base game, tell the user what is happening. For example, tell him/her when he/she draws a card, the name of the card, when they bust, etc.
  - Create a ranking system at the end of the game and tell the user their rank. For example, if the player finishes with 50-59 points they get an F, 60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
  - At the end of each round, print out the user's total score.
  - This may be the hardest part of the project, depending on how you wrote it. Make sure the deck has 4 of each type of card, and then remove cards as they are drawn. At the end of each round, make the deck have all of the cards again.

### Compare Recent reddit Karma
Since we're all redditors here, let's make something dealing with reddit. If you go to a user's profile and add .json to the end of it, you can get the all sorts of Json data about the user (think of Json as a giant dictionary of smaller dictionaries and lists). For example, if I go to my own profile and view it's Json data, it would look like this[1]. At first it might look intimidating, but if you break it down, you can see it's just one giant dictionary with all sorts of information about my latest posts.
- Create a program that gets information about two different users, and then sees whose most recent post received the most karma.
- The program should then print out which user received more karma, and what the difference was.
- This is a pretty open project, so I encourage you to take it further by adding more features if you find it interesting.
- Remember - Elements in a list are referenced by their index numbers while entries in a dictionary are referenced by their keys.
- Subgoals:
  - Allow the user to put in the name of two different users when the program first begins.
  - If one of the names of the users does not exist (because of a spelling error), print out a message saying so.
  - Allow the user to keep comparing other users until the program is closed.
  - Display the amount of upvotes and downvotes each user received for their posts.
  - Not sure how to turn json data into usable python data? Check [this](http://www.pythonforbeginners.com/python-on-the-web/parse-json-objects-in-python/) out.

### Watch for new TIL facts
If you finished the previous [project](https://github.com/alfredmuffin/Beginner-Projects#compare-recent-reddit-karma) which compared the karma of two new comments, hopefully you learned a thing or two about receiving data from Reddit's API. Now you're going to take this a step further, and even have the opportunity to make a basic twitter bot.
- Create a program that receives data from the [/r/todayilearned](https://reddit.com/r/todayilearned) subreddit, and looks for new facts that have been posted.
- Each time the program comes across a new fact, the fact should be printed into the command line. However, phrases like "TIL ", "TIL that", etc should be removed so the only thing that is printed is the fact.

[New TIL API data here](https://www.reddit.com/r/todayilearned/new/.json)

There are a couple things to note about this since you'll more than likely be using a loop to check for new posts. According to Reddit's [API Access Rules Page](https://github.com/reddit/reddit/wiki/API), the API pages are only updated once every thirty seconds, so you'll have to have your code pause for at least thirty seconds before it tries to find more posts. Secondly, if for some reason you decide to try to get data sooner than every thirty seconds, make sure to not send more than thirty requests per minute. That is the maximum you are allowed to do.

There is actually a lot you can do once your program starts receiving facts. Instead of simply printing the facts, here are some ideas for what you can do with them. If you currently do not feel like you can accomplish these ideas, feel free to come back later when you have more experience.
- Print the link to the source of the fact too.
- Try to further clean up the fact by adding punctuation to the end if it is missing, capitalize the first word, etc.
- Write the facts to a separate text file so you end up with a giant compilation of random facts.
- Create a bot that posts the facts to twitter. This may sound hard, but it's actually pretty simple by using the [Python Twitter Tools](https://pypi.python.org/pypi/twitter) module and following the guide posted [here](https://wilsonericn.wordpress.com/2011/08/22/tweeting-in-python-the-easy-way/).
- Remember, the maximum amount of characters you can use in a tweet is only 140, so you'll have to filter out facts that are longer than that.
- By now you should be pretty familiar with python, so if you get ideas for improving your program, go for it!

### Random Wikipedia Article
If you've been to Wikipedia, you may have noticed that there is a link to a random article on the left side of the screen. While it can be fun to see what article you get taken to, sometimes it would be nice to see the name of the article so you can skip it if it sounds boring. Luckily, Wikipedia has an API that allows us to do so [Click here](https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json).
However, there is a dilemma. Since Wikipedia has articles about topics from all over the world, some of them have special characters in the title. For example, the article about the spanish painter [Erasto Cortés Juárez](https://en.wikipedia.org/wiki/Erasto_Cort%C3%A9s_Ju%C3%A1rez) has é and á in it. If you look at this specific article's [API](https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids=39608394&inprop=url&format=json), you will see that the title is "Erasto Cort\u00e9s Ju\u00e1rez" and that the \u00e9 and \u00e1 are replacing the two previously mentioned letters. (For information about what this is, start by checking out the first half of [this page](https://docs.python.org/2/howto/unicode.html) in the documentation). To make your program work, you're going to have to handle this problem somehow.
- Create a program that pulls titles from the official Wikipedia API and then asks the user one by one if he or she would like to read about that article.
- Example:
  - If the first title is Reddit, then the program should ask something along the lines of "Would you like to read about Reddit?" If the user says yes, then the program should open up the article for the user to read.
  - HINT: Click [here](https://en.wikipedia.org/wiki?curid=39608394) to see how the article's ID can be used to access the actual article.
- Subgoals:
  - As mentioned before, do something about the possibility of unicode appearing in the title.
  - Whether you want your program to simply filter out these articles or you want to actually turn the codes into readable characters, that's up to you.
  - Make the program pause once the user has selected an article to read, and allow him or her to continue browsing different article titles once finished reading.
  - Allow the user to simply press ENTER to be asked about a new article.

### Whats the Weather?
If you would like to know the basics of what an API is, check out [this](http://www.reddit.com/r/explainlikeimfive/comments/qowts/eli5_what_is_api/c3z9kok) post by iamapizza.
- Create a program that pulls data from OpenWeatherMap.org and prints out information about the current weather, such as the high, the low, and the amount of rain for wherever you live.
- Subgoals:
  - Print out data for the next 5-7 days so you have a 5 day/week long forecast.
  - Print the data to another file that you can open up and view at, instead of viewing the information in the command line.
  - If you know html, write a file that you can print information to so that your project is more interesting. Here is an example of the results from what I threw together.[3]
- Tips:
  - APIs that are in Json are essentially lists and dictionaries. Remember that to reference something in a list, you must refer to it by what number element it is in the list, and to reference a key in a dictionary, you must refer to it by it's name.
  - Don't like Celsius? Add &units=imperial to the end of the URL of the API to receive your data in Fahrenheit.

### Sierpinski Triangle

The [Sierpinski triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle) (also with the original orthography Sierpinski), also called the Sierpinski gasket or the Sierpinski Sieve, is a fractal and attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. Originally constructed as a curve, this is one of the basic examples of self-similar sets, i.e., it is a mathematically generated pattern that can be reproducible at any magnification or reduction. It is named after the Polish mathematician _Waclaw Sierpinski_, but appeared as a decorative pattern many centuries prior to the work of Sierpinski.

Task in hand :

- create and visualize a fractal generator that forms a standard ***sierpinski triangle***.
- perform this using recursive calls.

- Subgoals :
  - Also accept ***depth*** for which the fractal should be generated.

### Two Numbers

Given an array of integers, return indices of the ***two numbers*** such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```
### Chickens and Rabbits

Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.

### FLAMES Game

Write a program which implements Flames.

Flames is an interesting game that people play to learn about their relationships. Flames is named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, and Siblings. It is a popular game among young people, especially those beginning to explore the world of crushes. Learn more about Flames [here](https://medium.com/@ritwika285/how-to-play-flames-game-890edc7bf3d) or [here](https://www.wikihow.com/Play-%22Flame%22)

### Pomodoro Timer
Create a Pomodoro Timer.

Pomodoro Timer is a time management method. The technique uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. These intervals are named pomodoros, the plural in English of the Italian word pomodoro (tomato), after the tomato-shaped kitchen timer that Cirillo used as a university student.
There are six steps in the original technique:

Decide on the task to be done.
Set the pomodoro timer (traditionally to 25 minutes).
Work on the task.
End work when the timer rings and put a checkmark on a piece of paper.
If you have fewer than four checkmarks, take a short break (35 minutes), then go to step 2.
After four pomodoros, take a longer break (1530 minutes), reset your checkmark count to zero, then go to step 1.
to know more about Pomodoro Timer [click here](https://en.wikipedia.org/wiki/Pomodoro_Technique)

### Scarne's Dice

Turn-based dice game where players score points by rolling a die and then: if they roll a 1, score no points and lose their turn, if they roll a 2 to 6: add the rolled value to their points choose to either reroll or keep their score and end their turn. The winner is the first player that reaches (or exceeds) 100 points.


### GoogleCase

- Its a game which allows you to play with english sentences.
- User will enter a sentence in any format.(uppercase or lowercase or a mix of both)
- Program must convert the given sentence in google case .What is a google case style of sentence?[know_about_it_here:]( It is a style of         writing where we replace all lower case letters into upper case letters leaving the initial of all the words).
- Subgoals:
    - Program must then convert the given sentence in camel case.To know more about camel case 
    [click_here](https://en.wikipedia.org/wiki/Camel_case)
    - Sentence can be entered with any number of spaces.

Hint: If you are dealing with languages such as ***c*** then consider the sentences as the char array.


### ChessGame

- Chess is a game as old as time, and has always followed the same rules (deviations aside). The logic of chess, however, matches up very nicely with the same logic you would use to program a game. Additionally, Chess makes for a fantastic starter piecepun intendedtowards a programming career.
- Youll start by mapping out both your board and your pieces. Then, youll go on to giving specific movements for your pieces. From brainstorm to final product, youll be forced to think of chess as less of a physical game and more of data-driven mental gymnastic! Click on the video above to begin learning how to maneuver your way through creating your very own chess program (and how to modify it to create your own version of chess).


### Movie of the day

- The app makes use of [OMDb REST API](https://www.omdbapi.com/) in order to fetch a random movie
- Every time the user opens the app, the API gets queried in order to fetch the random movie
- The app can also store (in the browser cache or the phone local storage) which movies have already been
shown to the user so that it can exclude them from the recommendation sub-system.


### Website Scraper / Analyzer 

- Make an app that scrapes the content of a website (it's produced HTML code)
- The app can then check for the absence of important HTML tags for SEO,
missing alt tags on images, and whether the page has SEO meta tags
- The app can be made in various languages that support web scraping (or have a library to
do so), like Python and Java.
- Then the app can give/subtract points and create an overall score.
- You will learn: 
    - How a web scraper works
    - How to traverse the HTML DOM and select elements
    - What are the important SEO tags and techniques in a web page


### Palidrome

- Palindrome means anything(here numbers) that reads the same backwards as forwards.
- Write a program to check if a number is a palindrome or not.
- For example 12321 is a palindrome since it reads the same forward and backwards. 

   

## Solutions
- [aekanshd](https://github.com/aekanshd/beginner-projects/tree/master/solutions/python)
- [Everstalk](https://github.com/Everstalk/BP)
- [NickSchmiek](https://github.com/NickSchimek/Python-Beginner-Projects)
- [luangthomas](https://github.com/luongthomas/Python-Mini-Projects)
- [sumedhpd](https://github.com/sumedhpb/Beginner_project_solutions)
- [hilkenbremen](https://github.com/hilkenbremen/beginner-projects)
- [zakaer](https://github.com/zakaer/problem-solutions-)
- [anuragkumarak95](https://github.com/anuragkumarak95/MyPython)
- [AnanyaTyagi](https://github.com/AnanyaTyagi/BeginnerProjects)
- [aviral36](https://github.com/aviral36/BeginnerProjects)
- [avantikasharma](https://github.com/avantikasharma/beg_project)
- [mattcarmody](https://github.com/mattcarmody/r-Beginner-Projects)
- [ayseenver](https://github.com/ayseenver/BeginnerCPP)
- [sdmaes18](https://github.com/sdmaes18/Beginner)
- [jclane](https://github.com/jclane/beginner-project-solutions)
- [uityh](https://github.com/uityh/Beginner-Project-Solutions)
- [Sudz](https://github.com/sudz123/beginner_project_solutions/tree/master)
- [MKJM2](https://github.com/MKJM2/beginner-project-solutions/tree/master)
- [chuckytah](https://github.com/chuckytah/beginner-projects)
- [Nikhil](https://github.com/imsnik/project-solution)
- [Brad135971](https://github.com/Brad135971/beginner-project-solutions)
- [spiraldancer](https://github.com/spiraldancer/beginner-project-solutions)
- [parthkandpal](https://github.com/parthkandpal/beginner-project-solutions)
- [mark-quinn](https://github.com/mark-quinn/random-but-useful-ruby-programs)
- [Vishnu-Kaladharan](https://github.com/Vishnu-Kaladharan/beginner-project-solutions)
- [Helkat](https://github.com/Helkat/beginner-project-solutions)
- [My3bka](https://github.com/My3bka/beginner-project-solutions)
- [vishal-vardhan](https://github.com/vishal-vardhan/beginner-project.git)
- [hc65100](https://github.com/Hc165100/sample-project-solutions.git)
- [areetaw](https://github.com/areetaw/beginner-projects-solutionst)
- [madelinecodes](https://github.com/madelinecodes/beginner-projects)
- [Recandi](https://github.com/Recandi/rust-beginner-projects)
- [tmug94](https://github.com/tmug94/beginner_project_solutions)
- [oscarada87](https://github.com/oscarada87/beginner-project-solutions)
- [jelenam86](https://github.com/jelenam86/SolutionsBeginnerProjects)
- [vpatyal](https://github.com/vpatyal/beginner-projects-solutions)
- [zamerman](https://github.com/zamerman/beginner-projects-solutions)
- [karthik](https://github.com/chkarthik257/beginner-project-solutions)
- [sanveg-rane](https://github.com/sanveg-rane-13/begineer-project-solutions)
- [sanveg-rane](https://github.com/sanveg-rane-13/begineer-project-solutions)
- [Ankit-Gupta](https://github.com/i-ankit25/begineer-project-solutions)
- [vishaldhull09](https://github.com/vishaldhull09/beginner-project-solution)
- [vishaldhull09](https://github.com/vishaldhull09/beginner-project-solution)
- [007vedant](https://github.com/007vedant/beginner-project-solutions)
- [mgokayb](https://github.com/mgokayb/beginnerpythonprojects)
- [anil-goudar](https://github.com/anil-goudar/beginner-project-solutions.git)
- [breindy](https://github.com/breindy/99bottles-soln)
- [marsmccrann04](https://github.com/marsmccrann04/beginner-project-solutions)
- [sankarsh98](https://github.com/sankarsh98/beginner-project-solutions)
- [SiddhantJain15](https://github.com/SiddhantJain15/beginner-projects-solutions)
- [crosbymichael1](https://github.com/crosbymichael1/beginner-project-solutions)
- [oakhtar147](https://github.com/oakhtar147/beginner-project-solutions)
- [Darepapi](https://github.com/Darepapi/beginners-python-solutions)
- [githubman2718](https://github.com/githubman2718/beginner-project-solutions)
- [rivindu1289](https://github.com/rivindu1289/beginner-python-solutions)
- [lsiepman](https://github.com/lsiepman/BeginnerProjectSolutions)

## Contributing
Contributing to this repository in any way is encouraged.

Some ways to contribute are:
- Adding solutions
- Adding new projects to the project list
- Editing the README

### Contributing Solutions
- Create a new repository called `beginner-project-solutions` (or some variation thereof).
- Add at least one project solution to that repository.
- Add a link to your new repository at the end of the list in the [Solutions](#solutions) section of this README with your GitHub username.

## Credits
Most of these project ideas were originally created on [reddit](https://reddit.com/r/beginnerprojects) where the original links are officially maintained [here](https://docs.google.com/document/d/1TyqD2_oDtiQIh_Y55J5RfeA91JJECc97xYIKM112H9I/edit?usp=sharing). The projects in this repository that are not in that list have been added by this project's contributors.
