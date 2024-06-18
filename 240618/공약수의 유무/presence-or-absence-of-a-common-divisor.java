import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a, b;
        a=sc.nextInt();
        b=sc.nextInt();
        boolean check = false;

        for (int i=a;i<=b;i++){
            if (1920%i==0 && 2880%i==0) {
                check = true;
            }
        }
        if (check) {
            System.out.println('1');
        } else {
            System.out.println('0');
        }
    }
}