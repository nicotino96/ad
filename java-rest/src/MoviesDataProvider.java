import java.sql.*;
import java.util.ArrayList;

public class MoviesDataProvider {

    // Método constructor
    public MoviesDataProvider() {
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Se ha establecido la conexión
            // ...
            System.out.println("The connection has been established successfully");
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT title FROM TMovies");
            while (result.next()) {
                // Para cada fila, imprimimos la primera (y única) columna tipo VARCHAR que hay
                System.out.println(result.getString(1));
            }

            conn.close(); // Cerramos la conexión
            System.out.println("Connection closed");
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    public ArrayList<String> getTwoColumns() {
        ArrayList<String> finalResult = new ArrayList<>();
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT title, countryIso3166 FROM TMovies");
            while(result.next()) {
                String firstColumnValue = result.getString(1);
                String secondColumValue = result.getString(2);
                String concatenated = firstColumnValue + ", " + secondColumValue;
                finalResult.add(concatenated);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return finalResult;
    }
    public ArrayList<String> getColumnUsingWhere(){
        ArrayList<String> finalResult = new ArrayList<>();
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT title FROM TMovies WHERE year>2001");
            while(result.next()) {
                String firstColumnValue = result.getString(1);
                String concatenated = firstColumnValue;
                finalResult.add(concatenated);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return finalResult;
    }
    public ArrayList<String> getResultsIssue6(){
        ArrayList<String> finalResult = new ArrayList<>();
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT title, year, duration FROM TMovies WHERE countryIso3166=\"US\"");
            while(result.next()) {
                String firstColumnValue = result.getString(1);
                String secondColumValue = result.getString(2);
                String thirdColumValue = result.getString(3);
                String concatenated = firstColumnValue + "," + secondColumValue+","+thirdColumValue;
                finalResult.add(concatenated);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return finalResult;
    }
    public String getResultIssue7 (){
        String firstColumnValue = "";
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT title FROM TMovies WHERE id=5");
            while(result.next()) {
                firstColumnValue = result.getString(1);

            }
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return firstColumnValue;
    }




}
