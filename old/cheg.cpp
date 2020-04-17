#include <iostream>
#include <vector>
#include <stack>
using namespace std;
/*
If you want to make your own functions so you can modifiy parameters
ensure you are using the result vector to store your answers
*/
void iterativeDFS( std::vector<std::vector<int> > & adjList, int startNode, std::vector<int> & result ){
    /* Your code goes here */
    vector<bool> visited(adjList.size(), false);

    stack<int> s;
    s.push(startNode);
    visited[startNode] = true;
    while (!s.empty()) {
        int topNode = s.top(); s.pop();
        result.push_back(topNode);
        for (int i = adjList[topNode].size() - 1; i >= 0; i--) {
            int v = adjList[topNode][i];
            if (v != topNode && visited[v] == false ) {
                s.push(v);
                visited[v] = true;
            }
        }
    }

}

void recursiveDFS( std::vector<std::vector<int> > & adjList, int currNode, std::vector<bool> & visited, std::vector<int> & result ){
    /* Your code goes here */
    visited[currNode] = true;
    result.push_back(currNode);
    for (int v: adjList[currNode]) {
        if (v!= currNode && visited[v] == false) {
            recursiveDFS(adjList, v, visited, result);
        }
    }
}


int main() {
    // Nothing is needed in main

    // TESTING
    //vector< vector<int> > adjList { {1, 2}, {2}, {0, 3}, {3}  };
        vector< vector<int> > adjList{ { 1, 2 }, { 2 }, { 0, 3}, {3} }; 

    vector<bool> visited(4, false);
    vector<int> result;
    recursiveDFS(adjList, 2, visited, result);
    for (int n: result) {
        cout << n << " ";
    }
    cout << endl;

    result.clear();
    iterativeDFS(adjList, 2, result);
    for (int n: result) {
        cout << n << " ";
    }
    cout << endl;

    return 0;
}