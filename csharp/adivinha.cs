using System;

namespace APP
{
    class Program
    {
      static void Main(string[] args)
      {
       Random number = new Random();

       Console.WriteLine("Vou Pensar em um Numero de 0 a 10 tente adivinha");

       int user = int.Parse(Console.ReadLine());
       int comput = number.Next(10);
     
       if(user == comput){
            Console.WriteLine($"Eu Pensei no Numero {comput} vc escolheu {user} ACERTOU");

       }

       else {
        Console.WriteLine($"Errou eu pensei em {comput} e vc em {user}");
       }

      }
    }
}
