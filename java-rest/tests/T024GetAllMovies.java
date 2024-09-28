import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.HttpURLConnection;
import java.net.URL;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class T024GetAllMovies {
    private Method stopServer = null;
    private Object currentServerInstance = null;
    private static List<TestMovie> testMovies = new ArrayList<>(10);

    @BeforeClass
    public static void setupDB() throws IOException {
        backupDatabase();
        String connectionStr = "jdbc:sqlite:db/sqlite3/movies.db";
        try {
            Connection conn = DriverManager.getConnection(connectionStr);
            for (int i = 0; i < 10; i++) {
                TestMovie m = new TestMovie("ATitle", (int)(Math.random()*1000), (int)(Math.random()*200), "US", "drama", "To be described!");
                conn.setAutoCommit(false);
                Statement statement = conn.createStatement();
                statement.executeUpdate("INSERT INTO TMovies(title, year, duration, countryIso3166, genre, synopsis) VALUES('" + m.getTitle() + "', " + m.getYear() + "," + m.getDuration() + ",'" + m.getCountryIso3166() + "','" + m.getGenre() + "','" + m.getSynopsis() + "')");
                Statement statement2 = conn.createStatement();
                ResultSet result = statement2.executeQuery("SELECT last_insert_rowid()");
                while (result.next()) {
                    m.setId(result.getInt(1));
                }
                conn.commit();
                testMovies.add(m);
            }
            conn.close();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        for (TestMovie m : testMovies) {
            System.out.println(m);
        }
    }

    @Test
    public void testResultSizeMatchesAtLeastAllTestMovies() {
        try {
            Class cls = Class.forName("MoviesREST");
            Class cls2 = Class.forName("GetAllMovies");
            Class cls3 = Class.forName("Movie");
            this.currentServerInstance = cls.getDeclaredConstructor().newInstance();
            this.stopServer = cls.getDeclaredMethod("stopServer");
            Method runServer = cls.getDeclaredMethod("runServer");
            runServer.invoke(this.currentServerInstance);
            JSONArray result = getUrl("http://localhost:8125/movies");
            assert(result != null);
            assert(result.length() >= testMovies.size());
            this.stopServer.invoke(this.currentServerInstance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("Puede que el servidor de Main.java siga activo. Dale a STOP (recuadro rojo) en la barra superior, y re-lanza el test");
        }
    }

    @Test
    public void testResultContainsAllTestMovies() {
        try {
            Class cls = Class.forName("MoviesREST");
            Class cls2 = Class.forName("GetAllMovies");
            Class cls3 = Class.forName("Movie");
            this.currentServerInstance = cls.getDeclaredConstructor().newInstance();
            this.stopServer = cls.getDeclaredMethod("stopServer");
            Method runServer = cls.getDeclaredMethod("runServer");
            runServer.invoke(this.currentServerInstance);
            JSONArray result = getUrl("http://localhost:8125/movies");
            assert(result != null);
            for (TestMovie movie : testMovies) {
                assert(existsInJSONArray(result, movie));
            }
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

    @AfterClass
    public static void restore() throws IOException {
        restoreDatabase();
    }

    private static void backupDatabase() throws IOException {
        copyFile("db/sqlite3/movies.db", "db/sqlite3/movies_test_backup.db");
    }

    private static void restoreDatabase() throws IOException {
        copyFile("db/sqlite3/movies_test_backup.db", "db/sqlite3/movies.db");
        File backup = new File("db/sqlite3/movies_test_backup.db");
        backup.delete();
    }

    private static void copyFile(String source, String target) throws IOException {
        InputStream is = null;
        OutputStream os = null;
        try {
            is = new FileInputStream(source);
            os = new FileOutputStream(target);
            byte [] buffer = new byte[1024];
            int length;
            while ((length = is.read(buffer)) > 0) {
                os.write(buffer, 0, length);
            }
        } finally {
            is.close();
            os.close();
        }
    }

    private JSONArray getUrl(String url) {
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
            return new JSONArray(result.toString());
        } catch (IOException e) {
            e.printStackTrace();
            fail("JSON was malformed or couldn't connect to server (or other bad thing happened)");
        }
        return null;
    }

    private boolean existsInJSONArray(JSONArray array, TestMovie movie) {
        for (int i = 0; i < array.length(); i++) {
            TestMovie current = new TestMovie(array.getJSONObject(i));
            if (current.equals(movie)) {
                return true;
            }
        }
        return false;
    }

    private static class TestMovie {
        private int id;
        private String title;
        private int year;
        private int duration;
        private String countryIso3166;
        private String genre;
        private String synopsis;

        TestMovie(String title, int year, int duration, String countryIso3166, String genre, String synopsis) {
            this.title = title;
            this.year = year;
            this.duration = duration;
            this.countryIso3166 = countryIso3166;
            this.genre = genre;
            this.synopsis = synopsis;
        }

        TestMovie(JSONObject json) {
            this.id = json.getInt("id");
            this.title = json.getString("title");
            this.year = json.getInt("year");
            this.duration = json.getInt("duration");
            this.countryIso3166 = json.getString("countryIso3166");
            this.genre = json.getString("genre");
            this.synopsis = json.getString("synopsis");
        }

        void setId(int id) {
            this.id = id;
        }

        public String getTitle() {
            return title;
        }

        public int getYear() {
            return year;
        }

        public int getDuration() {
            return duration;
        }

        public String getCountryIso3166() {
            return countryIso3166;
        }

        public String getGenre() {
            return genre;
        }

        public String getSynopsis() {
            return synopsis;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            TestMovie testMovie = (TestMovie) o;
            return id == testMovie.id && year == testMovie.year && duration == testMovie.duration && title.equals(testMovie.title) && countryIso3166.equals(testMovie.countryIso3166) && genre.equals(testMovie.genre) && synopsis.equals(testMovie.synopsis);
        }
    }
}

