class NumArray {
    public:
        NumArray(vector<int> &nums) {
            array.assign(nums.size()+1,0);
            int tmp = 0;
            for(int i=0;i<nums.size();i++)
            {
                tmp += nums[i];
                array[i+1] = tmp;
            }
        }

        int sumRange(int i, int j) {
            return array[j+1] - array[i];
        }
    private:
        vector<int> array;
};


// Your NumArray object will be instantiated and called as such:
// NumArray numArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
