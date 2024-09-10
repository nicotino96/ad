import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.*;
import java.lang.reflect.InvocationTargetException;

import static org.junit.Assert.*;

public class T026AccessAFile {
    private static final ByteArrayOutputStream outContent = new ByteArrayOutputStream(), errContent = new ByteArrayOutputStream();
    private static final PrintStream originalOut = System.out, originalErr = System.err;
        
    @BeforeClass
    public static void setUpStreams() {
        System.setOut(new PrintStream(outContent));
        System.setErr(new PrintStream(errContent));

        String file ="assets\\cinemaPrefs.txt";
        try {
            FileWriter fileWriter = new FileWriter(file);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            // Escribimos la primera línea
            bufferedWriter.write("username=John Doe");
            bufferedWriter.newLine();
            bufferedWriter.write("prefersDarkMode=true");
            bufferedWriter.newLine();
            bufferedWriter.flush();
            fileWriter.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void testHomeCinemaPreferencesConstructor() {
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor().newInstance();
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertTrue(outContent.toString().startsWith("username=John Doe\r\nprefersDarkMode=true\r\n"));
    }

    @AfterClass
    public static void restoreStreams() {
        System.setOut(originalOut);
        System.setErr(originalErr);
    }
}

