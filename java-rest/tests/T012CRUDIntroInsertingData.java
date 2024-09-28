import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.sql.*;

import static org.junit.Assert.*;

public class T012CRUDIntroInsertingData {
    private int previousNumberOfInsideOutTitles;
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void backupDBAndSetStreams() throws IOException {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
        backupDatabase();
    }

    @Test
    public void testPrintOutput() {
        try {
            Class cls = Class.forName("MoviesConnector");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("insertExampleFilm");
            method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertTrue(outContent.toString().contains("Se ha insertado satisfactoriamente"));
    }

    @Before
    public void checkNumberOfTitles() {
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE title = 'Inside Out' AND synopsis = 'Riley es una chica que disfruta o padece toda clase de sentimientos. Aunque su vida ha estado marcada por la Alegría, también se ve afectada por otro tipo de emociones. Lo que Riley no entiende muy bien es por qué motivo tiene que existir la Tristeza en su vida. Una serie de acontecimientos hacen que Alegría y Tristeza se mezclen en un peligroso viaje que dará un vuelco al mundo de Riley.'");
            while(result.next()) {
                previousNumberOfInsideOutTitles = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
    
    @Test
    public void testRowWasInserted() {
        try {
            Class cls = Class.forName("MoviesConnector");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("insertExampleFilm");
            method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        int newNumberOfTitles = -1;
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT COUNT(*) FROM TMovies WHERE title = 'Inside Out' AND synopsis = 'Riley es una chica que disfruta o padece toda clase de sentimientos. Aunque su vida ha estado marcada por la Alegría, también se ve afectada por otro tipo de emociones. Lo que Riley no entiende muy bien es por qué motivo tiene que existir la Tristeza en su vida. Una serie de acontecimientos hacen que Alegría y Tristeza se mezclen en un peligroso viaje que dará un vuelco al mundo de Riley.'");
            while(result.next()) {
                newNumberOfTitles = result.getInt(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        assertEquals(previousNumberOfInsideOutTitles + 1, newNumberOfTitles);
    }

    @AfterClass
    public static void restore() throws IOException {
        System.setOut(originalOut);
        System.setErr(originalErr);
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
