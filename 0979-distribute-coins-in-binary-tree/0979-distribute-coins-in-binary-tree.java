class Solution {
    int k=0;
    public int distributeCoins(TreeNode t) {
        fun(t);
        return k;
    }
    public int[] fun(TreeNode t)
    {
        if(t==null) return new int[]{0,0};
        int l[]=fun(t.left);
        int r[]=fun(t.right);
        int size=1+l[0]+r[0];
        int coins=t.val+l[1]+r[1];
        k+=Math.abs(size-coins);
        return new int[]{size,coins};
    }
}

