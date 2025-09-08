
import java.util.*;

class Solution {
    class Truck {
        int weight;
        int move;

        public Truck(int weight) {
            this.weight = weight;
            this.move = 1;
        }

        public void moving() {
            move++;
        }
    }

    public int solution(int bridgeLength, int weight, int[] truckWeights) {
        Queue<Truck> waitQ = new LinkedList<>();
        Queue<Truck> moveQ = new LinkedList<>();

        for (int t : truckWeights) {
            waitQ.offer(new Truck(t));
        }

        int answer = 0;
        int curWeight = 0;

        while (!waitQ.isEmpty() || !moveQ.isEmpty()) {
            answer++;

            // 이동큐가 비어있을 때 추가, 이후는 패스
            if (moveQ.isEmpty()) {
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
                continue;
            }

            // 이동큐에 있는 트럭들 한칸씩 이동
            for (Truck t : moveQ) {
                t.moving();
            }


            // 이동 후 길이보다 크면 poll
            if (moveQ.peek().move > bridgeLength) {
                Truck t = moveQ.poll();
                curWeight -= t.weight;
            }



            if (!waitQ.isEmpty() && curWeight + waitQ.peek().weight <= weight) {
                Truck t = waitQ.poll();
                curWeight += t.weight;
                moveQ.offer(t);
            }
        }

        return answer;
    }
}