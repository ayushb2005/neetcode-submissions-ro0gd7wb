class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int c = 0;
        int j = numbers.length-1;
        for(int i = 0; i<numbers.length; i++ ){
            int c1 = numbers[c];
            int j1 = numbers[j];
            if( c1+ j1 < target){
                c++;
            }else if(c1+j1>target){
                j--;
            }
            else{
                return new int[]{c+1, j+1} ;
            }
        }
        return new int[]{};
        // Set<Integer> set = new HashSet<>();
        // for(int i = 0; i<numbers.length; i++ ){
        //     if(numbers[i]>target){

        //     }else{
        //         set.add(numbers[i]);
        //     }
            
        // }
        // for(int i = 0; i<numbers.length; i++){
        //     if(set.contains(target-numbers[i])){
        //         for(int j = 0; j<numbers.length; j++){
        //             if(numbers[j] == target-numbers[i]){
        //                 return new int[]{i+1,j+1};
        //             }
                    
        //         }
        //     }
        // }
        // return new int[]{};
    }
}
