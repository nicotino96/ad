import org.json.JSONObject;

public class GrossProfit {
    private int year;
    private long amount;
    private String currencyCode;

    public GrossProfit(int year, long amount, String currencyCode) {
        this.year = year;
        this.amount = amount;
        this.currencyCode = currencyCode;
    }
    public JSONObject toJSONObject() {
        JSONObject jsonResult = new JSONObject();
        jsonResult.put("year", this.year);
        jsonResult.put("amount", this.amount);
        jsonResult.put("currencyCodeIso4217", this.currencyCode);
        return jsonResult;
    }

}
