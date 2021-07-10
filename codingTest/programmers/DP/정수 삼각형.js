function solution(triangle) {
    var answer = 0;
    let dp = [[triangle[0][0]]]
    for (let i=1;i<triangle.length;i++) {
        dp[i]= []
        for (let j=0;j<triangle[i].length;j++) {
            if (j == 0) {
                dp[i][j] = dp[i-1][j]  + triangle[i][j]
            }
            else if (j == triangle[i].length-1) {
                dp[i][j] = dp[i-1][j-1] +  triangle[i][j] 
            }
            else {
                dp[i][j] = Math.max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j] 
            }
        }
    }
    return dp[triangle.length-1].reduce((a,b) => a>b?a:b);
    
}
// Math.max() 최댓값
// reduce()
// dp = [[]] 2차원 배열 
console.log(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]));