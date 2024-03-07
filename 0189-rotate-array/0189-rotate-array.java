class Solution {
    public void rotate(int[] nums, int k) {
        //to keep track of the length of nums array
        int count = 0;
        
        for(int start=0; count<nums.length; start++){
            int currentIndex = start;
            int currentElement = nums[start];
            do{
                int nextIndex = (currentIndex + k) % nums.length;
                
                int temp = nums[nextIndex];
                nums[nextIndex] = currentElement;
                currentElement = temp;
                
                currentIndex = nextIndex;
                count++;
            }while(start != currentIndex);
        }
    }
}