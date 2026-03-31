class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            hm.put(nums[i],i);
        }
        int a = 0;
        int b = 0;
        for(int i = 0; i<nums.length; i++){
            int difference = target - nums[i];
            if(hm.containsKey(difference) && i!=hm.get(difference)){
                 return new int[] {i,hm.get(difference)};
            }
        }
        return new int[] {0,0} ;
    }
}
