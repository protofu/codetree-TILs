import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int ss = 0;
        int cnt = 0;
        double avr;
        int[] arr = new int[10];
        for (int i=0;i<10;i++){
            arr[i] = sc.nextInt();
            if (arr[i]>=250) break;
            ss += arr[i];
            cnt+=1;
        };
        avr = (double)ss/cnt;
        System.out.printf("%d %.1f", ss, avr);

    }
}