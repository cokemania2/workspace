// https://programmers.co.kr/learn/courses/30/lessons/87389?language=java
// 나머지가 1이 되는 수 찾기.java

class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int i=2; i< n; i++) {
            if ((n-1) % i == 0) {
                return i;
            }
        }
        return n-1;
    }
}