using System;

namespace salario
{
  class Desconto
  {
    static void Main(string[] args)
    {
      //declarando o tipo de variavel
      double preco, novo;

      Console.WriteLine("Qual Preço do produto?");
      preco = Double.Parse(Console.ReadLine());


      novo = preco - (preco * 5 / 100);

      Console.WriteLine($"Um Produto que Custava {preco} R$ Na Promoçao de 5% de desconto vai custa {novo:0.00}R$");

    }
  }
}
