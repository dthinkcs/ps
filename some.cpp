#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;
int main(void) {
    // input into s
    string s;
    cout << "Please Enter a word OR Sentence" << endl;
    getline(cin, s);
    // take stringstream s
    stringstream ss(s);
    string temp; // temp string
    int maxLength = INT_MIN; // assuming maxLength to be INT_MIN
    while (ss >> temp) {
        maxLength = max(maxLength, (int)temp.length());
    }
    // first line
    cout << "+";
    for (int i = 0; i < maxLength; i++) {
        cout << "-";
    }
    cout << "+" << endl;

    stringstream ss2(s); // re initializing the stream string to s
    while (ss2 >> temp) {
        // formula for leading spaces
        int leadingSpaces = ( maxLength - temp.size() ) / 2;
        cout << "|";
        for (int i = 0; i < leadingSpaces; i++) {
            cout << " ";
        }  
        // one more leading space for odd length strings
        if (temp.length() % 2 == 1 && maxLength % 2 == 0)  {
            cout << " ";
        }

        // printing the word
        cout << temp;


        for (int i = 0; i < leadingSpaces; i++) {
            cout << " ";
        }
        // one more space for even length strings
        if (temp.length() % 2 == 0 && maxLength % 2 == 1)  {
            cout << " ";
        }
        cout << "|" << endl;
    }

    // last line
    cout << "+";
    for (int i = 0; i < maxLength; i++) {
        cout << "-";
    }    
    cout << "+" << endl;
}
