package hash;

import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> map = new HashMap<>();

        //베얄 순회하면서 값 넣기
        for(int i = 0 ; i<clothes.length; i++){
            map.put(clothes[i][1], map.getOrDefault(clothes[i][1], 0)+1);
        }


        // 배열의 각 value값 읽어서 1 더한 다음 곱한다
        for(Integer cnt : map.values()){
            answer *= (cnt+1);
        }

        return answer-1;
    }
}