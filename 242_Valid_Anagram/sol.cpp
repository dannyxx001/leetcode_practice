class Solution {
    public:
        bool isAnagram(string s, string t) {
            if(s.size() != t.size())
                return false;

            map<char,int> s_map;
            map<char,int> t_map;

            for(int i=0;i<s.size();i++)
            {
                if(s_map[s[i]])
                    s_map[s[i]]++;
                else
                    s_map[s[i]] = 1;
                if(t_map[t[i]])
                    t_map[t[i]]++;
                else
                    t_map[t[i]] = 1;
            }

            if(s_map.size() != t_map.size())
                return false;

            for(map<char,int>::iterator it=s_map.begin();it!=s_map.end();++it)
                if(it->second != t_map[it->first])
                    return false;

            return true;
        }
};
