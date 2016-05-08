class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            int num_of_non_zero = 0;
            for(int i=0;i<nums.size();i++)
                if(nums[i] != 0)
                    nums[num_of_non_zero++] = nums[i];
            for(int i=num_of_non_zero;i<nums.size();i++)
                nums[i] = 0;
        }
};
