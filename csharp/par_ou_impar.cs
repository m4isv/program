using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
    	Console.WriteLine("Numero 1: ");
    	int numero1 = Convert.ToInt32(Console.ReadLine());

    	Console.WriteLine("Numero 2: ");
    	int numero2 = Convert.ToInt32(Console.ReadLine());

        string result_n1 = (numero1 %2==0) ? "numero 1 e par" : "numero 1 e impar";
        string result_n2 = (numero2 %2==0) ? "numero 2 e par" : "numero 2 e impar";

        Console.WriteLine(result_n1);
        Console.WriteLine(result_n2);
     
    }
  }
}