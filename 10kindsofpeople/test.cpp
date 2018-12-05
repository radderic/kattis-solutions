#include <iostream>
#include <vector>
#include <unistd.h>

using namespace std;

#define HEIGHT 10
#define WIDTH 10
#define MARK 2

void mark(int &x, int &y, int (&map)[HEIGHT][WIDTH]) {
    map[x][y] = MARK;
}

void printMap(int (&map)[HEIGHT][WIDTH]) {
    cout << "\033[2J\033[1;1H";
    for(int r = 0; r < HEIGHT; r++) {
        for(int c = 0; c < WIDTH; c++) {
            cout << map[r][c];
        }
        cout << endl;
    }
}

void moveLeft(int r, int c, int (&map)[HEIGHT][WIDTH], int &wall) {
    if(c-1 >= 0 && map[r][c-1] != wall) {
        c--;
        mark(r, c, map);
    }
}

void moveRight(int r, int c, int (&map)[HEIGHT][WIDTH], int &wall) {
    if(c+1 < HEIGHT && map[r][c+1] != wall) {
        c++;
        mark(r, c, map);
    }
}

void moveUp(int r, int c, int (&map)[HEIGHT][WIDTH], int &wall) {
    if(r-1 >= 0 && map[r-1][c] != wall && map[r-1][c] != MARK) {
        r--;
        mark(r, c, map);
    }
}

void moveDown(int r, int c, int (&map)[HEIGHT][WIDTH], int &wall) {
    if(r+1 < WIDTH && map[r+1][c] != wall && map[r+1][c] != MARK) {
        r++;
        mark(r, c, map);
    }
}

void traverse(int r, int c, int (&map)[HEIGHT][WIDTH], int wall) {
    moveLeft(r, c, map, wall);
}

int main(void) {
    int wall = 1;
    int path = 0;

    int r = 0;
    int c = 2;

    int map[HEIGHT][WIDTH] = {
                        {1, 1, 0, 0, 1, 1, 0, 1, 1, 0},
                        {1, 0, 0, 0, 0, 1, 0, 0, 0, 0},
                        {1, 1, 0, 0, 1, 1, 0, 1, 0, 0},
                        {1, 1, 0, 0, 1, 1, 0, 1, 1, 0},
                        {1, 1, 0, 0, 1, 1, 0, 1, 1, 0},
                        {1, 1, 0, 1, 1, 1, 0, 1, 1, 0},
                        {1, 1, 0, 1, 1, 1, 0, 1, 1, 0},
                        {1, 1, 0, 0, 0, 0, 0, 1, 1, 0},
                        {0, 0, 0, 1, 1, 1, 0, 1, 0, 0},
                        {1, 1, 0, 1, 1, 1, 0, 1, 1, 0}
                      };
    mark(r, c, map);
    printMap(map);
    sleep(2);
    moveRight(r, c, map, wall);
    printMap(map);
    sleep(2);
    moveDown(r, c, map, wall);
    printMap(map);

    return 0;

}
