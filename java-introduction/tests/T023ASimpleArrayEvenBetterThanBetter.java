import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T023ASimpleArrayEvenBetterThanBetter {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testUpdateMethod() {
        int num = (int) Math.floor(Math.random()*100);
        String newStop1 = "NewStop1" + num;
        String newStop2 = "NewStop2" + num;
        String newStop3 = "NewStop3" + num;
        try {
            Class cls = Class.forName("TravelStops");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method printFirstStop = cls.getDeclaredMethod("printFirstStop");
            Method printSecondStop = cls.getDeclaredMethod("printSecondStop");
            Method printThirdStop = cls.getDeclaredMethod("printThirdStop");
            Method updateStop = cls.getDeclaredMethod("modifyStop", int.class, String.class);
            printSecondStop.invoke(instance);
            printFirstStop.invoke(instance);
            updateStop.invoke(instance, 0, newStop1);
            updateStop.invoke(instance, 1, newStop2);
            updateStop.invoke(instance, 2, newStop3);
            printThirdStop.invoke(instance);
            printSecondStop.invoke(instance);
            printFirstStop.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Frankfurt\r\nTokyo\r\n"+newStop3+"\r\n"+newStop2+"\r\n"+newStop1+"\r\n", outContent.toString());
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}

