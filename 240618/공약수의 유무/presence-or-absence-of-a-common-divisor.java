import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a, b;
        a=sc.nextInt();
        b=sc.nextInt();
        boolean check = false;

        if (1920%a==0 && 2880%a==0) {
            check = true;
        } else if (1920%b==0 && 2880%b==0) {
            check = true;
        }
        
        if (check) {
            System.out.println('1');
        } else {
            System.out.println('0');
        }
    }
}