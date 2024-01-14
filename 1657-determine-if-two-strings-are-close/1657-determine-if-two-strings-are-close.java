class Solution {
    public boolean closeStrings(String word1, String word2) {
        Set<Character> s1=new HashSet<>();
        Set<Character> s2=new HashSet<>();
        int x[]=new int[26];
        int y[]=new int[26];
        for (char c:word1.toCharArray()){
            x[c-'a']+=1;
            s1.add(c);
        }
        for (char c:word2.toCharArray()){
            y[c-'a']+=1;
            s2.add(c);
        }
        Arrays.sort(x);
        Arrays.sort(y);
        return Arrays.equals(x,y) && s1.equals(s2);
    }
}