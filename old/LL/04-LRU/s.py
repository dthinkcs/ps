
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
LRU Cache
​
Implement a class for a Least Recently Used (LRU) Cache. The cache should support inserting key / value pairs (the insertKeyValuePair() method), retrieving a key's value (the getValueFromKey() method), and retrieving the most recently "active" key (the getMostRecentKey() method); each of these methods should run in constant time. When a key / value pair is inserted or a key's value is retrieved, the key in question should become the most recent key. Also, the LRUCache class should store a maxSize property set to the size of the cache, which is passed in as an argument during instantiation. This size represents the maximum number of key / value pairs that the cache can hold at once. If a key / value pair is added to the cache when it has reached maximum capacity, the least recently used ("active") key / value pair should be evicted from the cache and no longer retrievable; the newly added key / value pair should effectively replace it. Inserting a key / value pair with an already existing key should simply replace the key's value in the cache with the new value and should not evict a key / value pair if the cache is full. Attempting to retrieve a value from a key that is not in the cache should return the None (null) value.
​
Sample input: (for an LRU Cache of size 3)
insertKeyValuePair("a", 1)
insertKeyValuePair("b", 2)
insertKeyValuePair("c", 3)
getMostRecentKey()
getValueFromKey("a")
getMostRecentKey()
insertKeyValuePair("d", 4)
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
class LRUCache:
4
    def __init__(self, maxSize):
5
        self.cache = {}
6
        self.maxSize = maxSize or 1
7
        self.currentSize = 0
8
        self.listOfMostRecent = DoublyLinkedList()
9
​
10
    # O(1) time | O(1) space
11
    def insertKeyValuePair(self, key, value):
12
        if key not in self.cache:
13
            if self.currentSize == self.maxSize:
14
                self.evictLeastRecent()
15
            else:
16
                self.currentSize += 1
17
            self.cache[key] = DoublyLinkedListNode(key, value)
18
        else:
19
            self.replaceKey(key, value)
20
        self.updateMostRecent(self.cache[key])
21
​
22
    # O(1) time | O(1) space
23
    def getValueFromKey(self, key):
24
        if key not in self.cache:
25
            return None
26
        self.updateMostRecent(self.cache[key])
27
        return self.cache[key].value
28
​
29
    # O(1) time | O(1) space
30
    def getMostRecentKey(self):
31
        return self.listOfMostRecent.head.key
32
​
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
What data structure could allow you to insert, retrieve, and evict resources as fast as possible, all the while keeping track of the least recently accessed resource - essentially keeping track of the order of the resources? A hash table would allow you to insert and retrieve resources fast, but it wouldn't allow you to keep track of their order. An array would let you keep track of their order, but it wouldn't let you access elements fast; it also wouldn't allow you to move an element from one position to another in constant time, which you would need to do to make a newly-accessed key / value pair the most recent one upon retrieval of a key's value. A linked list would allow you to keep track of elements' order and to move them seamlessly (if you knew their position), but it wouldn't allow you to access them easily without knowing their position beforehand. Could a heap help? What about a BST or a trie? Would any other data structures work?
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
letterMaps = {
6
    "a": 0,
7
    "b": 1,
8
    "c": 2,
9
    "d": 3,
10
    "e": 4,
11
    "f": 5,
12
    "g": 6,
13
    "h": 7,
14
    "i": 8,
15
    "j": 9,
16
}
17
​
18
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
19
​
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
