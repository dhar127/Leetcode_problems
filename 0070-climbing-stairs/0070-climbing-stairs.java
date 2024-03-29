class Solution {
    public int climbStairs(int n) {
         if(n==1)
            return 1;
        
        int x=1,y=1,t=0;
        for(int i=2;i<=n;i++){
            t=x+y;
            y=x;
            x=t;
        }
        return t;
    }
}