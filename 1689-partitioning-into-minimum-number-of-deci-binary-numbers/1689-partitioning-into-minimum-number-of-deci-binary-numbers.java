class Solution {
    public int minPartitions(String n) {
        int max = 0;
        for(int i=0; i<n.length(); i++){
            int curr = n.charAt(i) - '0';
            max = Math.max(curr, max);
        }
        return max;
    }
}