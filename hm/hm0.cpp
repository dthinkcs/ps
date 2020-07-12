#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Node {
public:
    string key;
    string value;
    Node* next;
    Node(string key, string value) {
        this->key = key;
        this->value = value;
    }
};
#define INITIAL_SIZE 5
#define BASE 37
class Map {
public:
    Node** arrayOfNodes;
    int size;
    int numberOfFilledBuckets;
    
    void test() {
        for (int i = 0; i < size; i++) 
            if (arrayOfNodes[i] == NULL) 
                cout << i << ": NULL" << endl;
            else 
                for (Node* ptr = arrayOfNodes[i]; ptr; ptr=ptr->next) 
                    cout << i << ": " << ptr->key << ", " << ptr->value << endl;
        cout << "SIZE: " << size << endl;
        cout << "NUM_FILLED_BUCKETS: " << numberOfFilledBuckets << endl;
    }


    Map() {
        size = INITIAL_SIZE;
        arrayOfNodes = new Node*[size];
        for (int i = 0; i < size; i++)
            arrayOfNodes[i] = NULL;
        numberOfFilledBuckets = 0;
    }
    string get(string key) {
        int index = getHash(key);
        for (Node* ptr = arrayOfNodes[index]; ptr; ptr=ptr->next) {
            if (key.compare(ptr->key) == 0)
                return ptr->value;
        }
        return ""; // NULL
    }
    void insert(string key, string value) {
        int index = getHash(key);
        // check if already present
        for (Node* ptr = arrayOfNodes[index]; ptr; ptr=ptr->next) {
            if (key.compare(ptr->key) == 0) {
                return;
            }
        }

        if (arrayOfNodes[index] == NULL) 
            this->numberOfFilledBuckets++;

        Node* newNodePtr = new Node(key, value);
        newNodePtr->next = arrayOfNodes[index];
        arrayOfNodes[index] = newNodePtr;
        // this->numberOfFilledBuckets++;
        // WAS BUGGY ^
    }

    void rehash() {
        return;
    }
    int getHash(string key) {
        int multiplier = 1;
        int hash = 0;
        for (int i = 0; i < key.length(); i++) {
            hash = hash + ( key[i] * multiplier ) % size;
            multiplier = (multiplier * BASE) % size; // prime, otherwise mutliplier=0
        }   
        return hash % size;

    }

};

int main() {
    Map mapFromCountriesToCapitalCities;
    mapFromCountriesToCapitalCities.insert("India", "New Delhi");  
    cout << mapFromCountriesToCapitalCities.get("India") << endl;
    mapFromCountriesToCapitalCities.test();

        mapFromCountriesToCapitalCities.insert("US", "Washigton D.C.");  
    cout << mapFromCountriesToCapitalCities.get("US") << endl;
    mapFromCountriesToCapitalCities.test();

            mapFromCountriesToCapitalCities.insert("UK", "London");  
    cout << mapFromCountriesToCapitalCities.get("UK") << endl;
    mapFromCountriesToCapitalCities.test();

                mapFromCountriesToCapitalCities.insert("Canada", "Ottawa");  
    cout << mapFromCountriesToCapitalCities.get("Canada") << endl;
    mapFromCountriesToCapitalCities.test();

    
                    mapFromCountriesToCapitalCities.insert("Australia", "Canberra");  
    cout << mapFromCountriesToCapitalCities.get("Australia") << endl;
    mapFromCountriesToCapitalCities.test();

                        mapFromCountriesToCapitalCities.insert("New Zealand", "Wellington");  
    cout << mapFromCountriesToCapitalCities.get("New Zealand") << endl;
    mapFromCountriesToCapitalCities.test();

                        mapFromCountriesToCapitalCities.insert("Singapore", "Singapore City");  
    cout << mapFromCountriesToCapitalCities.get("Singapore City") << endl;
    mapFromCountriesToCapitalCities.test();

                            mapFromCountriesToCapitalCities.insert("J", "JJ");  
    cout << mapFromCountriesToCapitalCities.get("JJ") << endl;
    mapFromCountriesToCapitalCities.test();
}