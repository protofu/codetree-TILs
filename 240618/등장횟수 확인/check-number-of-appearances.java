import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int num;
        int cnt = 0;
        for (int i=0;i<5;i++) {
            num=sc.nextInt();
            if (num%2==0) cnt++;
        }       
        System.out.println(cnt);
    }
}