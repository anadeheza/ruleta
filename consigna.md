
# Problem description

## A brief introduction to the game of roulette in case you're not familiar with it.

The roulette has 37 numbers, from 0 to 36.

From all the possible bets, we'll focus on the so-called simple bets (odd / even, red / black, low / high). There are 18 numbers of each kind: odds and evens need no explanation, lows are numbers between 1 and 18, highs between 19 and 36. Reds and black can be seen here: http://es.wikipedia.org/wiki/Ruleta#mediaviewer/Archivo:Roulette_frz.png

Zero is a special number which isn't even, odd, red, black, high nor low. This means that if you placed one of the bets described above and the outcome is zero, you lose!

In single bets, if you win, the table will pay you back twice as much: this means that if your bet was 10 you'll get 20 back. If you lose, the table takes the money from your bet.

## Now to the problem:

Let's imagine a group of **6 people** go to the casino to play roulette as a team. They all seat in the same table and **each player bets on one type of simple bets**, so that player A bets on red, player B bets on black, player C bets on high, etc.

### For the simulation we'll assume the following:
**Maximum bet on the table is 4000.**
**Minimum bet on the table is 5.**

### Strategy:
Each player has a **notebook** where they keep their bets. At the beginning, the notebook looks like this (we'll call that the initial sequence):
<br>
1 - 2 - 3 - 4

In order to place their **bets** they **add up both ends** of the sequence (in this case 1 + 4 = 5). If they **win**, they **add their winnings (5) to the end**of the sequence, while if they **lose** they **scratch both ends** of the sequence (1 and 4). For the next bet they add both extremes again.

Following with the initial example:

- If a player won, the notebook would look like 1 - 2 - 3 - 4 - 5 (next bet would be 1 + 5 = 6)
- If he lost, the notebook would look like 2 - 3 (next bet would be 2 + 3 = 5)
- If at some point the notebook is empty because he crossed out all the numbers, then he starts over with the initial sequence.
- If at some point he only has one number left, that's his bet (he doesn't have to double it as if he was adding both extremes).
- If the bet he needs to place is out of the table boundaries (max and min), he starts over with the initial sequence.

### Assignment:
Write a program that will simulate these 6 people playing simultaneously on the same table. You'll need to simulate the roulette spin as well. The complete sequence of your program would look something like this:

Player A bets on red
<br>
Player B bets on black
<br>
Player C bets on high
<br>
Player D bets on low
<br>
Player E bets on odd
<br>
Player F bets on even

### Roulette spins
Pay each player according to the roulette outcome
<br>
Start over
<br>
You need to consider that **each player has his own notebook** and their **bets are independent** from one another.
<br>
Your simulation should **spin the roulette 10,000 times** and at the end it should **display** the money **balance** of the **team**. We want to know if they won, lost or broke even.
<br>
For the simulation we'll assume the 6 players have **unlimited money**, so they never stop betting because they have no money left.
<br>
Your program must build and run in Linux. Try to use standard libs so that the code is portable.
Code must be documented.