import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n;
        int[] people = new int[n];

        // 도난 처리
        for(int l : lost){
            people[l-1]--;
        }

        // 여벌 처리
        for(int r : reserve){
            people[r-1]++;
        }

        // 체육복 빌려주기
        for(int i = 0; i < n; i++){

            // 잃어버린 경우
            if(people[i] == -1){

                // 앞사람이 여벌이 있는 경우
                if(i-1 >= 0 && people[i-1] == 1){
                    people[i-1]--;
                    people[i]++;
                }
                // 뒷사람이 여벌이 있는 경우
                else if(i+1 < n && people[i+1] == 1){
                    people[i+1]--;
                    people[i]++;
                }
                // 빌릴 수 없는 경우
                else{
                    answer--;
                }
            }
        }

        return answer;
    }
}