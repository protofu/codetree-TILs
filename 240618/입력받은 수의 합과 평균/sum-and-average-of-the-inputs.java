import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int num;
        double avr;
        int sum_num = 0;
        for (int i=0;i<n;i++) {
            num=sc.nextInt();
            sum_num+=num;
        }
        avr = (double) sum_num/n;
        System.out.print(sum_num+" ");
        System.out.printf("%.1f", avr);
    }
}