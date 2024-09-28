import org.junit.After;
import org.junit.Test;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.HttpURLConnection;
import java.net.URL;

import static org.junit.Assert.*;

public class T026GetMovieByID404 {
    private Method stopServer = null;
    private Object currentServerInstance = null;

    @Test
    public void testNotFoundHasCorrectPhrase() {
        int randomInvalidID = (int) Math.floor((Math.random()*1000000)+1000000);
        try {
            Class cls = Class.forName("MoviesREST");
            this.currentServerInstance = cls.getDeclaredConstructor().newInstance();
            this.stopServer = cls.getDeclaredMethod("stopServer");
            Method runServer = cls.getDeclaredMethod("runServer");
            runServer.invoke(this.currentServerInstance);
            String result = get404Url("http://localhost:8125/movies/" + randomInvalidID);
            assert(result != null);
            assert(result.contains("The film was not found"));
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

    private String get404Url(String url) {
        try {
            URL endpointURL = new URL(url);
            HttpURLConnection httpConnection = (HttpURLConnection) endpointURL.openConnection();
            assertEquals(404, httpConnection.getResponseCode());
            InputStream es = httpConnection.getErrorStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(es));
            String line;
            StringBuilder result = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                result.append(line);
            }
            es.close();
            return result.toString();
        } catch (IOException e) {
            e.printStackTrace();
            fail("Couldn't connect to server (or other bad thing happened)");
        }
        return null;
    }
}
