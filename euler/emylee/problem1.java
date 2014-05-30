
public class problem1 {
	private static problem1 p1 = new problem1();
	
	public int problem1(int n){
		int ans = 0;
		for(int i = 1; i < n; i++){
			if (i % 3 == 0){
				ans = ans + i;
			}
			else if( i % 5 == 0){
				ans = ans + i;
			}
		}
		return ans;
	}
	public static void main (String args[]){
		int s = p1.problem1(1000);
		System.out.println(s);
	}
}
