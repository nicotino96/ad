import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import static org.junit.Assert.*;

public class T003InBetweenLetsRetrieveData {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testQueryOutputOk() {
        try {
            Class cls = Class.forName("MoviesDataProvider");
            Object instance = cls.getDeclaredConstructor().newInstance();
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertTrue(outContent.toString().contains("The Shawshank Redemption\r\nSecondhand Lions\r\nApocalypto\r\nBedazzled\r\nAvatar\r\nAlien\r\nUn monstruo viene a verme\r\nComme un chef\r\n"));
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}

