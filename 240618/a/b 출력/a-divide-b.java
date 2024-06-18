import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        double a, b;
        a=sc.nextDouble();
        b=sc.nextDouble();
        double ans = a/b;

        // System.out.println(ans);
        System.out.printf("%.20f", ans);
    }
}