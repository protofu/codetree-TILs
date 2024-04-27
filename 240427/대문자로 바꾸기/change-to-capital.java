import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String s;
        for (int i=0;i<5;i++){
            s=sc.nextLine();
            s=s.toUpperCase();
            System.out.println(s);
        }
    }
}