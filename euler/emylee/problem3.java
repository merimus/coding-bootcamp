
public class problem3 {
	private long x = 600851475143L;
	private long ans = 0;
	private boolean prime;
	private static problem3 p3 = new problem3();
	public long problem3(){
		
		long highestPrime = -1;
	    for(int i = 1; i < Math.sqrt(x); i++){
	    	prime = true;
	    	if(x%i == 0){
	    		for(int j = 2; j < i; j++){
	    			if(i%j == 0){
	    				prime = false;
	    			}
	    			else{
	    		
	    			}
	    			
	    		}
	    		if(prime){
	    			highestPrime = i;
	    		}
	    	}
	    		
	    
	    	else{
	    	}
	    }	    
	    return highestPrime;
	}
	public static void main (String args[]){
		long s = p3.problem3();
		System.out.println(s);
	}
}
