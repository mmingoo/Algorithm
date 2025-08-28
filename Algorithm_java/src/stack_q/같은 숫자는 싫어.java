import java.util.*;

public class Solution {
    public int[] solution(int []arr) {

        Deque<Integer> q = new ArrayDeque<Integer>();

        for (int num : arr){

            if(q.isEmpty()){
                q.offer(num);
            }else{
                if(q.peekLast() != num){
                    q.offer(num);
                }
            }
        }

        // Deque를 배열로 변환
        int[] answer = new int[q.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = q.poll();
        }
        return answer;

    }
}