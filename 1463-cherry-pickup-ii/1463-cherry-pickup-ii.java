class Solution {
    public int cherryPickup(int[][] grid) {
        int m=grid.length;
        int n=grid[0].length;
        int [][][]dp=new int[m][n][n];
        for(int j=0;j<n;j++){
            for(int k=0;k<n;k++){
                if(j==0 && k==n-1){
                    dp[0][j][k]=grid[0][0]+grid[0][n-1];
                }
                else{
                    dp[0][j][k]=Integer.MIN_VALUE;
                }
            }
        }
        for(int i=1;i<m;i++){
            for(int j=0;j<n;j++){
                for(int k=j+1;k<n;k++){
                    int max=Integer.MIN_VALUE;
                    for(int a=-1;a<=1;a++){
                        for(int b=-1;b<=1;b++){
                            if(j+a>=0 && j+a<n && k+b>=0 && k+b<n){
                                max=Math.max(max,dp[i-1][j+a][k+b]);
                            }
                        }
                    }
                    dp[i][j][k]=max+grid[i][j]+grid[i][k];
                }
            }
        }
        int ans=Integer.MIN_VALUE;
        for(int j=0;j<n;j++){
            for(int k=j+1;k<n;k++){
                ans=Math.max(ans,dp[m-1][j][k]);
            }
        }
        return ans;
    }
}