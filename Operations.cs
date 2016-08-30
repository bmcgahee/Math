using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecordCalculation
{
    class Operations
    {
        public string add(int number, int randomNumber)
        {
            int firstNumber = number;
            int secondNumber = randomNumber;
            int result = firstNumber + secondNumber;
            string plusEquation = firstNumber + " + " + secondNumber + " = " + result;
            return plusEquation;
        }

        public string subtract(int number, int randomNumber)
        {
            int firstNumber = number;
            int secondNumber = randomNumber;
            int result = firstNumber - secondNumber;
            string minusEquation = firstNumber + " - " + secondNumber + " = " + result;
            return minusEquation;
        }
    }
}
