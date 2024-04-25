import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b;
        a=sc.nextInt();
        b=sc.nextInt();
        while(a<=b){
            System.out.print(a+" ");
            if (a%2==1) a*=2;
            else a+=3;
            
        }
    }
}