import org.junit.BeforeClass;
import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import static org.junit.Assert.*;

public class T006USAMovies {
    private static List<String> expectedResult = new ArrayList<>();

    @BeforeClass
    public static void fetchCorrectResults() {
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            // Crear y ejecutar la consulta
            Statement statement = conn.createStatement();
            ResultSet result = statement.executeQuery("SELECT title, year, duration FROM TMovies WHERE countryIso3166 = 'US'");
            while(result.next()) {
                String firstColumnValue = result.getString(1);
                String secondColumValue = result.getString(2);
                String thirdColumnValue = result.getString(3);
                String conc = ",";
                String concatenated = firstColumnValue + conc + secondColumValue + conc + thirdColumnValue;
                expectedResult.add(concatenated);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void testResultsOk() {
        ArrayList<String> actualResult = null;
        try {
            Class cls = Class.forName("MoviesDataProvider");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("getResultsIssue6");
            actualResult = (ArrayList) method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals(expectedResult.size(), actualResult.size());
        for (int i = 0; i < expectedResult.size(); i++) {
            assertEquals(expectedResult.get(i), actualResult.get(i));
        }
    }
}

