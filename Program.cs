using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecordCalculation
{
    class Program
    {
        public static void Main(string[] args)
        {
            string path = "calc.txt";

            WriteFile wfAdd = new WriteFile();
            WriteFile wfSubtract = new WriteFile();
            Operations op = new Operations();

            string sumEquation;
            string differenceEquation;

            Console.WriteLine("Select Addition or Subtraction: ");
            string selection = Console.ReadLine();

            if (selection == "Addition")
            {
                Console.WriteLine("Enter a number: ");
                int number = int.Parse(Console.ReadLine());
                Console.WriteLine("Random number to add is generated...");
                Random randNumOne = new Random();
                int randomNumberOne = randNumOne.Next(1000, 9999);
                sumEquation = op.add(number, randomNumberOne);
                wfAdd.writeToFile(path, sumEquation);
                Console.WriteLine("Addition has been completed.");
                Console.WriteLine("Check the file to see the result.");
            }
            else if (selection == "Subtraction")
            {
                Console.WriteLine("Enter a number: ");
                int number = int.Parse(Console.ReadLine());
                Console.WriteLine("Random number to subtract is generated...");
                Random randNumTwo = new Random();
                int randomNumberTwo = randNumTwo.Next(1000, 9999);
                differenceEquation = op.subtract(number, randomNumberTwo);
                wfSubtract.writeToFile(path, differenceEquation);
                Console.WriteLine("Subtraction has been completed.");
                Console.WriteLine("Check the file to see the result.");
            }
        }
               
    }
}
