public class OuterClass{
    public void sleep(){
        System.out.println("Sleeping...");
        try{
            Thread.sleep(5000);
        }catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}