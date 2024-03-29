class Solution {
    public int hammingWeight(int n) {
        int c=0;
        while(n!=0){
            int g=(n&1);
            if (g==1)
                c+=1;
            n=n>>1;
        }
        return c;
    }
}