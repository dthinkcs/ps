#include <iostream>
#include <iomanip>
using namespace std;

double celciusConverter(double F);

int main(void) {
    cout << "Fahrenheit Celcius" << endl;
    cout << "---------------------" << endl;
    cout << setprecision(1) << fixed;
    for (int i = 0; i <= 200; i += 20) {
        cout << i << " " << celciusConverter(i) << endl;
    }

}

double celciusConverter(double F) {
    return 5 * (F - 32) / 9;
}