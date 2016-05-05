#include <iostream>
#include <vector>

using namespace std;

class Solution {
    public:
        vector<vector<int>> generate(int numRows) {
            //numRows = 5;
            vector<vector<int>> out;
            for(int i=0;i<numRows;i++)
            {
                vector<int> tmp(i+1,1);
                out.push_back(tmp);
                if(i > 1)
                {
                    for(int j=1;j<i;j++)
                    {
                        out[i][j] = out[i-1][j-1] + out[i-1][j];
                    }
                }
            }
            return out;
        }
};
