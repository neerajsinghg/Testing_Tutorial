public class Exceptionss{
    public static void main(String[] args) {
        try{
            int age = 15;
            if(age<18){
                throw new ArithmeticException("you are not allow");
            }
            System.out.println("you are eleigible");
        }
        catch(ArithmeticException e){
            System.out.println("program continue .. "+e.getMessage());
        }
    }
}