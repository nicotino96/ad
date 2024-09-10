import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T027Preferences {

    @Test
    public void testHomeCinemaPreferencesGetter() {
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method usernameGetter = cls.getDeclaredMethod("getUsername");
            Method darkModeGetter = cls.getDeclaredMethod("isDarkModePreferred");
            assertEquals("John Doe", usernameGetter.invoke(instance));
            assertEquals(true, darkModeGetter.invoke(instance));
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
    }
}

