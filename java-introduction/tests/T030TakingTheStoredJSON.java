import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.*;
import java.lang.annotation.Annotation;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import static org.junit.Assert.*;

public class T030TakingTheStoredJSON {
    private static List<String> beforeJSON = new ArrayList<>();
    private static String randomName;
    private static boolean randomBoolean;

    @BeforeClass
    public static void setTestJSON() {
        int num = (int) Math.floor(Math.random()*100);
        randomName = "RandomName" + num;
        randomBoolean = randomBoolean();

        String file = "assets\\cinemaPrefs.json";
        try {
            FileReader fileReader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String newLine = null;
            do {
                newLine = bufferedReader.readLine();
                if (newLine != null) {
                    beforeJSON.add(newLine);
                }
            } while (newLine != null);
            fileReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            FileWriter fileWriter1 = new FileWriter(file);
            BufferedWriter bufferedWriter1 = new BufferedWriter(fileWriter1);
            bufferedWriter1.write("{");
            bufferedWriter1.newLine();
            bufferedWriter1.write("\"prefersDarkMode\": " + randomBoolean + ",");
            bufferedWriter1.newLine();
            bufferedWriter1.write("\"username\": \""+ randomName +"\"");
            bufferedWriter1.newLine();
            bufferedWriter1.write("}");
            bufferedWriter1.flush();
            fileWriter1.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    @Test
    public void testHomeCinemaPreferencesRetrievesUsername() {
        String actualName = "";
        try {
			Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor(boolean.class).newInstance(true);
            Method usernameGetter = cls.getDeclaredMethod("getUsername");
            actualName = (String) usernameGetter.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals(randomName, actualName);
    }

    @Test
    public void testHomeCinemaPreferencesRetrievesBoolean() {
        boolean actualDarkmode = false;
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor(boolean.class).newInstance(true);
            Method dGetter = cls.getDeclaredMethod("isDarkModePreferred");
            actualDarkmode = (boolean) dGetter.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals(randomBoolean, actualDarkmode);
    }

    @Test
    public void testHomeCinemaPreferencesDeprecatedConstructor() {
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Constructor c = cls.getDeclaredConstructor();
            Annotation[] annotations = c.getDeclaredAnnotations();
            assert(annotations.length > 0);
            assert(annotations[0].annotationType().equals(Deprecated.class));
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        }
    }

    @AfterClass
    public static void restoreJSON() {
        String file = "assets\\cinemaPrefs.json";
        try {
            FileWriter fileWriter = new FileWriter(file);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            for (String line: beforeJSON) {
                bufferedWriter.write(line);
                bufferedWriter.newLine();
            }
            bufferedWriter.flush();
            fileWriter.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean randomBoolean() {
        return randomNumberBetween(0, 2) == 0;
    }

    private static int randomNumberBetween(int min, int max) {
        if (max <= min) {
            return 0;
        }
        Random r = new Random();
        int result = r.nextInt(max-min) + min;
        return result;
    }
}

