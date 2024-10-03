import org.json.JSONObject;

public class Magic {
    private int powerAmount;
    private String ability;
    public Magic(int powerAmount, String ability){
        this.powerAmount=powerAmount;
        this.ability=ability;
    }
    public JSONObject toJSONObject() {
        JSONObject jsonResult = new JSONObject();
        jsonResult.put("powerAmount", this.powerAmount);
        jsonResult.put("ability", this.ability);
        return jsonResult;
    }
}
