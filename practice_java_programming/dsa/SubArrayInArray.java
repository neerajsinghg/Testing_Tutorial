package dsa;
class SubArrayInArray {
	 public static void main(String[] args) {
	       int[] no= {4,5,6,7,8,9};
	       int[] no1 = {15,18,16};
	       boolean match = false;
	       for(int i=0; i<no1.length; i++){
	           for(int j=0; j<no.length; j++){
	               if(no1[i]==no[j]){
	                   match = true;
	               }
	               else{
	                   match=false;
	               }
	           }
	       }if(match){
	       System.out.println("this is subarray");
	       }
	       else{
	           System.out.println("not sub array");
	       }
	       
	    }
      }
