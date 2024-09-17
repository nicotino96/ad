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



}
