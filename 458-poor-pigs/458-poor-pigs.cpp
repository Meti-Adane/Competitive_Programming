class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int maxTest = (minutesToTest / minutesToDie) + 1; 
        double exp = log2(buckets) / log2(double(maxTest));
        
        return ceil(exp);
        
    }
};

/* [To Do] python equivalent of this code produces error due to inaccuracy of log function calculation 125 log 5 returns 3.000000004 taking a ceil of that produces 4 rather than the desired answer 3 */