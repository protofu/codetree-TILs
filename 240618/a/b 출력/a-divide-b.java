import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int a, b;
        a=sc.nextInt();
        b=sc.nextInt();
        
        System.out.print(a/b + ".");

        a%=b;
        for (int i=0;i<20;i++){
            a*=10;
            System.out.print(a/b);
            a%=b;
        }

    }
}