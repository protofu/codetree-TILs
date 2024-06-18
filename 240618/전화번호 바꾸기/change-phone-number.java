import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        String[] sarr = s.split("-");

        System.out.println(sarr[0]+"-"+sarr[2]+"-"+sarr[1]);
    }
}