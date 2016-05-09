class Solution {
    public:
        bool containsDuplicate(vector<int>& nums) {
            map<int,int> num_counter;
            for(int i=0;i<nums.size();i++)
                if(num_counter[nums[i]])
                    return true;
                else
                    num_counter[nums[i]] = 1;
            return false;
        }
};
