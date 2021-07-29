import java.lang.*;
import java.util.Scanner;
import java.util.Arrays;

public class Alphanames
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter n");
        int n = sc.nextInt();
        String names[] = new String[n];
        for(int i=0;i<n;i++)
        {
            names[i] = sc.next();
        }
        String st = "";
            
        for(int i=0;i<n;i++)
        {
            char charArray[] = names[i].toCharArray();
            Arrays.sort(charArray);
           for(int j=0;j<charArray.length;j++)
            {
                st = st + charArray[j];
            }
                
            if (names[i].compareTo(st)<=0)
            {
                System.out.println("NO");
            }
                
            else
            {
                System.out.println("YES");
            }

            st = "";
        }
    }
}