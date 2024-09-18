import java.util.ArrayList;
import java.util.List;

public class NewTravelStops {
    private ArrayList<String> stops;
    public NewTravelStops(){
        stops = new ArrayList<>(List.of("Kyoto","Singapur","Hanoi"));
    }
    public void printStop(int index){
        System.out.println(stops.get(index));
    }
    public void modifyStop(int index, String newValue){
        stops.set(index, newValue);
    }
    public void addStop(String newValue){
        stops.add(newValue);
    }
    public void showAllStops(){
        for(String a : stops){
            System.out.println(a);
        }
    }
}
