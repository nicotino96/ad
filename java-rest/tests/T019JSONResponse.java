import org.json.JSONObject;
import org.junit.After;
import org.junit.Test;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.HttpURLConnection;
import java.net.URL;
import static org.junit.Assert.*;

public class T019JSONResponse {
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
            JSONObject result = getUrl("http://localhost:8125/example3");
            assert(result != null);
            assertEquals("Esto es un JSON de prueba", result.getString("message"));
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

    private JSONObject getUrl(String url) {
        try {
            URL endpointURL = new URL(url);
            HttpURLConnection httpConnection = (HttpURLConnection) endpointURL.openConnection();
            String contentType = httpConnection.getHeaderField("Content-Type");
            assertTrue(contentType.contains("application/json"));
            InputStream is = httpConnection.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(is));
            String line;
            StringBuilder result = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                result.append(line);
            }
            is.close();
            return new JSONObject(result.toString());
        } catch (IOException e) {
            e.printStackTrace();
            fail("JSON was malformed or couldn't connect to server (or other bad thing happened)");
        }
        return null;
    }
}
