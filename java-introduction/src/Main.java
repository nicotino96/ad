public class Main {
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.sayHello();
        Cat cat = new Cat();
        cat.meow();
        String miString= greeter.byeWorld();
        System.out.println(miString);
        System.out.println(greeter.sumTwoNumbers());
        SimpleMathDemo simpleMathDemo = new SimpleMathDemo();
        System.out.println(simpleMathDemo.calculateResult());
        simpleMathDemo.printMultiplicationInfo();
        simpleMathDemo.loop50Times();
        simpleMathDemo.printNumber(5895);
        simpleMathDemo.printProduct(3,9);
    }
}

