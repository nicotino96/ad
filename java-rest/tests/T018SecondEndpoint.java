import org.junit.After;
import org.junit.Test;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLConnection;
import static org.junit.Assert.*;

public class T018SecondEndpoint {
    private Method stopServer = null;
    private Object currentServerInstance = null;

    @Test
    public void testExampleEndpoint() {
        try {
            Class cls = Class.forName("SimpleREST");
            this.currentServerInstance = cls.getDeclaredConstructor().newInstance();
            this.stopServer = cls.getDeclaredMethod("stopServer");
            Method runServer = cls.getDeclaredMethod("runServer");
            runServer.invoke(this.currentServerInstance);
            String result = getUrl("http://localhost:8125/example2");
            assert(result != null);
            assertTrue(result.contains("El secreto de la vida es..."));
            this.stopServer.invoke(this.currentServerInstance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("Puede que el servidor de Main.java siga activo. Dale a STOP (recuadro rojo) en la barra superior, y re-lanza el test");
        }
    }

    @After
    public void teardownServer() {
        try {
            if ((stopServer != null) && (this.currentServerInstance != null)) {
                stopServer.invoke(this.currentServerInstance);
            }
        } catch (IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }
    }

    private String getUrl(String url) {
        try {
            URL endpointURL = new URL(url);
            URLConnection httpConnection = endpointURL.openConnection();
            InputStream is = httpConnection.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(is));
            String line;
            StringBuilder result = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                result.append(line);
            }
            is.close();
            return result.toString();
        } catch (IOException e) {
            fail("Couldn't connect to server or other bad thing happened");
        }
        return null;
    }
}

