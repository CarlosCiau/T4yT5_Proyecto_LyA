package calculadora;
import java.util.Scanner; // Importacin de la clase Scanner.
 
public class TestCalculadora{
  public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double res = 0;
        String operacion;
        boolean comprobar = false;
 
        do{
            //Verificacin de los datos puestos por el usuario del nmero 1.
            /* Con matches, hay una condicin de que dgitos primero puede
            poner el usuario, en la condicional tenemos primero que solo se admite los caracteres '+' y '-', pero con la condici�n de que sea una sola vez o ninguna vez. Despu�s tenemos que se admiten cualquier n�mero del 0 al 9 y que se ponga o 0 veces o m�s veces, es decir, se pone algo o no se pone nada. Mas otra condici�n de que solo admite el car�cter '.' una o ninguna vez. Seguido del punto, si es que se coloca, se admite cualquier n�mero del 0 al 9 que sea una o m�s veces.*/
            String numero1;
            do {
                System.out.println("\n Por favor, dame el primer nmero de la operacin. ");
                numero1 = sc.nextLine();
            } while (!numero1.matches("[+-]?[\\d]*[.]?[\\d]+"));
            double nume1 = Double.parseDouble(numero1);
            double n1 = new Double(numero1);
            // Fin de la verificacin de los datos puestos por el usuario del nmero 1.
 
            do {
                System.out.println("\n Que operacin desea hacer? (Solo coloque un signo)");
                System.out.println("Teniendo en cuenta que: \n + = sumar \n - = restar \n"
                        + " x = multiplicar \n / = dividir \n * = elevar primer nmero al segundo numero."
                        + "\n % = residuo");
            operacion = sc.nextLine();
                if (operacion.equals("+") || operacion.equals("-") || operacion.equals("x") ||
                    operacion.equals("X") || operacion.equals("/") || operacion.equals("%") ||
                    operacion.equals("*")) {
                    comprobar = true;
                }else { comprobar = false; }
            } while (comprobar != true);
 
            // Verificacin de los datos puestos por el usuario del nmero 2.
            String numero2;
            do {
                System.out.println("\n Por favor, dame el segundo numero.");
                numero2 = sc.nextLine();
            } while (!numero2.matches("[+-]?[\\d]*[.]?[\\d]+"));
            double nume2 = Double.parseDouble(numero2);
            double n2 = new Double(numero2);
            // Fin de la verificacin de los datos puestos por el usuario del nmero 2.
 
            do{
                comprobar = true;
                switch(operacion){
                    case "+":
                        res = n1 + n2;
                        break;
                    case "-":
                        res = n1 - n2;
                        break;
                    case "x":
                    case "X":
                        res = n1 * n2;
                        break;
                    case "/":

                        while(n2 == 0){
                                 do {
                                    System.err.println(" En el denominador se encuentra \n"
                                            + "un cero, para evitar errores coloca otro numero.");
                                    numero2 = sc.nextLine();
                                }while (!numero2.matches("[+-]?[\\d]*[.]?[\\d]+"));
                                    nume2 = Double.parseDouble(numero2);
                                    n2 = new Double(numero2);
                        }
                        res = n1 / n2;
                        break;
                    case "*":
                        res = Math.pow(n1, n2);
                        break;
                    case "%":
                        while(n2 == 0){
                                 do {
                                    System.err.println(" En el denominador se encuentra \n"
                                            + "un cero, para evitar errores coloca otro numero.");
                                    numero2 = sc.nextLine();
                                }while (!numero2.matches("[+-]?[\\d]*[.]?[\\d]+"));
                                    nume2 = Double.parseDouble(numero2);
                                    n2 = new Double(numero2);
                        }
                        res = n1 % n2;
                        break;
                }
            }while(comprobar != true);
 
            System.out.println("(" + numero1 + ") " + operacion + " (" + numero2 + ")" + " = " + res);
            System.out.println("\n Desea hacer alguna otra operacion? \n");
            System.out.println(" [s/n]");
            do{
                comprobar = true;
                operacion = sc.nextLine();
 
                switch (operacion) {
                    case "s":
                    case "S":
                    case "n":
                    case "N":
                        break;
                    default:
                        System.err.println("\n Error, ponga un literal valido. \n");
                        comprobar = false;
                }
            }while(comprobar != true);
        }while(operacion.equals("s") || operacion.equals("S"));
  }
}