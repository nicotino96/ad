import org.json.JSONArray;
import org.json.JSONObject;
import org.json.JSONTokener;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

public class T033TimeRegister {
    private static List<String> beforeJSON = new ArrayList<>();

    @BeforeClass
    public static void backupJSONAndClear() {
        String file = "assets\\hours.json";
        try {
            FileReader fileReader = new FileReader(file);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String newLine = null;
            do {
                newLine = bufferedReader.readLine();
                if (newLine != null) {
                    beforeJSON.add(newLine);
                }
            } while (newLine != null);
            fileReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            FileWriter fileWriter1 = new FileWriter(file);
            BufferedWriter bufferedWriter1 = new BufferedWriter(fileWriter1);
            bufferedWriter1.write("");
            bufferedWriter1.flush();
            fileWriter1.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    // 1 Test Method raises exception
    @Test
    public void testMethodException() {
        try {
            Class cls = Class.forName("TimeRegister");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("registerTime", short.class, short.class);
            method.invoke(instance, (short) -1, (short) 0);
            fail("Se ha permitido invocar el método");
        } catch (ClassNotFoundException |NoSuchMethodException| IllegalAccessException | InstantiationException e) {
            fail("Problemas genéricos");
        } catch (InvocationTargetException  e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("TimeRegister");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("registerTime", short.class, short.class);
            method.invoke(instance, (short) 0, (short) -1);
            fail("Se ha permitido invocar el método");
        } catch (ClassNotFoundException |NoSuchMethodException| IllegalAccessException | InstantiationException e) {
            fail("Problemas genéricos");
        } catch (InvocationTargetException  e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("TimeRegister");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("registerTime", short.class, short.class);
            method.invoke(instance, (short) 24, (short) 5);
            fail("Se ha permitido invocar el método");
        } catch (ClassNotFoundException |NoSuchMethodException| IllegalAccessException | InstantiationException e) {
            fail("Problemas genéricos");
        } catch (InvocationTargetException  e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("TimeRegister");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("registerTime", short.class, short.class);
            method.invoke(instance, (short) 5, (short) 24);
            fail("Se ha permitido invocar el método");
        } catch (ClassNotFoundException |NoSuchMethodException| IllegalAccessException | InstantiationException e) {
            fail("Problemas genéricos");
        } catch (InvocationTargetException  e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("TimeRegister");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("registerTime", short.class, short.class);
            method.invoke(instance, (short) 11, (short) 10);
            fail("Se ha permitido invocar el método");
        } catch (ClassNotFoundException |NoSuchMethodException| IllegalAccessException | InstantiationException e) {
            fail("Problemas genéricos");
        } catch (InvocationTargetException  e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("TimeRegister");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("registerTime", short.class, short.class);
            method.invoke(instance, (short) 5, (short) 10);
            assertTrue(true);
        } catch (ClassNotFoundException |NoSuchMethodException| IllegalAccessException | InstantiationException e) {
            fail("Problemas genéricos");
        } catch (InvocationTargetException  e) {
            fail("No se ha permitido invocar el método con parámetros correctos");
        }
    }

    // 2 Test no records
    @Test
    public void testNoRecords() throws FileNotFoundException {
        testCase(new ArrayList<>());
    }

    // 3 Test one record
    @Test
    public void testOneRecord() throws FileNotFoundException {
        List<HoursInnerTestClass> testRecords = new ArrayList<>();
        testRecords.add(new HoursInnerTestClass((short)8, (short)15));
        testCase(testRecords);
    }

    // 4 Test two records
    @Test
    public void testTwoRecords() throws FileNotFoundException {
        List<HoursInnerTestClass> testRecords = new ArrayList<>();
        testRecords.add(new HoursInnerTestClass((short)8, (short)15));
        testRecords.add(new HoursInnerTestClass((short)8, (short)23));
        testCase(testRecords);
    }

    // 5 Test three records
    @Test
    public void testThreeRecords() throws FileNotFoundException {
        List<HoursInnerTestClass> testRecords = new ArrayList<>();
        testRecords.add(new HoursInnerTestClass((short)0, (short)1));
        testRecords.add(new HoursInnerTestClass((short)8, (short)15));
        testRecords.add(new HoursInnerTestClass((short)7, (short)23));
        testCase(testRecords);
    }

    // 6 Test 40 random records
    @Test
    public void test40RandomRecords() throws FileNotFoundException {
        List<HoursInnerTestClass> testRecords = new ArrayList<>();
        for (int i = 0; i < 40; i++) {
            short num1 = (short) Math.floor(Math.random()*20);
            short num2 = (short) Math.floor(Math.random()*20);
            short entrance = (short) Math.min(num1, num2);
            short exit = (short) (Math.max(num1, num2) + 1);
            testRecords.add(new HoursInnerTestClass(entrance, exit));
        }
        testCase(testRecords);
    }

    @AfterClass
    public static void restoreJSON() {
        String file = "assets\\hours.json";
        try {
            FileWriter fileWriter = new FileWriter(file);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            for (String line: beforeJSON) {
                bufferedWriter.write(line);
                bufferedWriter.newLine();
            }
            bufferedWriter.flush();
            fileWriter.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private void testCase(List<HoursInnerTestClass> toRecord) throws FileNotFoundException {
        try {
            Class cls = Class.forName("TimeRegister");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method method = cls.getDeclaredMethod("registerTime", short.class, short.class);
            for (HoursInnerTestClass h : toRecord) {
                method.invoke(instance, h.getEntranceHour(), h.getExitHour());
            }
            Method methodSaveJson = cls.getDeclaredMethod("storeJSON");
            methodSaveJson.invoke(instance);
        } catch (InvocationTargetException|ClassNotFoundException |NoSuchMethodException| IllegalAccessException | InstantiationException e) {
            fail("Problemas genéricos al instanciar la clase");
        }
        // And now check the result
        JSONTokener tokener = new JSONTokener(new FileReader("assets\\hours.json"));
        JSONObject object = new JSONObject(tokener);
        JSONArray records = object.getJSONArray("registers");
        assertEquals(toRecord.size(), records.length());
        assertEquals(calculateTotalTime(toRecord), object.getInt("totalTime"));
        for (int i = 0; i < records.length(); i++) {
            JSONObject someRecord = records.getJSONObject(i);
            HoursInnerTestClass someHours = toRecord.get(i);
            // Here we trust the correct order is respected
            assertEquals(someHours.getEntranceHour(), someRecord.getInt("entranceHour"));
            assertEquals(someHours.getExitHour(), someRecord.getInt("exitHour"));
        }
    }

    private int calculateTotalTime(List<HoursInnerTestClass> hours) {
        int total = 0;
        for (HoursInnerTestClass h : hours) {
            total+=(h.getExitHour()-h.getEntranceHour());
        }
        return total;
    }

    class HoursInnerTestClass {
        private short entranceHour;
        private short exitHour;

        public HoursInnerTestClass(short entranceHour, short exitHour) {
            this.entranceHour = entranceHour;
            this.exitHour = exitHour;
        }

        public short getEntranceHour() {
            return entranceHour;
        }

        public short getExitHour() {
            return exitHour;
        }
    }
}




