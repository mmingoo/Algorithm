import java.util.*;

class Task{
    int working_time;
    int request_time;
    int work_num;

    public Task(int working_time, int request_time, int work_num){
        this.working_time = working_time;
        this.request_time = request_time;
        this.work_num = work_num;
    }
}

class Solution {
    public int solution(int[][] jobs) {

        int current_time = 0;
        int total_return_time = 0;
        int completed_jobs = 0;

        // 요청시간 순으로 정렬된 작업 큐
        Queue<Task> taskQ = new LinkedList<>();

        // 작업시간 우선 정렬 (SJF)
        PriorityQueue<Task> readyQ = new PriorityQueue<>(
                Comparator.comparing((Task t) -> t.working_time)
                        .thenComparing(t -> t.request_time)
                        .thenComparing(t -> t.work_num)
        );

        // 작업들을 요청시간 순으로 정렬해서 taskQ에 추가
        Arrays.sort(jobs, (a, b) -> a[0] - b[0]);
        for(int i = 0; i < jobs.length; i++){
            taskQ.offer(new Task(jobs[i][1], jobs[i][0], i));
        }

        while(completed_jobs < jobs.length) {

            // 현재 시간까지 요청된 모든 작업을 readyQ로 이동
            while(!taskQ.isEmpty() && taskQ.peek().request_time <= current_time) {
                readyQ.offer(taskQ.poll());
            }

            if(!readyQ.isEmpty()) {
                // 가장 짧은 작업 실행
                Task currentTask = readyQ.poll();
                current_time += currentTask.working_time;

                // 반환시간 = 현재시간 - 요청시간
                total_return_time += (current_time - currentTask.request_time);
                completed_jobs++;

            } else {
                // 실행할 작업이 없으면 다음 작업 요청시간으로 점프
                if(!taskQ.isEmpty()) {
                    current_time = taskQ.peek().request_time;
                }
            }
        }

        return total_return_time / jobs.length;
    }
}