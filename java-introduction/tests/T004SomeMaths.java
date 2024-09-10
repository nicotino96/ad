import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import static org.junit.Assert.*;

public class T004SomeMaths {

    @Test
    public void testMethodReturnValue() {
        int result = 0;
        Class cls = null;
        try {
            cls = Class.forName("Greeter");
            Method method = cls.getDeclaredMethod("firstNumber");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Object shouldFail = method.invoke(instance);
            fail("No se debería poder invocar el método");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        } catch (IllegalAccessException e) {
            // Good. Method is expected to be private
            assertTrue(true);
        }
        try {
            cls = Class.forName("Greeter");
            Method method = cls.getDeclaredMethod("secondNumber");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Object shouldFail = method.invoke(instance);
            fail("No se debería poder invocar el método");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        } catch (IllegalAccessException e) {
            // Good. Method is expected to be private
            assertTrue(true);
        }
        try {
            cls = Class.forName("Greeter");
            Method method = cls.getDeclaredMethod("sumTwoNumbers");
            Object instance = cls.getDeclaredConstructor().newInstance();
            result = (Integer) method.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        int value1 = 35;
        int value2 = 14;
        assertEquals(value1+value2, result);
    }
}

