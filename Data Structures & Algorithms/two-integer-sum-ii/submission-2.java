class Solution {
    public int[] twoSum(int[] numbers, int target) {
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i<numbers.length; i++ ){
            set.add(numbers[i]);
        }
        for(int i = 0; i<numbers.length; i++){
            if(set.contains(target-numbers[i])){
                for(int j = 0; j<numbers.length; j++){
                    if(numbers[j] == target-numbers[i]){
                        return new int[]{i+1,j+1};
                    }
                    
                }
            }
        }
        return new int[]{};
    }
}
