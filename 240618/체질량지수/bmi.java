import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int h, w, ans, bmi;
        h = sc.nextInt();       
        w = sc.nextInt();

        bmi = (10000*w)/h/h;

        if (bmi>=25) {
            System.out.println(bmi);
            System.out.println("Obesity");
        } else {
            System.out.println(bmi);
        } 
    }
}