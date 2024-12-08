using System;

class OuterClass
{
    public void Sleep()
    {
        Console.WriteLine("Sleeping...");
        System.Threading.Thread.Sleep(5000);
    }
}
