using System;

namespace app
{
	class Pessoa
	{
		static void Main()
		{

      Random n1 = new Random();
      Random n2 = new Random();
      Random n3 = new Random();
      Random n4 = new Random();
      Random n5 = new Random();
      Random n6 = new Random();
      Random n7 = new Random();
      Random n8 = new Random();
      Random n9 = new Random();
      Random n10 = new Random();
      Random n11 = new Random();

      Console.WriteLine("\nGERANDO CPF:\n");

      Console.WriteLine($"{n1.Next(10)}{n2.Next(10)}{n3.Next(10)}.{n4.Next(10)}{n5.Next(10)}{n6.Next(10)}.{n7.Next(10)}{n8.Next(10)}{n9.Next(10)}-{n10.Next(10)}{n11.Next(10)}\n"); 

		}
	}
}
