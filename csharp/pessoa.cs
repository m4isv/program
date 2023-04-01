using System;

namespace app
{
	class Pessoa
	{
		static void Main()
		{
			Console.WriteLine("Digite Seu Nome");

			string nome = Console.ReadLine();

			if(nome == "Mailson"){
				Console.WriteLine($"Bem vindo de Volta {nome}");
			}

			else {
			Console.WriteLine($"Acesso Negado");
		   }
		}
	}
}