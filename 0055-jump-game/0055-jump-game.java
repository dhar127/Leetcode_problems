class Solution {
    public boolean canJump(int[] nums) {
        int s=0,m=0;
        for(int i=0;i<nums.length;i++){
             if(i>m){
                return false;
            }
            s=(i+nums[i]);
            if(s>m){
                m=s;
            }
           
        }
        return true;
    }
}