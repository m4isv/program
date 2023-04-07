using System;

namespace game
{
  class game 
  {
    static void Main(string[] args)
    {
      Console.Clear();

      Console.WriteLine("\nEscolha Uma Opçao\n\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n");
 

     Random sortear = new Random();
     int computador = sortear.Next(3);
     
     string[] itens = {"PEDRA", "PAPEL", "TESOURA"}; 
     
     Console.WriteLine("Qual sua Jogada?\n");
     int jogador = int.Parse(Console.ReadLine());
      Console.WriteLine("--------------------------------");
      Console.WriteLine($"o computador escolheu o: {itens[computador]}\n");
      Console.WriteLine($"o jogador escolheu o: {itens[jogador]}\n");
      Console.WriteLine("--------------------------------");

      if(computador == 0){
        //computador jogou PEDRA
          if(jogador == 0){
            Console.WriteLine("EMPATE");

          }

          else if(jogador == 1){
            Console.WriteLine("JOGADOR VENCE");

          }

          else if(jogador == 2){
            Console.WriteLine("COMPUTADOR VENCE");

          }

          else{
            Console.WriteLine("Jogada invalida");
          }


      }




      else if(computador == 1){
        //computador jogou PAPEL
          if(jogador == 0){
            Console.WriteLine("COMPUTADOR VENCE");

          }

          else if(jogador == 1){
            Console.WriteLine("EMPATE");

          }

          else if(jogador == 2){
            Console.WriteLine("JOGADOR VENCE");

          }

          else{
            Console.WriteLine("Jogada invalida");
          }

          

      }



      else if(computador == 2){
        //computador jogou TESOURA
          if(jogador == 0){
            Console.WriteLine("JOGADOR VENCE");

          }

          else if(jogador == 1){
            Console.WriteLine("COMPUTADOR VENCE");

          }

          else if(jogador == 2){
            Console.WriteLine("EMPATE");

          }

          else{
            Console.WriteLine("Jogada invalida");
          }

          

      }




    }
  }
}
