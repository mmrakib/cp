/**
 * Counting Bits
 * https://leetcode.com/problems/counting-bits/description/
 * 
 * Mayaz Rakib (mmrakib)
*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> cb(int n) {
    vector<int> result;

    for (int i = 0; i <= n; i++) {
        int ones = 0;
        int b = i;

        while (b > 0) {
            ones += b % 2;
            b /= 2;
        }

        result.push_back(ones);
    }

    return result;
}

int main() {
    int input = 7;
    vector<int> output = cb(input);

    for (auto &x : output) cout << x << '\n';

    return 0;
}
