console.log(solution(0));

function solution(n) {
    let answer = []
    let i = 0.0;
    if (n <  || n > 10 || n % 1 != 0 || Number(n) != n)
        return []
    while (i <= n) { 
       answer.push((i.toFixed(1).toString())); 
        i = i + 0.1
    }
    return answer;
}