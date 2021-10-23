import java.util.HashMap;
import java.util.Map.Entry;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        HashMap<String, Integer> map = new HashMap();
        int answer = 0;
        int count = 0;
        
        for (int i=0;i<cities.length;i++) {
            String city = cities[i].toUpperCase();
            if (map.containsKey(city)) {
                answer += 1;
                map.put(city, count++);
            } else {
                answer += 5;
                if (map.size() < cacheSize) {
                    map.put(city,count++);
                } else {
                    Entry<String, Integer> min = null;
                    for (Entry<String, Integer> entry : map.entrySet()) {
                        if (min == null || min.getValue() > entry.getValue()) {
                            min = entry;
                        }
                    }
                    if (min != null) {
                        map.remove(min.getKey());
                        map.put(city,count++);
                    }
                    
                }
            }
        }
            
        return answer;
    }
}