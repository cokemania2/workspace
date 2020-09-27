function solution(N, number) {
    var answer = 0;
    let a = []
    for (let i = 1; i <=9;i++) {
        let s = ''
        for (let j =0;j<i;j++) {
            s = s + String(N)
        }
        a.push([Number.parseInt(s)])
    }
    for (let i = 0 ; i<a.length; i++) {
        if (a[i].some((a) => a == number)) {
            return i+1
        }
        if (i == 8) break
        for (let j =0;j<a[i].length;j++) {
                a[i+1].push(a[i][j] + N)
                a[i+1].push(a[i][j] - N)
                a[i+1].push(N-a[i][j])
                a[i+1].push(a[i][j] * N)
                a[i+1].push(parseInt(a[i][j]/N))
                if (a[i][j] != 0){
                    a[i+1].push(parseInt(N/a[i][j]))
                }
        }
        a[i+1] = Array.from(new Set(a[i+1]))
        console.log(a[i+1]);
        
    }
    return -1

}
console.log(solution(5,31168));