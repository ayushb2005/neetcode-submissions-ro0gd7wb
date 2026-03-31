class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for(int i = 0; i<strs.length; i++){
            char[] charArray = strs[i].toCharArray();
            Arrays.sort(charArray);
            String add = new String(charArray);
            if(map.containsKey(add)){
                map.get(add).add(strs[i]);
            }else{
                map.put(add, new ArrayList<>(Arrays.asList(strs[i])));
            }
        }
        List<List<String>> ret = new ArrayList<>(map.values());
        return ret; 
        // for(int i = 0; i < strs.length; i++){
        //     char[] charArray = strs[i].toCharArray();
        //     Arrays.sort(charArray);
        //     strs[i] = new String(charArray);
        // }
        // Arrays.sort(strs);

        // List<List<String>> list = new ArrayList<>();
        // List<String> group = new ArrayList<>();
        // for(int i = 0; i < strs.length; i++){
        //     if(i > 0 && !strs[i].equals(strs[i-1])){
        //         list.add(group);
        //         group = new ArrayList<>();
        //     }
        //     group.add(strs[i]);
            
        // }
        // list.add(group);
        // return list;
    }
}
