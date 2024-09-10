import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T016ReallyUsingAttributes {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testConstructorOutput() {
        int num = (int) Math.floor(Math.random()*100);
        String name = "Nombre" + num;
        try {
            Class cls = Class.forName("Person");
            Object instance = cls.getDeclaredConstructor(String.class).newInstance(name);
            Method getter = cls.getDeclaredMethod("getName");
            Method greeting = cls.getDeclaredMethod("greeting");
            String actualName = (String) getter.invoke(instance);
            String actualGreeting = (String) greeting.invoke(instance);
            assertEquals(name, actualName);
            assertEquals("Bienvenido/a, "+name, actualGreeting);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals(name + " acaba de ser instanciado\r\n", outContent.toString());
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}
