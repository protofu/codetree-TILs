import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b, maxNum;
        a=sc.nextInt();
        b=sc.nextInt();
        maxNum=a<=b ? b:a;
        System.out.print(maxNum);
    }
}