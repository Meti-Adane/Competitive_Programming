class Solution {
public:
    int minCost(string s, vector<int>& neededTime) {
        int ans = 0, i = 0;
        
        while (i < neededTime.size()){
            int maxEffort = neededTime[i], totalEffort =neededTime[i];
            int j = i+1;
            bool isEffortRequired = false;
            
            while(j < neededTime.size() && s[i] == s[j]){
                isEffortRequired = true;
                totalEffort += neededTime[j];
                maxEffort = max(maxEffort, neededTime[j]);
                j += 1;
            }
            
            if (isEffortRequired){
                ans += (totalEffort - maxEffort);
            }
            
            i = j;
            
        }
        return ans;
        
        
        
        
    }
};