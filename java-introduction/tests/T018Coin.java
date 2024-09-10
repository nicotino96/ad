import org.junit.Test;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import static org.junit.Assert.*;

public class T018Coin {

    @Test
    public void testClassConstructorAndException() {
        int num = (int) Math.floor(Math.random()*100) + 1;
        try {
            Class cls = Class.forName("Coin");
            Object instance = cls.getDeclaredConstructor(int.class).newInstance(num);
            assertTrue(true);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        try {
            Class cls = Class.forName("Coin");
            Object instance = cls.getDeclaredConstructor(int.class).newInstance(0);
            fail("Coin is supposed to throw RuntimeException if initialized with 0 or negative");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InstantiationException e) {
            fail("Error no esperado");
        } catch (InvocationTargetException e) {
            assertTrue(true);
        }
        int negativeNum = (int) Math.floor(Math.random()*-100) - 1;
        try {
            Class cls = Class.forName("Coin");
            Object instance = cls.getDeclaredConstructor(int.class).newInstance(negativeNum);
            fail("Coin is supposed to throw RuntimeException if initialized with 0 or negative");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InstantiationException e) {
            fail("Error no esperado");
        } catch (InvocationTargetException e) {
            assertTrue(true);
        }
    }

    @Test
    public void testOutputMessages() {
        int num = (int) Math.floor(Math.random()*100) + 1;
        try {
            Class cls = Class.forName("Coin");
            Object instance = cls.getDeclaredConstructor(int.class).newInstance(num);
            Method method = cls.getDeclaredMethod("flip");
            boolean winOutputHappened = false;
            boolean loseOutputHappened = false;
            for (int i = 0; i < 100; i++) {
                String output = (String) method.invoke(instance);
                if (output.equals("Has tirado al aire la moneda y ha salido cruz. Perdiste")) {
                    loseOutputHappened = true;
                } else if (output.equals("Has tirado al aire la moneda y ha salido cara. Has ganado " + num + " euros")) {
                    winOutputHappened = true;
                } else {
                    fail("The output message didn't correspond to any of the specified ones. Maybe review commas (,) or points (.) ?");
                }
            }
            assertTrue("One of the outputs (win message, or lose message) never took place although I flipped the coin 100 times! Are you sure a random value is returned?", winOutputHappened && loseOutputHappened);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
    }
}
