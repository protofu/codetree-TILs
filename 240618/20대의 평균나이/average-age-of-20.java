import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int age;
        int cnt = 0;
        int total_age = 0;
        while (true) {
            age = sc.nextInt();
            if (age>=30 || age < 20) {
                break;
            }
            total_age += age;
            cnt++;
        }
        double avr = (double) total_age/cnt;
        System.out.printf("%.2f", avr);
    }
}