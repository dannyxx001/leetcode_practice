#include <iostream>
#include <map>

using namespace std;

class Solution {
    public:
        int lengthOfLongestSubstring(string s) {
            map<char,int> mymap;
            map<char,int>::iterator it;
            int len = 0, start = -1;
            for(int end=0;end<s.length();end++)
            {
                it = mymap.find(s.at(end));
                if(it != mymap.end())
                    start = max(it->second,start);
                mymap[s.at(end)] = end;
                len = max(len,(end-start));
            }
            return len;
        }
};
