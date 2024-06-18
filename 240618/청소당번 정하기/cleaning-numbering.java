import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int cnt1, cnt2, cnt3;
        cnt1 = cnt2 = cnt3 = 0;
        for (int i=1;i<=n;i++) {
            // 2일 교실, 3일 복도, 12일 화장실
            // 주기가 긴것이 우선

            if (i%12==0) {
                cnt3++;
            } else if (i%3==0) {
                cnt2++;
            } else if (i%2==0) {
                cnt1++;
            }
        }
        System.out.print(cnt1+" "+cnt2+" "+cnt3);
    }
}