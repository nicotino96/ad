import org.json.JSONObject;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

public class Movie {
    private int id;
    private String title;
    private int year;
    private int duration;
    private String countryIso3166;
    private String genre;
    private String synopsis;
    private Connection connection;

    public Movie(int id, String title, int year, int duration, String countryIso3166, String genre, String synopsis) {
        this.id = id;
        this.title = title;
        this.year = year;
        this.duration = duration;
        this.countryIso3166 = countryIso3166;
        this.genre = genre;
        this.synopsis = synopsis;
    }
    public JSONObject toJSONObject() {
        JSONObject object = new JSONObject();
        object.put("id", this.id);
        object.put("title", this.title);
        object.put("year", this.year);
        object.put("duration",this.duration);
        object.put("countryIso3166",this.countryIso3166);
        object.put("genre",this.genre);
        object.put("synopsis",this.synopsis);

        return object;
    }



}
