#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

class Solution {
    public:
        bool wordPattern(string pattern, string str) {

            // split str into word
            vector<string> words;
            stringstream ss(str);
            string word;
            while(ss >> word)
                words.push_back(word);

            if(words.size() != pattern.size())
                return false;

            // two unordered map for pattern and str
            unordered_map<char,int> pattern_map;
            unordered_map<string,int>words_map;

            for(int i=0;i<pattern.size();i++)
            {
                if((pattern_map[pattern[i]] || words_map[words[i]]) && (pattern_map[pattern[i]] != words_map[words[i]]))
                    return false;
                else // use first position as record
                    pattern_map[pattern[i]] = words_map[words[i]] = i+1;
            }
            return true;
        }
};
