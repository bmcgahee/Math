using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RecordCalculation
{
    class WriteFile
    {
        public void writeToFile(string filePath, string calculation)
        {
            
            if (!File.Exists(filePath))
            {
                File.CreateText(filePath);
                StreamWriter calcWriter = new StreamWriter(filePath);
                calcWriter.Write(calculation);
                calcWriter.Close();
            }
            else if (File.Exists(filePath))
            {
                StreamWriter calcWriter = new StreamWriter(filePath);
                calcWriter.Write(calculation);
                calcWriter.Close();
            }

        }
    }
}
