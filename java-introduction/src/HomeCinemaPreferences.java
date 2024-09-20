import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class HomeCinemaPreferences {
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public boolean isDarkModePreferred() {
        return darkModePreferred;
    }

    public void setDarkModePreferred(boolean darkModePreferred) {
        this.darkModePreferred = darkModePreferred;
    }

    private String username;
    private boolean darkModePreferred;

    public HomeCinemaPreferences() throws IOException {
        String file ="assets\\cinemaPrefs.txt";
        try {
            FileReader reader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(reader);
            String newLine = null;
            do {
                newLine = bufferedReader.readLine();
                System.out.println(newLine);
                parseLine(newLine);
            } while (newLine != null);
            reader.close();


        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
    private void parseLine(String line) {
        if (line == null) {
            return;
        }
        String[] separatedString = line.split("=");
        String firstHalf = separatedString[0];
        String secondHalf = separatedString[1];
        if (firstHalf.equals("username")) {
            this.username = secondHalf;
        }
        if (firstHalf.equals("prefersDarkMode")) {
            this.darkModePreferred=secondHalf.equals("true");
        }



    }

}
