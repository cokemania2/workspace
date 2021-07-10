console.log(solution([12,1213]));

function solution(numbers) {
    var answer = numbers.map(v=>v+'')
    .sort((a,b) => (b+a)*1 - (a+b)*1)
    .join('');

    return answer[0]==='0'?'0':answer;
    // numbers.sort((a,b) => { 
    //     let A = String(a);
    //     let B = String(b);
    //     if (A.length == B.length && A.charAt(0) != B.charAt(0)) 
    //         return B.charAt(0) - A.charAt(0);
    //     else {
    //         let x = 0;
    //         let Aflag = false;
    //         let Bflag = false;
    //         let y = 0;
    //         while (true) {
    //             if (A.charAt(x) != B.charAt(y)) {        
    //                 //console.log(`${B} ${B.charAt(x)} ssv ${A} ${ A.charAt(y)}`);               
    //                 return (B.charAt(y) - A.charAt(x));
    //             }
    //             else {
    //                 if (x < A.length-1)
    //                     x++;
    //                 else {
    //                     x=0;
    //                     Aflag = true;
    //                 }
    //                 if (y < B.length-1) 
    //                     y++;
    //                 else {
    //                     y=0;
    //                     Bflag = true;
    //                 }
    //             }
    //             if (Aflag == true && Bflag == true) {
    //                 return (B.charAt(y) - A.charAt(x));
    //             }
    //         }
    //     }
    // })
    // answer = numbers.join('');
    // if (parseInt(answer)==0)
    //      return '0'
    // else
    //      return answer;
}
