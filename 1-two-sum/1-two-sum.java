class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        
        for(int i=0; i<nums.length; i++)
        {
            Integer element2 = (Integer)(target - nums[i]);
            //System.out.println("i: "+i+" element2: "+element2);
            if(hash.containsKey(element2))
            {
                int positions[] = {hash.get(element2), i};
                return positions;
            }
            hash.put(nums[i], i);
        }
        return null;

    }
}