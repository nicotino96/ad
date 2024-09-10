import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import static org.junit.Assert.*;

public class T011RandomNumberInRange {

    @Test
    public void testMethodReturnValue() {
        try {
            Class cls = Class.forName("SimpleMathDemo");
            Method method = cls.getDeclaredMethod("randomNumberInRange", int.class, int.class);
            Object instance = cls.getDeclaredConstructor().newInstance();
            for (int i = 0; i < 50; i++) {
                // Test 50 times with random values
                int num1 = (int) Math.floor(Math.random()*100) - 50;
                int num2 = (int) Math.floor(Math.random()*100) + 1;
                int result = (Integer) method.invoke(instance, num1, num2);
                assertTrue(result >= num1);
                assertTrue(result < num2+num1);
            }
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
            fail("La clase especificada no puede ser instanciada");
        }
    }

    @Test
    public void testMethodReturnValueInvalidParameters() {
        try {
            Class cls = Class.forName("SimpleMathDemo");
            Method method = cls.getDeclaredMethod("randomNumberInRange", int.class, int.class);
            Object instance = cls.getDeclaredConstructor().newInstance();
            for (int i = 0; i < 50; i++) {
                // Test 50 times with random values
                int num1 = (int) Math.floor(Math.random()*100);
                int num2 = (int) Math.floor(Math.random()*-100);
                int result = (Integer) method.invoke(instance, num1, num2);
                assertEquals(-1, result);
            }
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (InvocationTargetException | InstantiationException | IllegalAccessException e) {
            fail("La clase especificada no puede ser instanciada");
        }
    }
}

