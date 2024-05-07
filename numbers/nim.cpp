/**
 * Nim Game
 * https://leetcode.com/problems/nim-game/description/
 * 
 * Mayaz Rakib (mmrakib)
*/

#include <iostream>

using namespace std;

bool nim(int n) {
    return (bool)(n % 4);
}

int main() {
    int input = 4;
    bool output = nim(input);

    cout << (output ? "true" : "false") << '\n';

    return 0;
}
