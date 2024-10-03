import org.json.JSONObject;

public class AnimalFantastico {
    private String nombre;
    private int lifespanYears;
    private boolean isDangerous;
    private Magic magic;

    public AnimalFantastico(String nombre, int lifespanYears, boolean isDangerous, Magic magic){
        this.nombre=nombre;
        this.lifespanYears=lifespanYears;
        this.isDangerous=isDangerous;
        this.magic = magic;

    }
    public JSONObject toJSONObject(){
        JSONObject jsonResult = new JSONObject();
        jsonResult.put("name",this.nombre);
        jsonResult.put("lifespanYears",this.lifespanYears);
        jsonResult.put("isDangerous",this.isDangerous);
        jsonResult.put("magic",this.magic.toJSONObject());
        return jsonResult;
    }
}
