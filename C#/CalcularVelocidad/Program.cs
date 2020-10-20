using System;

namespace CalcularVelocidad
{

    //PROGRAMA QUE CALCULA LA VELOCIDAD
    class Program
    {
        //METODO PRINCIPAL
        static void Main(string[] args)
        {
            Console.WriteLine("----------------------------------"); 
            Console.WriteLine("Programa que calcula la velocidad.");
            Console.WriteLine("----------------------------------");
            Console.WriteLine("Distancia = 310 \nTiempo = 2.8 \nVelocidad = ?"); 
            //VARIABLES
            int distancia = 310;
            double tiempo = 2.8;
            double velocidad;
            
            //CALCULAMOS LA VELOCIDAD
            velocidad = distancia/tiempo;
            
            //IMPRIMIMOS EL RESULTADO
            Console.WriteLine("Velocidad= "+velocidad);
            Console.WriteLine("Presiona c para salir"); 
            Console.ReadKey();

            
        }
    }
}
