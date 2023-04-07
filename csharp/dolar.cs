using System;

namespace converso
{
  class Converso
  {
    static void Main(string[] args)
    {
      //declarando o tipo de variavel
      double REAL, DOLAR;

      Console.WriteLine("Quanto dinheiro voce tem na carteira?");
      REAL = float.Parse(Console.ReadLine());
      
      DOLAR = (REAL / 5.3); 
      string FORMAT = DOLAR.ToString("C2");

      Console.WriteLine($"Com {REAL} R$ voce pode Comprar {FORMAT} Dolar");
    }
  }
}
