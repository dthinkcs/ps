
// #include<bits/stdc++.h>
// using namespace std;

// int findit(int* distance ,bool* visited , int v){
// 	int minVertex  = -1;
// 	for(int i = 0;i<v;i++){
// 		if(!visited[i]&&(minVertex == -1 ||distance[i]<distance[minVertex])){
// 			minVertex = i;
// 		}
// 	}

// 	return minVertex;
// }


// int main(){
// 	int v,e,c,k;
// 	cin >> v >> e >> c >> k;
// 	vector<int>* edges = new vector<int>[v];
// 	// for(int i = 0;i<v;i++){
// 	// 	edges[i] = new int[v];
// 	// 	for(int j = 0;j<v;j++){
// 	// 		edges[i][j] = 0;
// 	// 	}
// 	// }

// 	for(int i = 0;i<e;i++){
//         int f,s,w;
// 		cin >> f >> s >>w;
//         edges[f - 1][s - 1] = w;
// 		edges[s - 1][f - 1] = w;
// 	}

// 	//cout << djikstra(edges,v, c - 1, k) << endl;

//     bool* visited = new bool[v];
// 	int* distance = new int[v];
// 	for(int i = 0;i<v;i++){
// 		visited[i] = false;
// 		distance[i] = INT_MAX;
// 	}

//     // since this is from vertex zero if we have to generalize then we must
//     // set the value of captital city (starting vertex/ source vertex)
// 	distance[c - 1] = 0;

// 	for(int i = 0;i<v;i++){
// 		int minVertex = findit(distance,visited,v);
//         //if (minVertex == -1)
//         //{
//         //    cout << "OH NO";
//         //    return 0;
//         //}

// 		visited[minVertex] = true;
// 		for(int j = 0;j<v;j++){
// 			if(!visited[j]&&edges[minVertex][j]!=0){
// 				distance[j] = min(distance[j],distance[minVertex]+edges[minVertex][j]);
// 			}
// 		}
// 	}
//     int count = 0;
// 	for(int i = 0;i<v;i++){
// 		//cout << i << " " << distance[i] << endl;
//         if (distance[i] <= k)
//             count++;
// 	}

//     cout << count;

// }

#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e6 + 6 ;
priority_queue< pair<int,int> , vector< pair<int,int> > , greater< pair<int,int> >> pq ;
//int dis1[MAXN] = {};
const int INF = INT_MAX ;
int n,m ;
vector< pair<int,int> > g[MAXN] ;

// source, dis, predecesor 
void dijkstra(int s,int *dis, vector< pair<int,int> > *g){
    // 1 to N :: WILL NOT WORK FOR 0 to n - 1
    for(int i = 1 ; i <= n ; i++)
      dis[i] = INF ; // can also use predecesoor[i] = NULL; instead of vector<pair <int, int>> "MAPS" vertex to predecessor
    dis[s] = 0 ;
    pq.push({dis[s] , s}) ;
    while(!pq.empty()){
        int u = pq.top().second ;
        int d = pq.top().first ;
        pq.pop() ;
        if(dis[u] != d) continue ;
        // for each unvisited negihbout v of u
        for(auto it:g[u]){
            int v = it.first ;
            int wt = it.second ;
            // tempDist = dist[u] + edgwt(u, v)
            // if tempDist < dist[v]
            if((dis[u] + wt) < dis[v]){
              // then we found a better path
                dis[v] = dis[u] + wt ;
                pq.push({dis[v],v}) ;
            }
        }
    }
    // return dist, predecessor
}

int main(int argc,char* argv[]) {


    int c, k;
    cin >> n >> m >> c >> k ;
    int u,v,w ;
    while(m--)
    {
        cin >> u >> v >> w ;
        g[u].push_back({v , w}) ;
        g[v].push_back({u, w}) ;
    }
    dijkstra(c, dis1, g) ;
    int count = 0;
    for (int i = 1; i <= n; i++)
        if (dis1[i] <= k)
            count += 1;


    //dijkstra(t,dis2,g) ;
    //dijkstra(s,dis3,g2) ;
    //dijkstra(t,dis4,g2) ;
    // bool ok = 0 ;
    // int ans = INF  ;
    // for(int i = 1 ; i <= n ; i++){
    //     if(i == s || i == t) continue ;
    //     if(dis1[i] < INF && dis2[i] < INF  && dis3[i] < INF && dis4[i] < INF){
    //         ok = 1 ;
    //         int tmp = dis1[i] + dis2[i] + dis3[i] + dis4[i] ;
    //         ans = min(ans ,tmp) ;
    //     }
    // }
    // if(!ok) ans = -1 ;
    cout << count << endl ;
    // return 0 ;
}
