public class SimpleMathDemo {
    private int firstNumber(){
        return 3172;
    }
    private int secondNumber(){
        return 1408;
    }
    private int thirdNumber(){
        return 4920;
    }
    public int calculateResult(){
        return firstNumber()+secondNumber()+thirdNumber();
    }
    public void printMultiplicationInfo() {
        System.out.println("Los múltiplos de 7 menores que 70 son:");
        for (int i = 0; i < 70; i+=7) {
            System.out.println(i);
        }
    }
    public void loop50Times() {
        for (int i = 0; i < 50; i++) {
            System.out.println("Imprimiendo... " + i);
            if (i == 38) {
                return; // Se puede hacer return si el método devuelve
                // void. Tiene el mismo efecto...
                // ¡Pero no devuelve nada!
            }
        }
    }
    public void printNumber(int nombreArbitrario) {
        System.out.println(nombreArbitrario);
    }
    public void printProduct(int n1, int n2){
        int result=n1*n2;
        System.out.println(result);
    }
    public void printProduct(String var, int num1, int num2) {
        System.out.println("Muy buenas," + " " + var);
        System.out.println("Este es el producto de tus dos valores:");
        System.out.println(num1 * num2);
    }
    public int randomNumberInRange(int start, int length){
        if(length<=0){
            return -1;
        }
        int random = (int) ((length * Math.random()) + start);
        return random;
    }
    public int randomNumberBetween(int min, int max){
        if(min>=max)
            return -1;
        int random = (int) (((max-min)*Math.random())+ min);
        return random;
    }
    public int getTheSmallerValue(int n1, int n2, int n3, int n4){
        if(n1>n2)
            n1=n2;
        if(n1>n3)
            n1=n3;
        if(n1>n4)
            return n4;
        else
            return n1;
    }




}
