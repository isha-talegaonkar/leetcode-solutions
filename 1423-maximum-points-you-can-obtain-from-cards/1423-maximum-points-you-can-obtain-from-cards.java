class Solution {
    public int maxScore(int[] cardPoints, int k) {
        int n = cardPoints.length;
        
        int[] frontSet = new int[k+1];
        int[] rearSet = new int[k+1];
        
        frontSet[0] = rearSet[0] = 0;
        
        for(int i=0; i<k; i++){
            frontSet[i+1] = cardPoints[i] + frontSet[i];
            rearSet[i+1] = cardPoints[n-i-1] + rearSet[i];
        }
        
        int maxScore = 0;
        
        for(int i=0; i<=k; i++){
            int curr = frontSet[i] + rearSet[k-i];
            maxScore = Math.max(maxScore, curr);
        }
        
        return maxScore;
    }
}