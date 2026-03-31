class Solution {
    public boolean isPalindrome(String s) {
        ArrayList<Character> arr = new ArrayList<>();
        s = s.toLowerCase();
        String s2 = "";
        for(int i = 0; i<s.length();i++){
            if(s.charAt(i)!=' ' && Character.isLetterOrDigit(s.charAt(i))){
                s2+=s.charAt(i);
            }
        }
        String t= "";
        for(int i = s.length()-1; i>=0;i--){
            if(s.charAt(i)!=' ' && Character.isLetterOrDigit(s.charAt(i))){
                t+=s.charAt(i);
            }
        }
        if(s2.equals(t)){
            return true;
        }
        return false;
    }
}
