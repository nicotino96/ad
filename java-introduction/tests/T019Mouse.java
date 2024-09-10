import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T019Mouse {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testLeftHandedOutputs() {
        try {
            Class cls = Class.forName("Mouse");
            Object instance = cls.getDeclaredConstructor(boolean.class).newInstance(true);
            Method methodLeft = cls.getDeclaredMethod("clickLeft");
            Method methodRight = cls.getDeclaredMethod("rightButton");
            methodLeft.invoke(instance);
            assertEquals("Has hecho click secundario\r\n", outContent.toString());
            methodRight.invoke(instance);
            assertEquals("Has hecho click secundario\r\nHas hecho click principal\r\n", outContent.toString());
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
    }

    @Test
    public void testRightHandedOutputs() {
        outContent.reset();
        try {
            Class cls = Class.forName("Mouse");
            Object instance = cls.getDeclaredConstructor(boolean.class).newInstance(false);
            Method methodLeft = cls.getDeclaredMethod("clickLeft");
            Method methodRight = cls.getDeclaredMethod("rightButton");
            methodLeft.invoke(instance);
            assertEquals("Has hecho click principal\r\n", outContent.toString());
            methodRight.invoke(instance);
            assertEquals("Has hecho click principal\r\nHas hecho click secundario\r\n", outContent.toString());
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}
