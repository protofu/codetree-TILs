public class Main {
    public static void main(String[] args) {
        int a, b, c, tmp, tmp1;
        a=5;
        b=6;
        c=7;
        tmp = a;
        a = c;
        tmp1 = b;
        b = tmp;
        c = tmp1;
        System.out.printf("%d\n%d\n%d", a, b, c);
    }
}