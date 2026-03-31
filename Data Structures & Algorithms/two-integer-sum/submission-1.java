class Solution {
    public int[] twoSum(int[] nums, int target) {
        // if(nums.length == 2){
        //     return new int[]{0, 1};
        // }

        // for(int i =0; i<nums.length; i++){
        //     for(int j=i+1; j<nums.length;j++){
        //         if(nums[i]+nums[j]==target && i!=j){
        //             return new int[]{i, j};
        //         }
        //     }
        // }
        // return new int[]{0};
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i =0; i<nums.length;i++){
            int count = target-nums[i];
            if(map.containsKey(count)){
                return new int[]{map.get(count),i};
            }else{
                map.put(nums[i],i);
            }
        }
        return new int[]{};
    }
}
