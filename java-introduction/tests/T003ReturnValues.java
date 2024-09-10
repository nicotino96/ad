import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import static org.junit.Assert.*;

public class T003ReturnValues {

    @Test
    public void testMethodReturnValue() {
        String result = "";
        try {
            Class cls = Class.forName("Greeter");
            Method method = cls.getDeclaredMethod("byeWorld");
            Object instance = cls.getDeclaredConstructor().newInstance();
            result = (String) method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertEquals("Bye!", result);
    }
}

