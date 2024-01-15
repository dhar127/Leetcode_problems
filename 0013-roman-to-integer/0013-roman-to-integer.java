class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> map=new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        int res=0;
        int p=0;
        for(int i=s.length()-1;i>=0;i--){
            char c=s.charAt(i);
            int v=map.get(c);
            if(v<p){
                res-=v;
            }
            else{
                res+=v;
            }
            p=v;
        }
        return res;
    }
}