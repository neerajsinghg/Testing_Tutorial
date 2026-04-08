class InputOutputBased{
    public static void main(String[] args) {
       String st = "abc de";  //o/p edc ba 
       String str = st.replaceAll("[\\s+]","");
       StringBuilder sb = new StringBuilder(str);
       String rev = sb.reverse().toString();
       for(int i=0; i<rev.length(); i++){
           if(i!=3){
               System.out.print(rev.charAt(i));
           }
           else{
               System.out.print(" "+rev.charAt(i));
           }
       }
    }
}