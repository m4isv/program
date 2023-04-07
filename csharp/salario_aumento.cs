using System;

namespace salario
{
  class Salario
  {
    static void Main(string[] args)
    {
      //declarando o tipo de variavel
      double Salario, novo;


      Console.WriteLine("Digite o Salario Do Funcionario?");
      Salario = Double.Parse(Console.ReadLine());

      novo = Salario + (Salario * 15 / 100);

      Console.WriteLine($"Um Funcionario que Ganhava {Salario} Com Aumento de 15% Passa A Ganha {novo:0.00}R$");

    }
  }
}
