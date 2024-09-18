public class Person {
    private String name;
    public String getName() {
        return this.name;
    }

    public Person(String name) {
        this.name=name;
        System.out.println(name+" acaba de ser instanciado");

    }
    public String greeting() {
        return "Bienvenido/a, " + this.name;
    }
}

