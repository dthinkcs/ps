
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
Airport Connections
​
You are given a list of airports (three-letter codes like 'JFK'), a list of routes (one-way flights from one airport to another like ['JFK', 'SFO']), and a starting airport. Write a function that returns the minimum number of airport connections (one-way flights) that need to be added in order for someone to be able to reach any airport in the list, starting at the starting airport. Note that the connections don't have to be direct; it's okay if an airport can only be reached from the starting airport by stopping at other airports first.
​
Sample input:
[
  "BGI",
  "CDG",
  "DEL",
  "DOH",
  "DSM",
  "EWR",
Input:Your Solution
Our Solution


No changes made.
Run Code
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(a * (a + r) + a + r + alog(a)) time | O(a + r) space - where a is the number of airports and r is the number of routes
4
def airportConnections(airports, routes, startingAirport):
5
    airportGraph = createAirportGraph(airports, routes)
6
    unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
7
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
8
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)
9
​
10
# O(a + r) time | O(a + r) space
11
def createAirportGraph(airports, routes):
12
    airportGraph = {}
13
    for airport in airports:
14
        airportGraph[airport] = AirportNode(airport)
15
    for route in routes:
16
        airport, connection = route
17
        airportGraph[airport].connections.append(connection)
18
    return airportGraph
19
​
20
# O(a + r) time | O(a) space
21
def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
22
    visitedAirports = {}
23
    depthFirstTraverseAirports(airportGraph, startingAirport, visitedAirports)
24
​
25
    unreachableAirportNodes = []
26
    for airport in airports:
27
        if airport in visitedAirports:
28
            continue
29
        airportNode = airportGraph[airport]
30
        airportNode.isReachable = False
31
        unreachableAirportNodes.append(airportNode)
32
    return unreachableAirportNodes
Help:Hide
Show
Hint #1Hint #2Hint #3Hint #4Optimal Space & Time Complexity
Start by creating a graph out of the inputs. Each airport should be a vertex in the graph, and each route should be an edge. The graph should be directed with potential cycles, since it's possible for there to be round-trip flights between airports or for some series of flights to eventually lead back to an arbitrary starting point. How can this graph be useful?
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
AIRPORTS = [
6
    'BGI',
7
    'CDG',
8
    'DEL',
9
    'DOH',
10
    'DSM',
11
    'EWR',
12
    'EYW',
13
    'HND',
14
    'ICN',
15
    'JFK',
16
    'LGA',
17
    'LHR',
18
    'ORD',
19
    'SAN',
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
