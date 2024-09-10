import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import static org.junit.Assert.*;

public class T006WhatHappenedInsideTheLoop {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;

    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));
    }

    @Test
    public void testMultiplicationTablePrint() {
        try {
            Class cls = Class.forName("SimpleMathDemo");
            Method method = cls.getDeclaredMethod("printMultiplicationInfo");
            Object instance = cls.getDeclaredConstructor().newInstance();
            method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Los múltiplos de 7 menores que 70 son:\r\n0\r\n7\r\n14\r\n21\r\n28\r\n35\r\n42\r\n49\r\n56\r\n63\r\n", outContent.toString());
    }

    @Test
    public void testLoop50TimesPrint() {
        outContent.reset();
        StringBuilder expected = new StringBuilder();
        for (int i = 0; i <= 38; i++) {
            expected.append("Imprimiendo... ").append(i).append("\r\n");
        }
        try {
            Class cls = Class.forName("SimpleMathDemo");
            Method method = cls.getDeclaredMethod("loop50Times");
            Object instance = cls.getDeclaredConstructor().newInstance();
            method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals(expected.toString(), outContent.toString());
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}

