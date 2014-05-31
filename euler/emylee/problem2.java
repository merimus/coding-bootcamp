
public class problem2 {
	private static problem2 p2= new problem2();
	private static int ans, temp = 1, next = 0;
	public void problem2(int n){
		for(int i = 1; i < n; ){
			if(i%2 ==0)	{
				ans = i + ans;
			}
			next = temp+i;
			System.out.print(i);
			temp =i;
			i = next;
			
		
		}
	}
	public static void main(String args[]){
		p2.problem2(4000000);
		System.out.print("\n"+ans);
	}
}
