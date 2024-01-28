class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int r=matrix.length,c=matrix[0].length;
        for(int i=0;i<r;i++){
            for(int j=1;j<c;j++){
                matrix[i][j]+=matrix[i][j-1];
            }
        }
        int count=0;
        for(int c1=0;c1<c;c1++){
            for(int c2=c1;c2<c;c2++){
                Map<Integer,Integer> map=new HashMap<>();
                map.put(0,1);
                int s=0;
                for(int row=0;row<r;row++){
                  s+=matrix[row][c2]-(c1>0?matrix[row][c1-1]:0);
                  count+=map.getOrDefault(s-target,0);  
                map.put(s,map.getOrDefault(s,0)+1);
                }
            }
    }
        return count;
}
}