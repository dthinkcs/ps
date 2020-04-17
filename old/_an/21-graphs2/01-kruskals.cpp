#include <bits/stdc++.h>
using namespace std;

struct Edge{
	int source;
	int dest;
	int weight;
};

bool comparator(Edge a, Edge b){
	return a.weight<b.weight;
}

int findParent(int v, int*parent){
	if(parent[v]==v){
		return v;
	}
	findParent(parent[v],parent);
}
void kruskals(Edge* input, int n, int E){
	//sort;
	sort(input,input+E,comparator);

	Edge *output = new Edge[n-1];

	int* parent = new int[n];

	for(int i =0 ;i<n;i++){
		parent[i] = i;
	}
	int count = 0;
	int i = 0;
	while(count!=n-1){
		Edge currentEdge = input[i];
		//checking using Union Find
		int sourceParent = findParent(currentEdge.source,parent);
		int destParent = findParent(currentEdge.dest,parent);

		if(sourceParent!=destParent){
			output[count] = currentEdge;
			count++;
			parent[sourceParent] = destParent;
		}

		i++;
	}

	for(int i = 0;i<n-1;i++){
		int anssource=  min(output[i].source,output[i].dest);
		int ansdest =  max(output[i].dest,output[i].source);
		cout <<anssource<< " " <<ansdest << " " << output[i].weight << endl;
	}
}
int main(){
	int n,E;
	cin >> n >> E;
	Edge* input = new Edge[E];

	for(int i =0;i<E;i++){
		int s,d,w;
		cin >> s >> d >> w;
		input[i].source = s;
		input[i].dest = d;
		input[i].weight = w;
	}

	kruskals(input,n,E);
}
