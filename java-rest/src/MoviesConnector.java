import java.sql.*;

public class MoviesConnector {
    private Connection connection;

    public MoviesConnector() {
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            this.connection = DriverManager.getConnection(connectionStr);
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }


    }
    public void closeConnection() {
        try {
            this.connection.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
