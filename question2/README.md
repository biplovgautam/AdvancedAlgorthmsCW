## Question 2: Scenario: The "Strategic Tile Shatter" Game (Dynamic Programming)[5 Marks]

### Problem :
You're playing a new single-player arcade game called "Strategic Tile Shatter." In this game, you are presented with a row of n intricately designed ceramic tiles, each marked with a unique score multiplier. Your objective is to shatter all the tiles one by one.  
When you shatter the i-th tile, you earn points based on the score multipliers of its adjacent tiles. 
Specifically, if you shatter tile i, you gain points equal to the product of the score multipliers of the tile 
immediately to its left, the tile i itself, and the tile immediately to its right.

#### A special rule applies to tiles at the ends:

- If tile i-1 is out of bounds (meaning tile i is the leftmost tile remaining), its score multiplier is treated as 1.

- If tile i+1 is out of bounds (meaning tile i is the rightmost tile remaining), its score multiplier is treated as 1.

Your challenge is to devise a strategy to shatter all the tiles in a specific order to maximize your total 
accumulated points.

#### Formal Defination:
Given an array tile_multipliers where tile_multipliers[i] is the score multiplier painted on the i-th tile 
(indexed from 0 to n-1), determine the maximum total points you can collect by shattering the tiles 
optimally.

#### Constraints: 
This problem must be solved using a Dynamic Programming approach. You are expected to define your dp 
state, recurrence relation, base cases, and the order of computation. 

#### Example 1: 
Input: tile_multipliers = [3, 1, 5, 8]

Output: 167 

Initial State: [3, 1, 5, 8] 

Shatter 1: 3 * 1 * 5 = 15 points. Remaining: [3, 5, 8] 

Shatter 5: 3 * 5 * 8 = 120 points. Remaining: [3, 8] 

Shatter 3: 1 * 3 * 8 = 24 points. Remaining: [8] (Note: 1 is for the left out-of-bounds, 8 is to its right) 

Shatter 8: 1 * 8 * 1 = 8 points. Remaining: [] (Note: 1 for both left and right out-of-bounds) 

*Total Points = 15 + 120 + 24 + 8 = 167 
#### Example 2: 

Input: tile_multipliers = [1, 5] 

Output: 10 

*Shatter 1: 1 * 1 * 5 = 5 points. Remaining: [5] 

*Shatter 5: 1 * 5 * 1 = 5 points. Remaining: [] 

*Total Points = 5 + 5 = 10 
