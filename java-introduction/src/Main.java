public class Main {
    public static void main(String[] args) {
        Greeter greeter = new Greeter();
        greeter.sayHello();
        Cat cat = new Cat();
        cat.meow();
        String miString= greeter.byeWorld();
        System.out.println(miString);
    }
}

