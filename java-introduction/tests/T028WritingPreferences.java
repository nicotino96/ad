import org.junit.Test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T028WritingPreferences {

    @Test
    public void testHomeCinemaPreferencesWriteToFile() {
        int num = (int) Math.floor(Math.random()*100);
        String randomName = "RandomName" + num;
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method usernameSetter = cls.getDeclaredMethod("setUsername", String.class);
            Method darkModeSetter = cls.getDeclaredMethod("setDarkModePreferred", boolean.class);
            Method saveToFile = cls.getDeclaredMethod("writeToFile");
            usernameSetter.invoke(instance, randomName);
            darkModeSetter.invoke(instance, false);
            saveToFile.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        String file ="assets\\cinemaPrefs.txt";
        try {
            FileReader fileReader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String firstLine = bufferedReader.readLine();
            String secondLine = bufferedReader.readLine();
            assertEquals(firstLine, "username=" + randomName);
            assertEquals(secondLine, "prefersDarkMode=false");
            fileReader.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
