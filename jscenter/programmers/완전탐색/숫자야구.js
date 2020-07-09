console.log(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]));


function solution(baseball) {
    let arr=[];
    for (let i=123;i<=987;i++) {
        let a = String(i);
        a = a.split('');
        if (a[0] == a[1] || a[0] == a[2] || a[1] == a[2] || a[0] == 0 || a[1] == 0 || a[2] ==0) 
            continue;
        else {
            let flag = true;
            for (let j=0;j<baseball.length;j++) {
                let strike = 0;
                let ball = 0;
                let b = String(baseball[j][0]).split('');
                
                for (let k=0;k<3;k++) {
                    if (a[k] == b[k]) strike++;
                    else if (b.indexOf(a[k]) != -1) ball++;
                }
                if (strike == baseball[j][1] && ball == baseball[j][2]) 
                    continue;
                else 
                    flag = false;            
            }
            if (flag == true)
                arr.push(a);
        }
            
    }
    return(arr.length);
}