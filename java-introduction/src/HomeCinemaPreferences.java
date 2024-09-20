import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class HomeCinemaPreferences {
    public HomeCinemaPreferences() throws IOException {
        String file ="assets\\cinemaPrefs.txt";
        try {
            FileReader reader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(reader);
            String newLine = null;
            do {
                newLine = bufferedReader.readLine();
                System.out.println(newLine);
            } while (newLine != null);
            reader.close();


        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}
