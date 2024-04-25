import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        if (a<=b) c=b-a;
        else c = a-b;
        System.out.print(c);
    }
}