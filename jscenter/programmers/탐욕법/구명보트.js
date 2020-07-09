console.log(solution([70, 50, 80, 50],100));
// 2H 46M
// 문제를 잘 읽자 
function solution(people, limit) {
    let answer =0;
    let boat;
    let last = people.length-1;
    people.sort((a,b)=>b-a);
    for (let i=0;i<=last;i++) {
        boat = people[i];
        if (boat + people[last] <= limit){
             last--;
        }
        answer++;
    }    
    return answer;
}