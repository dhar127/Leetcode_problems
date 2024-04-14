class Solution {
    int currentVal = 0, currentCount = 0, maxCount = 0;
    List<Integer> l = new ArrayList<>();
    
    public int[] findMode(TreeNode root) {
        findHelper(root);
        int[] result = new int[l.size()];
        for (int i = 0; i < l.size(); i++) {
            result[i] = l.get(i);
        }
        return result;
    }
    
    public void findHelper(TreeNode root) {
        if (root == null) return;
        findHelper(root.left);
        if (root.val == currentVal) {
            currentCount++;
        } else {
            currentVal = root.val;
            currentCount = 1;
        }
        if (currentCount == maxCount) {
            l.add(root.val);
        } else if (currentCount > maxCount) {
            l.clear();
            l.add(root.val);
            maxCount = currentCount;
        }
        findHelper(root.right);
    }
}
