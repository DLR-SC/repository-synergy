TSP_Animation
=============

The source code for an animation of four algorithms trying to solve a traveling salesman problem

You can find the animation on:

<https://www.youtube.com/watch?v=q6fPk0--eHY>

Given a set of 200 cities four algorithms are used to find the shortest tour
of all 200 cities.  The algorithms are:

1. Random path, start a city and randomly select the next city from the remaining not visited cities until all cities are visited.
2. Greedy, start a city select as next city the unvisited city that is closest to the current city
3. 2-Opt, First create a random tour, and then optimize this with the 2-opt
   algorithm
4. Simulated Annealing. First create a random tour, and then optimize this with 2-opt in combination
   with simualted annealing.


To create the animation you will need python (Version 2) and ffmpeg.

For python you need one additional library (matplotlib) and its dependcies.
You can install it with:

    pip install matplotlib


To create the animation use:

    make .anim
    make

This should create a file called sa.mp4.  This should be playable with vlc.

