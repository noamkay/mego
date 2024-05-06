
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lesson1._2
{
    internal class Program
    {
        static void Main(string[] args)
        {

            int[] a = new int[] { 1, 2, 44, 2, 3, 47, 99, 66 };
            int max = a[0];
            for (int i = 1; i < a.Length; i++)
            {
                if (a[i] > max) ;
                max = a[i];
                Console.WriteLine(max);
            }
        }
    }
}
