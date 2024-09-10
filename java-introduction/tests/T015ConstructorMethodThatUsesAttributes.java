import org.junit.Test;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import static org.junit.Assert.*;

public class T015ConstructorMethodThatUsesAttributes {

    @Test
    public void testNameIsPrivate() {
        try {
            Class cls = Class.forName("Person");
            Field field = cls.getDeclaredField("name");
            Object instance = cls.getDeclaredConstructor(String.class).newInstance("Anything");
            field.get(instance);
            fail("name field is expected to be private");
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

