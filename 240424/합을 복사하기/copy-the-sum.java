public class Main {
    public static void main(String[] args) {
        int a, b, c;
        a=1;
        b=2;
        c=3;
        a=b=c=(a+b+c);
        System.out.printf("%d %d %d",a,b,c);
    }
}