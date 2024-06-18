import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        // 3 이라면
        // idx 기준 2/ 1 3/ 0 2 4/

        for (int i=0;i<n;i++) {
            for (int j=n;j>i+1;j--) {
                System.out.print(" ");
            }
            for (int k=0;k<i+1;k++) {
                System.out.print("* ");
            }
            System.out.println();
        }
        for (int i=1;i<n;i++) {
            for (int j=0;j<i;j++) {
                System.out.print(" ");
            }
            for (int k=n;k>i;k--) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}