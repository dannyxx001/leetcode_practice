class Solution {
    public:
        string convertToTitle(int n) {
            return n < 27 ? string(1,64+n) : convertToTitle((n-1)/26) + convertToTitle((n-1)%26+1);
        }
};
