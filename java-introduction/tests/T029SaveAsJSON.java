import org.json.JSONObject;
import org.json.JSONTokener;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Random;

import static org.junit.Assert.*;

public class T029SaveAsJSON {

    @BeforeClass
    public static void clearJSONs() {
        String file1 = "assets\\example.json";
        String file2 = "assets\\cinemaPrefs.json";
        try {
            FileWriter fileWriter1 = new FileWriter(file1);
            BufferedWriter bufferedWriter1 = new BufferedWriter(fileWriter1);
            bufferedWriter1.write("");
            bufferedWriter1.flush();
            fileWriter1.close();
            FileWriter fileWriter2 = new FileWriter(file2);
            BufferedWriter bufferedWriter2 = new BufferedWriter(fileWriter2);
            bufferedWriter2.write("");
            bufferedWriter2.flush();
            fileWriter2.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    @Test
    public void testHomeCinemaPreferencesWriteExample() throws FileNotFoundException {
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method saveToFile = cls.getDeclaredMethod("saveExampleJSON");
            saveToFile.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        JSONTokener tokener = new JSONTokener(new FileReader("assets\\example.json"));
        JSONObject object = new JSONObject(tokener);
        String studentName = object.getString("name");
        boolean isLearning = object.getBoolean("isLearning");
        assertEquals("Pepe Depura", studentName);
        assertEquals(true, isLearning);
    }

    @Test
    public void testHomeCinemaPreferencesStoresUsername() throws FileNotFoundException {
        int num = (int) Math.floor(Math.random()*100);
        String randomName = "RandomName" + num;
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method usernameSetter = cls.getDeclaredMethod("setUsername", String.class);
            Method saveToFile = cls.getDeclaredMethod("writeJSON");
            usernameSetter.invoke(instance, randomName);
            saveToFile.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        JSONTokener tokener = new JSONTokener(new FileReader("assets\\cinemaPrefs.json"));
        JSONObject object = new JSONObject(tokener);
        String username = (String) object.get("username");
        assertEquals(randomName, username);
    }

    @Test
    public void testHomeCinemaPreferencesStoresDarkMode() throws FileNotFoundException {
        boolean darkMode = randomBoolean();
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method dSetter = cls.getDeclaredMethod("setDarkModePreferred", boolean.class);
            Method saveToFile = cls.getDeclaredMethod("writeJSON");
            dSetter.invoke(instance, darkMode);
            saveToFile.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        JSONTokener tokener = new JSONTokener(new FileReader("assets\\cinemaPrefs.json"));
        JSONObject object = new JSONObject(tokener);
        boolean actualDarkMode = (boolean) object.get("prefersDarkMode");
        assertEquals(darkMode, actualDarkMode);
    }

    private boolean randomBoolean() {
        return randomNumberBetween(0, 2) == 0;
    }

    private int randomNumberBetween(int min, int max) {
        if (max <= min) {
            return 0;
        }
        Random r = new Random();
        int result = r.nextInt(max-min) + min;
        return result;
    }
}

