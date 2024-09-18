import java.sql.SQLOutput;

public class Coin {
    private int recompensa;

    public Coin(int recompensa) {
        if(recompensa<=0) throw new RuntimeException("Recompensa no válida");
        this.recompensa = recompensa;
    }
    public String flip(){
        double numeroAleatorio = Math.random();
        if(numeroAleatorio<=0.5)
            return "Has tirado al aire la moneda y ha salido cruz. Perdiste";
        else
            return "Has tirado al aire la moneda y ha salido cara. Has ganado " + recompensa + " euros";
    }
}
