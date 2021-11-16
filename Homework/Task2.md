# Unit 5.4 M2 Task 2

## Question
- In a BFS, we track what neighbors still need to be explored. In a BFS, this is done in a first in, first out FIFO order. 
- What data structure works best for keeping track of these unvisited neighbors?

## Solution
- queue 
 - q.pop(o)
 - One of the most common and simplest ways to implement a BFS is to use a __queue__ to keep track of unvisited nodes and a set to keep track of visited nodes. 