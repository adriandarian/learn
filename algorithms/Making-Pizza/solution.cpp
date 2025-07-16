#include "solution.hpp"
#include <bits/stdc++.h>

using namespace std;

int Solution::solve(string s)
{
    int pizza[4] = {0, 0, 0, 0};

    for (int i = 0; i < s.length(); i++)
    {
        switch (s[i])
        {
        case 'p':
        {
            pizza[0]++;
            break;
        }
        case 'i':
        {
            pizza[1]++;
            break;
        }
        case 'z':
        {
            pizza[2]++;
            break;
        }
        case 'a':
        {
            pizza[3]++;
            break;
        }
        }
    }

    int result = pizza[0];
    cout << pizza[0] << endl;
    for (int i = 1; i < 4; i++)
    {
        cout << pizza[i] << endl;
        if (i == 2)
        {
            if (result > pizza[i] / 2)
            {
                result = pizza[i] / 2;
            }
        }
        else if (result > pizza[i])
        {
            result = pizza[i];
        }
    }

    return result;
};