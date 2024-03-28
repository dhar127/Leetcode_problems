class Solution {
    public int search(int[] nums, int target) {
         int n = nums.length;
        int l = 0;
        int r = n  - 1;

        while(l <= r) {
            int mid = (l + r) / 2;

            if(nums[mid] == target) {
                return mid;
            }

            // checks if we are in the left side of sorted array
            if(nums[l] <= nums[mid]) { 

                // combined both the logic
                if(target > nums[mid] || target < nums[l]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } 
            // checks if we are in the right side of sorted array
            else {
                if(target < nums[mid] || target > nums[r]) {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            } 
        }
        return -1;        
    }
}