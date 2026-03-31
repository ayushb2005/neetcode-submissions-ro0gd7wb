class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num: nums){
            set.add(num);
        }
        int longest = 0;
        for(int n: set){
            if(set.contains(n-1)){
                continue;
            }else{
                int counter = 1;
                while(set.contains(n+counter)){
                    counter++;
                }
                longest = Math.max(counter,longest);
            }
        }
        return longest;
    }
}
