#include <iostream>
#include <vector>

int main(void) {

    int d1, d2;

    std::cin >> d1 >> d2;

    std::cout << d1 << std::endl;
    std::cout << d2 << std::endl;

    int total = d1 + d2;
    std::cout << total << std::endl;
    std::vector<int> rolls(total, 0);

    int max = 0;

    for(int i = 1; i <= d1; i++) {
        for(int k = 1; k <= d2; k++) {
            rolls[i + k]++;
            if(rolls[i+k] > max)
            {
                std::cout << "New max: " << max << std::endl;
                max = rolls[i+k];
            }
        }
    }
    std::cout << "New max: " << max << std::endl;

    return 0;
}
