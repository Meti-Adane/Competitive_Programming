class Solution {
    long int ans = 0;
    unordered_map<long int, long int> dp;
    int mod = pow(10, 9) + 7;
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        
        for (int i=0; i < arr.size(); i++){
            dp[arr[i]] = 1;
        }
        
        sort(arr.begin(), arr.end());
        recurse(0, arr);
        return ans % mod;
        
    }
    
    long int recurse(int index, vector<int>& arr){
            if (index >= arr.size()){
                return 0;
            }
            
            int parent = arr[index];
            
            for (int j=0; j < index; j++){
                int child1 = arr[j], child2 = parent / double(child1);
                if (parent % child1 != 0) continue;
                
                dp[parent] += (dp[child1] * dp[child2]);
                
            }
            recurse(index+1, arr);
            
            ans += dp[parent];
            return dp[parent];
        }
};