using System;

namespace APP
{
    class Program
    {
      static void Main(string[] args)
      {
        string[] cars = {"Fusca", "Ford", "bmw", "Jipe"};

        for(int number = 0; number < cars.Length; number++){
          Console.WriteLine(cars[number]);
        } 

      }
    }
}
