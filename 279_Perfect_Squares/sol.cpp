#include <iostream>
#include <vector>
#include <math.h>
#include <limits.h>
#include <algorithm>

using namespace std;

class Solution {
    public:
        int bfs(vector<int> &out, int n)
        {
            // already has record
            if(out[n] != 0)
                return out[n];

            // add new record
            int x = sqrt(n);
            if(x*x == n)
            {
                out[n] = 1;
                return 1;
            }

            int min_out = INT_MAX;
            while(x > 0)
            {
                min_out = min(min_out, 1+bfs(out,n-x*x));
                if(min_out == 2)
                {
                    out[n] = 2;
                    return 2;
                }
                x--;
            }
            out[n] = min_out;
            return min_out;
        }

        int numSquares(int n) {
            //n = 12;
            static vector<int> out;
            if(n+1 > out.size())
            {
                out.insert(out.end(), n-out.size()+1, 0);
            }
            return bfs(out,n);
        }
};
