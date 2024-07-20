class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> vals (nums.begin(),nums.end());
        int max_ans=0;
        for(int num:nums){
            int ans=1;
            if(vals.count(num-1)){
                continue;
            }
            if(vals.count(num))
            {
                while(vals.count(++num)){
                    ans++;
                }
                max_ans=max(ans,max_ans);
            }
        }
        return max_ans;
        return 0;
    }
};