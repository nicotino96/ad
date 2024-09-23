import org.json.JSONObject;
import org.json.JSONTokener;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Text;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.*;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.*;

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
    @Deprecated
    public HomeCinemaPreferences() {
        initializeFromTXT();
    }
    public HomeCinemaPreferences(boolean readJSON) {
        if (readJSON) {
            initializeFromJSON();
        } else {
            initializeFromTXT();
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
    public void writeToFile() {
        String file ="assets\\cinemaPrefs.txt";
        try {
            FileWriter fileWriter = new FileWriter(file);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            // Escribimos la primera línea
            bufferedWriter.write("username=");
            bufferedWriter.write(this.username);
            bufferedWriter.newLine();
            // Escribimos la segunda línea
            if (this.darkModePreferred) {
                bufferedWriter.write("prefersDarkMode=true");
            } else {
                bufferedWriter.write("prefersDarkMode=false");
            }
            bufferedWriter.newLine();
            bufferedWriter.flush(); // Guardamos el fichero a disco
            fileWriter.close(); // Y lo cerramos
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    public void saveExampleJSON() throws IOException {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("name", "Pepe Depura");
        jsonObject.put("isLearning", true);

        FileWriter writer = new FileWriter("assets\\example.json");
        jsonObject.write(writer, 2, 0); // Estos números indican la identación del resultado,
        // espacios en blanco que mejoran la legibilidad
        writer.flush();
        writer.close();

    }
    public void writeJSON() throws IOException {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("username", this.username);
        jsonObject.put("prefersDarkMode", this.darkModePreferred);
        FileWriter writer = new FileWriter("assets\\cinemaPrefs.json");
        jsonObject.write(writer, 2, 0); // Estos números indican la identación del resultado,
        // espacios en blanco que mejoran la legibilidad
        writer.flush();
        writer.close();

    }
    private void initializeFromJSON() {
        try {
            JSONTokener tokener = new JSONTokener(new FileReader("assets\\cinemaPrefs.json"));
            JSONObject jsonObject = new JSONObject(tokener);
            String fileUsername = jsonObject.getString("username");
            boolean fileDarkMode = jsonObject.getBoolean("prefersDarkMode");
            this.username = fileUsername;
            this.darkModePreferred = fileDarkMode;

        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
    private void initializeFromTXT() {
        String file = "assets\\cinemaPrefs.txt";
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


        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
    public void saveExampleXML() throws ParserConfigurationException, TransformerException {
        DocumentBuilderFactory factory1 = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory1.newDocumentBuilder();
        Document xmlDocument = builder.newDocument();
        Element rootNode = xmlDocument.createElement("Student");
        xmlDocument.appendChild(rootNode);
        Element node1 = xmlDocument.createElement("Name");
        Text node1Content = xmlDocument.createTextNode("Pepe Depura");
        node1.appendChild(node1Content);
        rootNode.appendChild(node1);
        Element node2 = xmlDocument.createElement("IsLearning");
        Text node2Content = xmlDocument.createTextNode("true");
        node2.appendChild(node2Content);
        rootNode.appendChild(node2);
        TransformerFactory factory2 = TransformerFactory.newInstance();
        Transformer transformer = factory2.newTransformer();
        transformer.setOutputProperty(OutputKeys.INDENT, "yes");
        DOMSource dom = new DOMSource(xmlDocument);
        StreamResult outputStream = new StreamResult(new File("assets\\example.xml"));

        transformer.transform(dom, outputStream);


    }

}
