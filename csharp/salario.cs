using System;

namespace salario
{
  class Media
  {
    static void Main(string[] args)
    {
      //declarando o tipo de variavel
      double Salario, INSS;


      Console.WriteLine("Digite o Salario Do Funcionario?");
      Salario = Double.Parse(Console.ReadLine());

      if(Salario <= 1000){
          INSS = Salario * 0.08;
          
          Console.WriteLine($"O valor a ser descontado do INSS = R$ {INSS:0.00}");
      }


      else {
          INSS = Salario * 0.10;

          Console.WriteLine($"O valor a ser descontado do INSS = R$ {INSS:0.00}");
      }



    }
  }
}
