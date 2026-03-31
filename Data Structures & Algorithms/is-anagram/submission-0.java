class Solution {
    public boolean isAnagram(String s, String t) {
        // HashMap<Character, Integer> map = new HashMap<>();
        // for(int i =0; i<s.length();i++){
        //     if(map.containsKey(s.charAt(i))){
        //         map.put(s.charAt(i), map.get(s.charAt(i))+1)
        //     }else{
        //         map.put(s.charAt(i),1)
        //     }
        // }
        char[] s1 = s.toCharArray();
        char[] t1 = t.toCharArray();
        Arrays.sort(s1);
        String s1Sort = new String(s1);
        Arrays.sort(t1);
        String t1Sort = new String(t1);
        if(s1Sort.equals(t1Sort)){
            return true;
        }
        return false;
    }
}
