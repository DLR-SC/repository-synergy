Reinforcement Learning in Tic-Tac-Toe
=====================================

Reference implementation of the Tic-Tac-Toe value function learning agent described in Chapter 1 of 
"Reinforcement Learning: An Introduction" by Sutton and Barto. The agent contains a lookup table that
maps states to values, where initial values are 1 for a win, 0 for a draw or loss, and 0.5 otherwise.
At every move, the agent chooses either the maximum-value move (greedy) or, with some probability
epsilon, a random move (exploratory); by default epsilon=0.1. The agent updates its value function 
(the lookup table) after every greedy move, following the equation:

    V(s) <- V(s) + alpha * [ V(s') - V(s) ]

This particular implementation addresses the question posed in Exercise 1.1:
    
    What would happen if the RL agent taught itself via self-play?

The result is that the agent learns only how to maximize its own potential payoff, without consideration
for whether it is playing to a win or a draw. Even more to the point, the agent learns a myopic strategy
where it basically has a single path that it wants to take to reach a winning state. If the path is blocked
by the opponent, the values will then usually all become 0.5 and the player is effectively moving randomly.

Note that if you use a loss value of -1, then the agent learns to play the optimal strategy in the minimax
sense.

License
-------
Created by Wesley Tansey

1/21/2013

Code released under the MIT license.