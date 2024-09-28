import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.sql.*;
import static org.junit.Assert.*;

public class T013GenericComedyInsertion {
    private String test3Title = "A", test3CountryCode = "us", test3Synopsis = "B";
    private int test3Year = 2000, test3Duration = 101;
    private static String randomName = "N" + Math.floor((Math.random() * 100));

    @BeforeClass
    public static void backupDBAndSetStreams() throws IOException {
        backupDatabase();
    }

    @Test
    public void testCorrectInsert() {
        // Check number of titles previous to the method execution
        int previousNumberOfTitlesNormalInsert = -99;
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE genre = 'comedy'");
            while(result.next()) {
                previousNumberOfTitlesNormalInsert = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        // Execute to-be tested method
        try {
            Class cls = Class.forName("MoviesConnector");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("insertComedy", String.class, int.class, int.class, String.class, String.class);
            boolean result = (boolean) method.invoke(instance, "Funny Alien", 0, 0, "Test", "Test");
            assertTrue(result);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        // Query new amount of results, in order to assert
        int newNumberOfTitles = -1;
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE genre = 'comedy'");
            while(result.next()) {
                newNumberOfTitles = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        assertEquals(previousNumberOfTitlesNormalInsert + 1, newNumberOfTitles);
    }

    @Test
    public void testCorrectInsertMultipleRandom() {
        // Check number of titles previous to the method execution
        int previousNumberOfTitlesRandomInsert = -99;
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE title = '"+ randomName+"' AND genre = 'comedy'");
            while(result.next()) {
                previousNumberOfTitlesRandomInsert = result.getInt(1);
           }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        // Execute to-be tested method
        try {
            Class cls = Class.forName("MoviesConnector");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("insertComedy", String.class, int.class, int.class, String.class, String.class);
            boolean result1 = (boolean) method.invoke(instance, randomName, 0, 0, "Test", "Test");
            assertTrue(result1);
            boolean result2 = (boolean) method.invoke(instance, randomName, 0, 0, "Test", "Test");
            assertTrue(result2);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }

        // Query new amount of results, in order to assert
        int newNumberOfTitles = -1;
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE title = '"+randomName+"' AND genre = 'comedy'");
            while(result.next()) {
                newNumberOfTitles = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        assertEquals(previousNumberOfTitlesRandomInsert + 2, newNumberOfTitles);
    }

    @Test
    public void testAllCorrectValuesInserted() {
        // Check number of titles previous to the method execution
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        int previousNumberOfTitlesRandomInsert = -99;
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE title = '"+ test3Title+"' AND genre = 'comedy' AND year = "+test3Year+" AND duration = "+test3Duration+" AND synopsis = '"+test3Synopsis+"' AND countryIso3166='"+test3CountryCode+"'");
            while(result.next()) {
                previousNumberOfTitlesRandomInsert = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        // Execute to-be tested method
        try {
            Class cls = Class.forName("MoviesConnector");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("insertComedy", String.class, int.class, int.class, String.class, String.class);
            boolean result1 = (boolean) method.invoke(instance, test3Title, test3Year, test3Duration, test3CountryCode, test3Synopsis);
            assertTrue(result1);
         } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        int newNumberOfTitles = -1;
        // Query new results in order to assert
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE title = '"+ test3Title+"' AND genre = 'comedy' AND year = "+test3Year+" AND duration = "+test3Duration+" AND synopsis = '"+test3Synopsis+"' AND countryIso3166='"+test3CountryCode+"'");
            while(result.next()) {
                newNumberOfTitles = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        assertEquals(previousNumberOfTitlesRandomInsert + 1, newNumberOfTitles);
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

