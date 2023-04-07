using System;

namespace mes
{
  class Mes
  {
    static void Main(string[] args)
    {
      //declarando o tipo de variavel
      int mes;

      Console.WriteLine($"Digite o Numero do Mes");
      mes = int.Parse(Console.ReadLine());
      string mesSTR;

      switch(mes){
        case 1: mesSTR = "Janeiro";
                break;

        case 2: mesSTR = "Fevereiro";
                break;

        case 3: mesSTR = "Março";
                break;

        case 4: mesSTR = "Abril";
                break;

        case 5: mesSTR = "Maio";
                break;

        case 6: mesSTR = "Junho";
                break;

        case 7: mesSTR = "Julho";
                break;

        case 8: mesSTR = "Agosto";
                break;

        case 9: mesSTR = "Setembro";
                break;

        case 10: mesSTR = "Outubro";
                break;

        case 11: mesSTR = "Novembro";
                break;

        case 12: mesSTR = "Dezembro";
                break;

        default: mesSTR = "Mes invalido";
                break;
      }

      Console.WriteLine(mesSTR);

    }
  }
}
