
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
Topological Sort
​
You are given a list of arbitrary jobs that need to be completed; these jobs are represented by integers. You are also given a list of dependencies. A dependency is represented as a pair of jobs where the first job is prerequisite of the second one. In other words, the second job depends on the first one; it can only be completed once the first job is completed. Write a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid order in which the given jobs can be completed. If no such order exists, the function should return an empty list.
​
Sample input: [1, 2, 3, 4], [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
Sample output: [1, 4, 3, 2] or [4, 1, 3, 2]
​
Input:Your Solution
Our Solution


No changes made.
Run Code
Solution #1Solution #2
1
# Copyright © 2019 AlgoExpert, LLC. All rights reserved.
2
​
3
# O(j + d) time | O(j + d) space
4
def topologicalSort(jobs, deps):
5
    jobGraph = createJobGraph(jobs, deps)
6
    return getOrderedJobs(jobGraph)
7
​
8
def createJobGraph(jobs, deps):
9
    graph = JobGraph(jobs)
10
    for job, dep in deps:
11
        graph.addDep(job, dep)
12
    return graph
13
​
14
def getOrderedJobs(graph):
15
    orderedJobs = []
16
    nodesWithNoPrereqs = list(filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
17
    while len(nodesWithNoPrereqs):
18
        node = nodesWithNoPrereqs.pop()
19
        orderedJobs.append(node.job)
20
        removeDeps(node, nodesWithNoPrereqs)
21
    graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
22
    return [] if graphHasEdges else orderedJobs
23
​
24
def removeDeps(node, nodesWithNoPrereqs):
25
    while len(node.deps):
26
        dep = node.deps.pop()
27
        dep.numOfPrereqs -= 1
28
        if dep.numOfPrereqs == 0:
29
            nodesWithNoPrereqs.append(dep)
30
​
31
class JobGraph:
32
    def __init__(self, jobs):
Help:Hide
Show
Hint #1Hint #2Hint #3Optimal Space & Time Complexity
Try representing the jobs and dependencies as a graph, where each vertex is a job and each edge is a dependency. How can you traverse this graph to topologically sort the list of jobs?
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
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
9
        deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [1, 6], [1, 2], [7, 6]]
10
        order = program.topologicalSort(jobs, deps)
11
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)
12
​
13
    def test_case_2(self):
14
        jobs = [1, 2, 3, 4, 5, 6, 7, 8]
15
        deps = [[3, 1], [8, 1], [8, 7], [5, 7], [5, 2], [1, 4], [6, 7], [1, 2], [7, 6]]
16
        order = program.topologicalSort(jobs, deps)
17
        self.assertEqual(order, [])
18
​
19
    def test_case_3(self):
Video ExplanationGo to Conceptual OverviewGo to Code WalkthroughQuestions List
Copyright © 2019 AlgoExpert, LLC. All rights reserved.
Become An Affiliate
Contact Us
FAQ
Legal Stuff
Privacy Policy
