package smartpractice;

import java.util.Arrays;
class SecondLargestSmallestElementOfArray{
    public static void main(String[] args){
    int [] nums = {5,6,7,4,2,3};//2
    Arrays.sort(nums);
    int largestNo = nums[nums.length-1], smallestNo=nums[0];
    int secondLargestNo =-1, secondSmallestNo=-1;
    
    
    for(int i=nums.length-2; i>= 0; i--){
        if(nums[i]<largestNo){
            secondLargestNo =nums[i];
            break;
        }}
        if(secondLargestNo ==-1){
            System.out.println("no is not found");
        }
        else{
            System.out.println("second largest no is found = "+secondLargestNo);
        
    }
      for(int i=1; i<=nums.length-1; i++) {
    	  if(nums[i]>smallestNo) {
    		  secondSmallestNo=nums[i];
    		  break;
    	  }
      }
      if(secondSmallestNo ==-1){
          System.out.println("no is not found");
      }
      else{
          System.out.println("second smallest no is found = "+secondSmallestNo);
      
  }
    } 
}