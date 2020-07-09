solution("1924",2)

function solution(number, k) {
    arr = number.split('');
    console.log(arr);
    
    for (let i=0;i<k;i++) {
        let max = 0;
        let maxj = 0;
        for (let j=0;j<number.length;j++) {
            if (arr[j] == '#') continue;
            let tmp = Number(number.charAt(j))
            if ( max < tmp ) {
                max = tmp;
                maxj = j;
            }
        }
        arr[maxj] = '#';
    }   
    
    console.log(arr);
}