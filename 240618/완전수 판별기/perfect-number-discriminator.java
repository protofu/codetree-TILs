import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int cnt = 0;
        // 완전 수
        for (int i=1;i<n;i++) {
            if (n%i==0) {
                cnt += i;
            }
        }
        if (cnt == n) {
            System.out.println('P');
        } else {

            System.out.println('N');
        }
    }
}