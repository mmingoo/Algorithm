import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        int firstSco = 0;
        int secondSco = 0;
        int newSco = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        for(int sco : scoville){

            heap.offer(sco);
        }


        while(heap.peek() < K){
            answer ++;

            if(!heap.isEmpty() && heap.size() != 1 ){
                firstSco = heap.poll();
                secondSco = heap.poll();

            }else{
                return -1;

            }


            newSco = firstSco + secondSco*2;

            heap.offer(newSco);

        }

        return answer;
    }
}