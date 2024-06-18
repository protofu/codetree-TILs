import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num;
        boolean check = false;
        for (int i=0;i<5;i++) {
            num=sc.nextInt();
            if (num%3!=0) check = true;
        }

        if (check) {
            System.out.print(0);
        } else {
            System.out.print(1);
        }
    }
}