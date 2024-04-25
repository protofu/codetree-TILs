import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h, w;
        h=sc.nextInt();
        w=sc.nextInt();
        int bmi = (10000*w)/(h*h);
        System.out.println(bmi);
        if (bmi>=25) System.out.print("Obesity");
    }
}