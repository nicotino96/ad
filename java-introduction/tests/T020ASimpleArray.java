import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T020ASimpleArray {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testPrivateAttributeAndMethods() {
        try {
            Class cls = Class.forName("TravelStops");
            Field field = cls.getDeclaredField("stops");
            Object instance = cls.getDeclaredConstructor().newInstance();
            field.get(instance);
            fail("stops field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("TravelStops");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method printFirstStop = cls.getDeclaredMethod("printFirstStop");
            Method printSecondStop = cls.getDeclaredMethod("printSecondStop");
            Method printThirdStop = cls.getDeclaredMethod("printThirdStop");
            printSecondStop.invoke(instance);
            printThirdStop.invoke(instance);
            printFirstStop.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Frankfurt\r\nKuala Lumpur\r\nTokyo\r\n", outContent.toString());
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}
