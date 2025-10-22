// Java program for simple calculator
import java.util.Scanner;

// Driver class
public class BasicCalc {
    // main function
    public static void main(String[] args)
    {
        int num1, num2;
        
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the numbers:");

        num1 = sc.nextInt();
        num2 = sc.nextInt();
        double sum = num1 + num2;
        System.out.println(num1 + " + " + num2 + " = " + sum);
        
        sc.close();
    }
}