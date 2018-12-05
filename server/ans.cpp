#include <iostream>

using namespace std;

int main(){
    int cases, time;
    cin >> cases >> time;
    int c = cases;
    while(c--){
        int val;
        cin >> val;
        cout << "Process time: " << val << endl;
        time -= val;
        cout << "Remaining time: " << time << endl;
        if(time < 0){
            cout << "Cases: " << cases << endl;
            cout << "Decrement: " << c << endl;
            cout << cases-c-1 << endl;
            return 0;
        }
    }
    cout << cases << endl;
    return 0;
}
