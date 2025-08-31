import java.util.*;
class Solution {

    public int[] solution(int[] progresses, int[] speeds) {
        int days = 0;
        int cnt = 0;
        List<Integer> list = new ArrayList<>();
        Deque<Integer> q = new ArrayDeque<>();

        for(int i = 0; i < progresses.length; i++){import java.util.*;
            class Solution {

                public int[] solution(int[] progresses, int[] speeds) {
                    int days = 0;
                    int cnt = 0;
                    List<Integer> list = new ArrayList<>();
                    Deque<Integer> q = new ArrayDeque<>();

                    for(int i = 0; i < progresses.length; i++){
                        // System.out.println("progresses :  " + progresses[i]);
                        // 현재 작업이 며칠만에 100 넘어가는지 계산
                        days = (int)Math.ceil((double)(100 - progresses[i]) / speeds[i]);

                        if(q.isEmpty()){
                            // System.out.println("큐에 추가하는 days : " + days );

                            q.offer(days);

                        }else{

                            // System.out.println("q.peek() : " +q.peek() );
                            if(q.peek() >= days){


                                // System.out.println("큐에 추가하는 days : " + days );
                                q.offer(days);
                            }

                            else{
                                cnt = q.size();
                                q.clear();
                                // System.out.println("큐 초기화");
                                // System.out.println("큐에 넣을 days : " + days);
                                q.offer(days);

                                list.add(cnt);
                            }

                        }


                    }
                    cnt = q.size();
                    list.add(cnt);

                    int[] answer = new int[list.size()];

                    for(int i =0; i<answer.length; i++){
                        answer[i] = list.get(i);
                    }
                    return answer;
                }
            }
            // System.out.println("progresses :  " + progresses[i]);
            // 현재 작업이 며칠만에 100 넘어가는지 계산
            days = (int)Math.ceil((double)(100 - progresses[i]) / speeds[i]);

            if(q.isEmpty()){
                // System.out.println("큐에 추가하는 days : " + days );

                q.offer(days);

            }else{

                // System.out.println("q.peek() : " +q.peek() );
                if(q.peek() >= days){


                    // System.out.println("큐에 추가하는 days : " + days );
                    q.offer(days);
                }

                else{
                    cnt = q.size();
                    q.clear();
                    // System.out.println("큐 초기화");
                    // System.out.println("큐에 넣을 days : " + days);
                    q.offer(days);

                    list.add(cnt);
                }

            }


        }
        cnt = q.size();
        list.add(cnt);

        int[] answer = new int[list.size()];

        for(int i =0; i<answer.length; i++){
            answer[i] = list.get(i);
        }
        return answer;
    }
}