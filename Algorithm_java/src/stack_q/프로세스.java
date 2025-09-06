

import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int cnt = 0;
        Deque<Task> dq = new ArrayDeque<>();

        // 큐에 작업들 추가
        for(int i = 0; i<priorities.length; i++){
            dq.offer(new Task(i, priorities[i]))
        }

        while(!dq.isEmpty()){

            max = dq.stream()
                    .mapToInt()
        }

        return cnt;
    }
}

class Task{
    int index;
    int pr;

    public Task(int index, int pr){
        this.index = index;
        this.pr = pr;
    }

    public int getIndex(){
        return this.index;
    }

    public int getPr(){
        return this.pr;
    }
}










import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int cnt = 0;
        Deque<Task> dq = new ArrayDeque<>();

        // 큐에 작업들 추가
        for(int i = 0; i < priorities.length; i++){
            Task task = new Task(i, priorities[i]);  // priorities[i] 수정
            dq.offer(task);
        }

        while(!dq.isEmpty()) {
            // 현재 큐에서 최대 우선순위 찾기
            int max = dq.stream()
                    .mapToInt(Task::getPr)
                    .max()
                    .orElse(0);

            Task current = dq.poll();

            // 현재 작업이 최대 우선순위가 아니면 뒤로 보내기
            if(current.getPr() < max) {
                dq.offer(current);
            } else {
                // 최대 우선순위면 실행
                cnt++;
                if(current.getIndex() == location) {
                    break;
                }
            }
        }

        return cnt;
    }
}

class Task{
    int index;
    int pr;

    public Task(int index, int pr){
        this.index = index;
        this.pr = pr;
    }

    public int getIndex(){
        return this.index;
    }

    public int getPr(){
        return this.pr;
    }
}






