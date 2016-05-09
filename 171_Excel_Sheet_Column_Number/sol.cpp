class Solution {
    public:
        int titleToNumber(string s) {
            int num = 0;
            for(int i=0;i<s.size();i++)
            {    
                num *= 26;
                num += s[i] - 64;
            }
            return num;
        }
};
