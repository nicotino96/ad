import java.sql.*;

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
}
