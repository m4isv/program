using System;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      Console.WriteLine("NUMERO 1:");
      int N1 = Convert.ToInt32(Console.ReadLine());


      Console.WriteLine("NUMERO 2: ");
      int N2 = Convert.ToInt32(Console.ReadLine());

      int SOMA = (N1 + N2);

      Console.WriteLine($"A Soma Entre {N1} e {N2} e Ingual a {SOMA}");
    }
  }
}

