class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans; 
        int proximity = INT_MAX;
          
        
          for(int i=0;i<n-2;i++)
          {
              int left = i+1;
              int right = n-1 ;
              
              while (left < right){
                  int sum = nums[i] + nums[left] + nums[right];
                  if (abs(sum-target) < proximity){
                      proximity = abs(sum-target);
                      ans = sum;
                  }
                  if  (sum > target){
                      right -= 1;
                  }else if (sum < target) {
                      left += 1;
                  }else{
                      return target;
                  }
                  
              }
          }
        
        return ans;
    } 
    
};