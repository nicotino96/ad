import org.junit.Test;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

public class T011AGoodDataConnector {
    @Test
    public void testAttributeIsPrivate() {
        try {
            Class cls = Class.forName("MoviesConnector");
            Field field = cls.getDeclaredField("connection");
            Method close = cls.getDeclaredMethod("closeConnection");
            Object instance = cls.getDeclaredConstructor().newInstance();
            close.invoke(instance);
            field.get(instance);
            fail("connection field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
    }
}
