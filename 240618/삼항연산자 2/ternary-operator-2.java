import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int a;
        char b;
        a=sc.nextInt();

        b = a == 1 ? 't' : 'f';

        System.out.println(b); 
    }
}