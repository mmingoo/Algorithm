import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> list = new ArrayList<>();
        int[] answer = {};
        int i = 0;
        int j = 0;
        int k = 0;

        for(int m = 0; m< commands.length; m++){
            i = commands[m][0];
            j = commands[m][1];
            k = commands[m][2];

            int[] arr = Arrays.copyOfRange(array, i-1, j);
            Arrays.sort(arr);
            System.out.println(Arrays.toString(arr));

            list.add(arr[k-1]);

        }

        int[] result = list.stream().mapToInt(Integer :: intValue).toArray();

        return result;
    }
}