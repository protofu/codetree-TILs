import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int a, b, c, avr, sum_all;

        a=sc.nextInt();
        b=sc.nextInt();
        c=sc.nextInt();

        sum_all = a+b+c;
        avr = sum_all / 3;

        System.out.println(sum_all);
        System.out.println(avr);
        System.out.println(sum_all-avr);
                
    }
}