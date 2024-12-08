//Single line comment

/*
Multiline
comment
*/

public class MyJavaProgram{
    private static final String CONSTANT = "Constant String";
    private OuterClass outerClass;
    private Unused unused;

    public static void main(String[] args){
        System.out.println("Running...");
        printConstant(CONSTANT);
        new MyJavaProgram();
    }

    private static void printConstant(String constant) {
        System.out.println("Your constant is " + constant);
    }

    public MyJavaProgram(){
        init();
        String[] strings = new String[]{"string1", "string2"};
        methodWithParameter(strings);
        emptyMethod();
        int sum = add(10,20);
        System.out.println("10 + 20 = " + sum);
    }

    private void init(){
        System.out.println("Init called.");
        outerClass = new OuterClass();
        outerClass.sleep();
        methodNoParameter();
    }

    @Deprecated
    private void methodNoParameter(){
        System.out.println("methodNoParater called...");
    }

    /**
    *
    *This is a JavaDoc
    *
    *@param strings an array of strings
    */

    private void methodWithParameter(String[] strings){
        System.out.println("methodWithParameter called");
        System.out.println("strings[0] = " + strings[0]);
    }

    private void emptyMethod(){
    }

    private int add(int first, int second){
        int sum = Math.addExact(first, second);
        return sum;
    }

    private void unused(){
        System.out.println("This is unused and should never print.");
    }
}