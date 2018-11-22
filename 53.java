import java.util.*;
import java.lang.*;
import java.io.*;
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
	Scanner ob=new Scanner(System.in);
	int x=ob.nextInt();
	int n;
	int sum=0;
	while(x!=0)
	{
		n=x%10;
		sum=sum+n;
		x=x/10;
	}
	System.out.println(sum);
	}
}
