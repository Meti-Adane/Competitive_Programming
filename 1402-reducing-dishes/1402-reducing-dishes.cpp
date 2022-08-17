class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end());
        int ans = 0;
        
        for (int i=0; i < satisfaction.size(); i++){
            int currSum = satisfaction[i];
            int coff = 2;
            for (int j=i+1; j < satisfaction.size(); j++){
                currSum += (satisfaction[j] * coff);
                coff += 1;
                    
            }
            ans = max(ans, currSum);
        }
        return ans;
    }
};