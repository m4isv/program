using System;

namespace MENU
{
  class menu 
  {
    static void Main(string[] args)
    {
      Console.Clear();
     
      int MENU;
      Console.WriteLine("Escolha Uma Opçao\nOPÇAO 1\nOPÇAO 2\nOPÇAO 3\n");

      MENU = int.Parse(Console.ReadLine());

      //IF 
      switch(MENU){
        case 1:
            Console.WriteLine("OPÇAO 1 escolhida");
            break;

        case 2:
            Console.WriteLine("OPÇAO 2 escolhida");
            break;

        case 3:
            Console.WriteLine("OPÇAO 3 escolhida");
            break;

        default:
           Console.WriteLine("OPÇAO INVALIDA");
           break;
      }

    }
  }
}
