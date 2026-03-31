class Solution {
    public int[] twoSum(int[] nums, int target) {
        if(nums.length == 2){
            return new int[]{0, 1};
        }

        for(int i =0; i<nums.length; i++){
            for(int j=i+1; j<nums.length;j++){
                if(nums[i]+nums[j]==target && i!=j){
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{0};
    }
}
