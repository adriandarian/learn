#include "solution.hpp"
#include <bits/stdc++.h>

using namespace std;

int Solution::solve(vector<int> &a, vector<int> &b)
{
    int p;

    for (int i = 0; i < a.size(); i++)
    {
        p += a[i] * b[i];
    }

    return p;
};
