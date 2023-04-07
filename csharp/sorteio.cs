using System;

namespace APP
{
    class Program
    {
      static void Main(string[] args)
      {
        Random sortear = new Random();
        int computador = sortear.Next(3);

        string[] itens = {"PEDRA", "PAPEL", "TESOURA"};
        Console.WriteLine($"o computador escolheu o: {itens[computador]}");


      }
  }
}
