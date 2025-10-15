import java.util.*;

class Solution {
    Set<Integer> primeSet = new HashSet<>();

    public int solution(String numbers) {
        char[] numArr = numbers.toCharArray();
        boolean[] visited = new boolean[numArr.length];

        // 1자리부터 n자리까지
        for(int i = 1; i <= numbers.length(); i++){
            generatePermutations(numArr, visited, "", i);
        }

        return primeSet.size();
    }

    public void generatePermutations(char[] numbers, boolean[] visited,
                                     String current, int length){

        if(current.length() == length){
            int num = Integer.parseInt(current);
            if(isPrime(num)){
                primeSet.add(num);
            }
            return;
        }

        for(int i = 0; i < numbers.length; i++){
            if(!visited[i]){
                visited[i] = true;
                generatePermutations(numbers, visited, current + numbers[i], length);
                visited[i] = false;
            }
        }
    }

    private boolean isPrime(int n){
        if(n < 2) return false;
        if(n == 2) return true;
        if(n % 2 == 0) return false;

        for(int i = 3; i <= Math.sqrt(n); i += 2){
            if(n % i == 0){
                return false;
            }
        }
        return true;
    }
}