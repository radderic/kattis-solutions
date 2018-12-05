#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int findSquare(int n) {
    return ceil(sqrt(n));
}

int main(void) {
    int messageNum;

    cin >> messageNum;
    for(int l = 0; l < messageNum; l++) {
        string input;
        cin >> input;
        int square = findSquare(input.size());
        int pos = 0;
        char msg[square][square];

        for(int i = 0; i < square; i++) {
            for(int k = 0; k < square; k++) {
                if(pos < input.size()) {
                    msg[i][k] = input[pos++];
                }
                else {
                    msg[i][k] = '*';
                }
            }
        }

        //read sideways
        for(int i = 0; i < square; i++) {
            for(int k = square-1; k >= 0; k--) {
                if(msg[k][i] != '*')
                    cout << msg[k][i];
            }
        }
        cout << endl;
    }
    return 0;
}
