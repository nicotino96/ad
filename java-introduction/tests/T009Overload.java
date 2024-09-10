import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import static org.junit.Assert.*;

public class T009Overload {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testPrint() {
        int num1 = (int) Math.floor(Math.random()*1000);
        int num2 = (int) Math.floor(Math.random()*1000);
        try {
            Class cls = Class.forName("SimpleMathDemo");
            Method method = cls.getDeclaredMethod("printProduct", String.class, int.class, int.class);
            Object instance = cls.getDeclaredConstructor().newInstance();
            method.invoke(instance, "Pepe", num1, num2);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Muy buenas," + " " + "Pepe\r\nEste es el producto de tus dos valores:\r\n"  + num1 * num2 +"\r\n", outContent.toString());
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}

