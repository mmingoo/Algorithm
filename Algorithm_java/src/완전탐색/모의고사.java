class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int w  = 0;
        int h = 0;
        int a = 0;

        for(int i = 0; i<sizes.length; i++){
            if (sizes[i][0] < sizes[i][1]){
                a = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = a;
            }
        }
        for(int i  = 0; i < sizes.length; i++){
            if (w < sizes[i][0]){
                w = sizes[i][0];
            }

            if(h < sizes[i][1]){
                h = sizes[i][1];
            }

        }
        System.out.println(w);
        System.out.println(h);


        answer = w * h;
        return answer;
    }
}