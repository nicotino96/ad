import org.junit.BeforeClass;
import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.sql.*;
import static org.junit.Assert.*;

public class T007GetTitleByID {
    private static String expectedResult = "";

    @BeforeClass
    public static void fetchCorrectResults() {
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT title FROM TMovies WHERE id = 5");
            while(result.next()) {
                expectedResult = result.getString(1);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void testResultsOk() {
        String actualResult = null;
        try {
            Class cls = Class.forName("MoviesDataProvider");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("getResultIssue7");
            actualResult = (String) method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals(expectedResult, actualResult);
    }
}


