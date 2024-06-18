import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int num;
        for (int i=0; i<n; i++) {
            num = sc.nextInt();
            if (num%3==0 && num%2==1) {
                System.out.println(num);
            }
        }
    }
}