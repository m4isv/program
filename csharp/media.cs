using System;

namespace media
{
  class Media
  {
    static void Main(string[] args)
    {
      //declarando o tipo de variavel
      int nota1, nota2, nota3, nota4, nota5, SOMA;
      double MEDIA;


      Console.WriteLine("Primeira nota?");
      nota1 = Convert.ToInt32(Console.ReadLine());

      Console.WriteLine("Segunda nota?");
      nota2 = Convert.ToInt32(Console.ReadLine());
     
      Console.WriteLine("Terceira nota?");
      nota3 = Convert.ToInt32(Console.ReadLine());
      
      Console.WriteLine("Quarta nota?");
      nota4 = Convert.ToInt32(Console.ReadLine());

      Console.WriteLine("Quinta nota?");
      nota5 = Convert.ToInt32(Console.ReadLine());

      SOMA = (nota1 + nota2 + nota3 + nota4 + nota5);
      MEDIA = SOMA / 5.0;

      Console.WriteLine($"A MEDIA do aluno foi {MEDIA}");
      
    }
  }
}
