import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class MoviesDataProvider {

    // Método constructor
    public MoviesDataProvider() {
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Se ha establecido la conexión
            // ...
            System.out.println("The connection has been established successfully");
            conn.close(); // Cerramos la conexión
            System.out.println("Connection closed");
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
