import org.json.JSONArray;
import org.json.JSONObject;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class TimeRegister {
    List<short[]> registers = new ArrayList<>();

    public void registerTime (short entranceHour, short exitHour) {
        if (entranceHour < 0 || entranceHour > exitHour || exitHour >= 24) {
            throw new RuntimeException();
        }
        short[] horas = {entranceHour, exitHour};
        registers.add(horas);
    }

    public void storeJSON() throws IOException {
        JSONObject jsonObject = new JSONObject();
        JSONArray jsonArray = new JSONArray();
        short totalTime = 0;
        for (short[] registro : registers) {
            JSONObject jsonObject1 = new JSONObject();
            jsonObject1.put("entranceHour", registro[0]);
            jsonObject1.put("exitHour", registro[1]);
            jsonArray.put(jsonObject1);
            totalTime += (short) (registro[1] - registro[0]);
        }
        jsonObject.put("totalTime", totalTime);
        jsonObject.put("registers", jsonArray);
        FileWriter writer = new FileWriter("assets\\hours.json");
        jsonObject.write(writer, 2, 0); // Estos números indican la identación del resultado,
        // espacios en blanco que mejoran la legibilidad
        writer.flush();
        writer.close();
    }


}