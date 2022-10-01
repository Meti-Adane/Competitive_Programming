class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int prefixsum = 0;
        int ans = nums.size() + 1;
        int left = 0;
        
        for (int i = 0; i < nums.size(); i++){
            prefixsum += nums[i];
            while (prefixsum >= target){
                ans = min(ans, i-left+1);
                prefixsum -= nums[left++];
            }
                
        }
        if (ans <= nums.size()) return ans;
        return 0;
    }
};