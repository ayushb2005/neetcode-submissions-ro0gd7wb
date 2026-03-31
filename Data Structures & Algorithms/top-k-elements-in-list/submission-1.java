
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
            } else {
                map.put(nums[i], 1);
            }
        }
        List<List<Integer>> list = new ArrayList<>(nums.length+1);
        for(int i =0; i<= nums.length; i++){
            list.add(new ArrayList<>());
        }
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            list.get(entry.getValue()).add(entry.getKey());
        }

        int[] arr = new int[k];
        int counter = 0;
        for (int i = list.size() - 1; i >= 1 && counter < k; i--) {
                for (int j = 0; j < list.get(i).size() && counter < k; j++) {
                    arr[counter] = list.get(i).get(j);
                    counter++;
            }
        }
        return arr;

    }
}
