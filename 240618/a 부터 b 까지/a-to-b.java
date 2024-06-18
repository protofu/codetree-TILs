import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int a, b;
        a=sc.nextInt();
        b=sc.nextInt();

        while (true) {
            System.out.print(a+" ");
            if (a%2==0) {       // 짝수인 경우
                a += 3;
            } else {            // 홀수인 경우
                a *= 2;
            }
            if (a>b) break;
        }


    }
}