class Solution {
    public int findMin(int[] nums) {
        int n=nums.length;
        if (nums[0]<nums[n-1])
            return nums[0];
        int s=0,e=nums.length-1;
        while(s<e){
            int mid=s+(e-s)/2;
            if(nums[mid]<nums[e]){
                e=mid;
            }
            else {
                s=mid+1;
            }
        }
        return nums[s];
    }
}