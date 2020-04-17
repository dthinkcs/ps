
Don't show this again.

Questions List
C++
Go
Java
Javascript
Python



Theme:
algoexpert
algoexpert
blackboard
cobalt
lucario
midnight
night
oceanic-next
rubyblue
white
Keymaps:
default
default
emacs
vim

00:00

×Don't forget to scroll to the bottom of the page for the video explanation!
Question:_
No changes made.


​
Boggle Board
​
You are given a two-dimensional array (matrix) of potentially unequal height and width containing letters; this matrix represents a boggle board. You are also given a list of words. Write a function that returns an array of all the words contained in the boggle board. A word is constructed in the boggle board by connecting adjacent (horizontally, vertically, or diagonally) letters, without using any single letter at a given position more than once; while words can of course have repeated letters, those repeated letters must come from different positions in the boggle board in order for the word to be contained in the board. Note that two or more words are allowed to overlap and use the same letters in the boggle board.
​
Sample input:
[
  ["t", "h", "i", "s", "i", "s", "a"],
  ["s", "i", "m", "p", "l", "e", "x"],
  ["b", "x", "x", "x", "x", "e", "b"],
  ["x", "o", "g", "g", "l", "x", "o"],
  ["x", "x", "x", "D", "T", "r", "a"],
  ["R", "E", "P", "E", "A", "d", "x"],
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(nm*8^s + ws) time | O(nm + ws) space
4
def boggleBoard(board, words):
5
    trie = Trie()
6
    for word in words:
7
        trie.add(word)
8
    finalWords = {}
9
    visited = [[False for letter in row] for row in board]
10
    for i in range(len(board)):
11
        for j in range(len(board[i])):
12
            explore(i, j, board, trie.root, visited, finalWords)
13
    return list(finalWords.keys())
14
​
15
def explore(i, j, board, trieNode, visited, finalWords):
16
    if visited[i][j]:
17
        return
18
    letter = board[i][j]
19
    if letter not in trieNode:
20
        return
21
    visited[i][j] = True
22
    trieNode = trieNode[letter]
23
    if "*" in trieNode:
24
        finalWords[trieNode["*"]] = True
25
    neighbors = getNeighbors(i, j, board)
26
    for neighbor in neighbors:
27
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
28
    visited[i][j] = False
29
​
30
def getNeighbors(i, j, board):
31
    neighbors = []
32
    if i > 0 and j > 0:
Help:Hide
Show
Hint #1Hint #2Hint #3Hint #4Optimal Space & Time Complexity
You can divide this question into two separate problems: one part involves traversing the boggle board in such a way that allows you to construct strings letter by letter; the other part involves actually comparing the strings you construct in the board against the words in the list that you're given. For the second part, what data structure lends itself very well to matching characters to multiple strings at once?
Output:Custom Output
Raw Output
Run your code when you feel ready.
​
Tests:Our Tests
Your Tests
Hide
Show

No changes made.
1
import program
2
import unittest
3
​
4
​
5
class TestProgram(unittest.TestCase):
6
​
7
    def test_case_1(self):
8
        board = [
9
            ["y", "g", "f", "y", "e", "i"],
10
            ["c", "o", "r", "p", "o", "u"],
11
            ["j", "u", "z", "s", "e", "l"],
12
            ["s", "y", "u", "r", "h", "p"],
13
            ["e", "a", "e", "g", "n", "d"],
14
            ["h", "e", "l", "s", "a", "t"],
15
        ]
16
        words = ["san", "sana", "at", "vomit", "yours", "help", "end", "been", "bed", "danger", "calm", "ok", "chaos", "complete", "rear", "going", "storm", "face", "epual", "dangerous"]
17
        expected = ["yours", "help", "danger", "san", "at"]
18
        actual = program.boggleBoard(board, words)
19
        self.assertEqual(len(actual), len(expected))
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
