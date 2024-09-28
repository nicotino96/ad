import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.sql.*;
import static org.junit.Assert.*;

public class T014UpdateDuration {
    private int invalidRandomId = (int) Math.floor((Math.random() * 100) + 1000);
    private int randomDuration = (int) Math.floor((Math.random() * 100));
    private String randomName = "NaN" + Math.floor((Math.random() * 100));

    @BeforeClass
    public static void backupDBAndSetStreams() throws IOException {
        backupDatabase();
    }

    @Test
    public void testCorrectUpdate() {
        // Insert a random film
        int newMovieId = -1;
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement1 = conn.createStatement();
            statement1.executeUpdate("INSERT INTO TMovies(title, year, duration, countryIso3166, genre, synopsis) VALUES ('"+randomName+"', 0, 0, 'es', 'nb', 'A')");
            Statement statement2 = conn.createStatement();
            ResultSet result = statement2.executeQuery("SELECT id FROM TMovies WHERE title = '"+randomName+"'");
            while(result.next()) {
                newMovieId = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        // Execute to-be tested method
        try {
            Class cls = Class.forName("MoviesConnector");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("changeDurationByFilmId", int.class, int.class);
            boolean result = (boolean) method.invoke(instance, randomDuration, newMovieId);
            assertTrue(result);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        // Query film duration, in order to assert
        int newDuration = -1;
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT duration FROM TMovies WHERE id = " + newMovieId);
            while(result.next()) {
                newDuration = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        assertEquals(randomDuration, newDuration);
    }

    @Test
    public void testReturnsFalse() {
        // Execute to-be tested method
        try {
            Class cls = Class.forName("MoviesConnector");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("changeDurationByFilmId", int.class, int.class);
            boolean result = (boolean) method.invoke(instance, randomDuration, invalidRandomId);
            assertFalse(result);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
    }

    @AfterClass
    public static void restore() throws IOException {
        restoreDatabase();
    }

    private static void backupDatabase() throws IOException {
        copyFile("db/sqlite3/movies.db", "db/sqlite3/movies_test_backup.db");
    }

    private static void restoreDatabase() throws IOException {
        copyFile("db/sqlite3/movies_test_backup.db", "db/sqlite3/movies.db");
        File backup = new File("db/sqlite3/movies_test_backup.db");
        backup.delete();
    }

    private static void copyFile(String source, String target) throws IOException {
        InputStream is = null;
        OutputStream os = null;
        try {
            is = new FileInputStream(source);
            os = new FileOutputStream(target);
            byte [] buffer = new byte[1024];
            int length;
            while ((length = is.read(buffer)) > 0) {
                os.write(buffer, 0, length);
            }
        } finally {
            is.close();
            os.close();
        }
    }
}


