function solution(N) {
    var answer = 0;
    let dp = [1,1] 
    for (let i=2;i<N;i++) {
        dp[i] = dp[i-1] + dp[i-2]
    }
    return (dp[N-1]*2 + (dp[N-2]+dp[N-1])*2);
}

console.log(solution(6));