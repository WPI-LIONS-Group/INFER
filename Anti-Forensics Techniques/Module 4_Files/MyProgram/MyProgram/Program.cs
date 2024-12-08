using System;

class MyCSProgram
{
    static void Main()
    {
        Console.WriteLine("Running...");
        string CONSTANT = "Constant String";
        printConstant(CONSTANT);
        init();
        string[] strings = { "string1", "string2" };
        methodWithParameter(strings);
        emptyMethod();
        int sum = add(10, 20);
        Console.WriteLine("10 + 20 = {0}", sum);
    }

    static void printConstant(string constant)
    {
        Console.WriteLine("Your constant is {0}", constant);
    }

    static void init()
    {
        Console.WriteLine("Init called.");
        OuterClass outerClass = new OuterClass();
        outerClass.Sleep();
        methodNoParameter();
    }

    static void methodNoParameter()
    {
        Console.WriteLine("methodNoParameter called...");
    }

    static void methodWithParameter(string[] strings)
    {
        Console.WriteLine("methodWithParameter called");
        Console.WriteLine("strings[0] = {0}", strings[0]);
    }

    static void emptyMethod()
    {
    }

    static int add(int first, int second)
    {
        int sum = first + second;
        return sum;
    }
}
