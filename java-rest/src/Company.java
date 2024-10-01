import org.json.JSONObject;

public class Company {
    private String name;
    private String owner;
    private GrossProfit grossProfit;

    public Company(String name, String owner, GrossProfit grossProfit) {
        this.name = name;
        this.owner = owner;
        this.grossProfit = grossProfit;
    }
    public JSONObject toJSONObject() {
        JSONObject jsonResult = new JSONObject();
        jsonResult.put("name", this.name);
        jsonResult.put("owner", this.owner);
        jsonResult.put("grossProfit", this.grossProfit.toJSONObject()); // Observa cómo invocamos toJSONObject del atributo tipo GrossProfit
        return jsonResult;
    }


}
