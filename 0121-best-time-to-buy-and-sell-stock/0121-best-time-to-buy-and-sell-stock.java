class Solution {
    public int maxProfit(int[] prices) {
        int minp=prices[0],maxp=0;
        for(int i=1;i<prices.length;i++){
            int cp=prices[i]-minp;
            if(maxp<cp) maxp=cp;
            if(minp>prices[i]) minp=prices[i];
        }
        return maxp;
    }
}