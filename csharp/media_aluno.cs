using System;

namespace MyApplication
{
  class Media
  {
    static void Main(string[] args)
    {
      Console.WriteLine("Qual Nota do Primeiro Aluno?");
      //NOTA 1
      string nota1 = convert.ToInt32(Console.ReadLine());

      Console.WriteLine("Qual Nota do Segundo Aluno?");
      //NOTA 2
      string nota2 = convert.ToInt32(Console.ReadLine());

      int MEDIA = (nota1 + nota2) / 2;

      Console.WriteLine($"A MEDIA do aluno foi {MEDIA}");
      
    }
  }
}