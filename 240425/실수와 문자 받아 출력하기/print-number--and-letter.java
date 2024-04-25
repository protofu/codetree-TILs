import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        double b = sc.nextDouble();
        double c = sc.nextDouble();
        System.out.printf("%s\n%.2f\n%.2f", a, b, c);
    }
}