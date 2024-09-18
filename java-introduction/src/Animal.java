public class Animal {
    private String name;
    private String species;
    private int numberOfTeeth;

    public void setName(String name) {
        this.name = name;
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public void setNumberOfTeeth(int numberOfTeeth) {
        this.numberOfTeeth = numberOfTeeth;
    }

    public String getName() {
        return name;
    }

    public String getSpecies() {
        return species;
    }

    public int getNumberOfTeeth() {
        return numberOfTeeth;
    }

    public Animal(String name, String species, int numberOfTeeth) {
        this.name = name;
        this.species = species;
        this.numberOfTeeth = numberOfTeeth;
    }
}
