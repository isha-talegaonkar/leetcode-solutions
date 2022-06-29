class Solution {
    public boolean isSubsequence(String s, String t) {
        int l1 = s.length();
        int l2 = t.length();
        int left = 0;
        int right = 0;
        
        while(left<l1 && right<l2){
            if(s.charAt(left) == t.charAt(right)){
                left++;
            }
            right++;
        }
        
        return left == l1;
        
    }
}