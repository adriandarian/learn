#include "solution.hpp"
#include <bits/stdc++.h>

using namespace std;

int Solution::solve(vector<int> &nums)
{
    return accumulate(nums.begin(), nums.end(), 0) - (nums.size() - 1) * nums.size() / 2;
};
