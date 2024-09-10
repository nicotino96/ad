import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T024NewTravelStops {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testPrintMethodAndContents() {
        try {
            Class cls = Class.forName("NewTravelStops");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method printStop = cls.getDeclaredMethod("printStop", int.class);
            printStop.invoke(instance, 2);
            printStop.invoke(instance, 0);
            printStop.invoke(instance, 1);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Hanoi\r\nKyoto\r\nSingapur\r\n", outContent.toString());
    }

    @Test
    public void testSetMethod() {
        outContent.reset();
        int num = (int) Math.floor(Math.random()*100);
        String newStop1 = "NewStop1" + num;
        String newStop2 = "NewStop2" + num;
        String newStop3 = "NewStop3" + num;
        try {
            Class cls = Class.forName("NewTravelStops");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method printStop = cls.getDeclaredMethod("printStop", int.class);
            Method setStop = cls.getDeclaredMethod("modifyStop", int.class, String.class);
            printStop.invoke(instance, 2);
            printStop.invoke(instance, 0);
            printStop.invoke(instance, 1);
            setStop.invoke(instance, 0, newStop1);
            setStop.invoke(instance, 1, newStop2);
            setStop.invoke(instance, 2, newStop3);
            printStop.invoke(instance, 0);
            printStop.invoke(instance, 1);
            printStop.invoke(instance, 2);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Hanoi\r\nKyoto\r\nSingapur\r\n"+newStop1+"\r\n"+newStop2+"\r\n"+newStop3+"\r\n", outContent.toString());
    }

    @Test
    public void testAddMethod() {
        outContent.reset();
        int num = (int) Math.floor(Math.random()*100);
        String newStop = "NewStop" + num;
        try {
            Class cls = Class.forName("NewTravelStops");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method printStop = cls.getDeclaredMethod("printStop", int.class);
            Method addStop = cls.getDeclaredMethod("addStop", String.class);
            printStop.invoke(instance, 2);
            printStop.invoke(instance, 0);
            printStop.invoke(instance, 1);
            addStop.invoke(instance,newStop);
            printStop.invoke(instance, 3);
            addStop.invoke(instance,newStop);
            printStop.invoke(instance, 4);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Hanoi\r\nKyoto\r\nSingapur\r\n"+newStop+"\r\n"+newStop+"\r\n", outContent.toString());
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}

