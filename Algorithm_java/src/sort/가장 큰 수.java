import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        // String 배열로 변환
        String[] strNumbers = new String[numbers.length];
        for(int i = 0; i< numbers.length; i++){
            strNumbers[i] = String.valueOf(numbers[i]);
        }


        Arrays.sort(strNumbers, (a,b) -> (b+a).compareTo(a+b));
        System.out.println(Arrays.toString(strNumbers));
        if(strNumbers[0].equals("0")){
            return "0";
        }

        StringBuilder answer = new StringBuilder();

        for(String str : strNumbers){
            answer.append(str);
        }
        return answer.toString();
    }
}