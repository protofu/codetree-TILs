import java.util.Scanner;

public class Main {
    static boolean check(int m){
        String s = String.valueOf(m);
        char[] arr = s.toCharArray();
        for (int j=0; j<arr.length;j++){
            if (arr[j] =='3' || arr[j]=='6' || arr[j]=='9'){
                return false;
            }; 
        }
        return true;
    };
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i=1;i<=n;i++){
            if (i%3==0) System.out.print(0+" ");
            else if (!check(i)) System.out.print(0+" ");
            else System.out.print(i+" ");
        }
    }
}