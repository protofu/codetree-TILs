import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int test = n-1;
        while (test!=1) {
            if (n%test == 0) {
                System.out.println("C");
                break;
            }
            test--;
            if (test==1){
                System.out.println("N");
            }
        }
    }
}