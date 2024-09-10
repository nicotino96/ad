import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import static org.junit.Assert.*;

public class T013SmallerNumber {

    @Test
    public void testMethodReturnValueWithPositiveAndZeroInput() {
        try {
            Class cls = Class.forName("SimpleMathDemo");
            Method method = cls.getDeclaredMethod("getTheSmallerValue", int.class, int.class, int.class, int.class);
            Object instance = cls.getDeclaredConstructor().newInstance();
            for (int i = 0; i < 50; i++) {
                // Test 50 times with random values
                int num1 = (int) Math.floor(Math.random()*100);
                int num2 = (int) Math.floor(Math.random()*100);
                int num3 = (int) Math.floor(Math.random()*100);
                int num4 = 0;
                int result = (Integer) method.invoke(instance, num1, num2, num3, num4);
                assertEquals(0, result);
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
    public void testMethodReturnValueWithNegativeInput() {
        try {
            Class cls = Class.forName("SimpleMathDemo");
            Method method = cls.getDeclaredMethod("getTheSmallerValue", int.class, int.class, int.class, int.class);
            Object instance = cls.getDeclaredConstructor().newInstance();
            for (int i = 0; i < 50; i++) {
                // Test 50 times with random values
                int num1 = (int) Math.floor(Math.random()*-100);
                int num2 = (int) Math.floor(Math.random()*-100);
                int num3 = (int) Math.floor(Math.random()*-100);
                int num4 = (int) Math.floor(Math.random()*-100);
                int expected = Math.min(Math.min(Math.min(num1, num2), num3), num4);
                int result = (Integer) method.invoke(instance, num1, num2, num3, num4);
                assertEquals(expected, result);
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


