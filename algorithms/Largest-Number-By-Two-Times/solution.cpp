#include "solution.hpp"
#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

bool Solution::solve(vector<int> &nums)
{
    sort(nums.begin(), nums.end());
    return nums[nums.size() - 1] > nums[nums.size() - 2] * 2;
};
