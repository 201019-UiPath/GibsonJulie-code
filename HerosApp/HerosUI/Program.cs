using System;
using HerosLib;

namespace HerosUI
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            Hero obj = new Hero();
            Console.WriteLine($"{obj.id}, {obj.name}");
        }
    }
}
