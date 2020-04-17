// non preemptive FCFS
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
struct Process {
  int id;
  int at;
  int bt;

  int startTime;
  int endTime;

  Process() {

  }

  Process(int id, int at, int bt) {
    this->id = id;
    this->at = at;
    this->bt = bt;
  }
};
void fcfsNP(Process * p, int n);
void fcfsInOrderNP(Process* p, int n);
bool processCompareAT(Process a, Process b);
void printProcessTable(Process* p, int n);

int main(void) {
  int n;
  cout << "Number of Processes: " << endl;
  cin >> n;
  cout << "PID AT BT(format): " << endl;
  Process* p = new Process[n];
  for (int i = 0; i < n; i++) {
    int id; int at; int bt;

    // cin >> p[i].id;
    // cin >> p[i].at;
    // cin >> p[i].bt;
    cin >> id;
    cin >> at;
    cin >> bt;

    p[i] = Process(id, at, bt);
  }

  // fcfsNP(p, n);
  fcfsInOrderNP(p, n); // contain a map (OR INDIRECTION) if you do not want to sort

}

bool processCompareAT(Process a, Process b) {
  return a.at < b.at;
}

void printProcessTable(Process* p, int n) {
  cout << "P ID\tAT\tBT\tTAT\tWT" << endl;

  for (int i = 0; i < n; i++) {
    cout << p[i].id << "\t" << p[i].at << "\t" << p[i].bt << "\t" << p[i].endTime - p[i].at << "\t" << p[i].startTime - p[i].at << endl;
  }
}


void fcfsNP(Process* p, int n) {
  sort(p, p + n, processCompareAT);
  // assert p.at[i] > 0

  // start from t = 0
  int t = 0;
  for (int i = 0; i < n; i++) {
    // p[i].at if this is the first thing non premtive
    // if (i == 0) {
    //   p[i].startTime = p[i].at;
    //   p[i].endTime = p[i].at + p[i].bt;
    // } else {
      p[i].startTime = max(p[i].at, t);
      p[i].endTime = max(p[i].at, t) + p[i].bt;
    // }
    t = p[i].endTime; // non preemptive
  }
  // premptive issues :: mutliple startTimes[0...] and endTimes[...n-1]
  // print Table

}

bool processPtrCompareAT(Process* a, Process* b) {
  return a->at < b->at;
}

// correction create a Process**
void fcfsInOrderNP(Process* p, int n) {
  // copy it first
  Process** pcopy = new Process*[n];
  for (int i = 0; i < n; i++)
    pcopy[i] = &(p[i]);
  // mutate the copy of p to get the values of start and end time
  sort(pcopy, pcopy + n, processPtrCompareAT);
  // start from t = 0
  int t = 0;
  for (int i = 0; i < n; i++) {
    // p[i].at if this is the first thing non premtive
    // if (i == 0) {
    //   p[i].startTime = p[i].at;
    //   p[i].endTime = p[i].at + p[i].bt;
    // } else {
      pcopy[i]->startTime = max(pcopy[i]->at, t);
      pcopy[i]->endTime = max(pcopy[i]->at, t) + pcopy[i]->bt;
    // }
    t = pcopy[i]->endTime; // non preemptive
  }

  printProcessTable(p, n);

}
