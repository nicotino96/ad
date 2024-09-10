import org.junit.Test;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

import static org.junit.Assert.*;

public class T017WhatIsAPojo {

    @Test
    public void testConstructorAndGetters() {
        int num = (int) Math.floor(Math.random()*100);
        String name = "Nombre" + num;
        String species = "Species" + num;
        try {
            Class cls = Class.forName("Animal");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            Method getter1 = cls.getDeclaredMethod("getName");
            Method getter2 = cls.getDeclaredMethod("getSpecies");
            String actualName = (String) getter1.invoke(instance);
            String actualSpecies = (String) getter2.invoke(instance);
            assertEquals(name, actualName);
            assertEquals(species, actualSpecies);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        try {
            Class cls = Class.forName("Animal");
            Field field = cls.getDeclaredField("name");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            field.get(instance);
            fail("name field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("Animal");
            Field field = cls.getDeclaredField("species");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            field.get(instance);
            fail("name field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("Animal");
            Field field = cls.getDeclaredField("numberOfTeeth");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            field.get(instance);
            fail("name field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
    }

    @Test
    public void testConstructorSettersGetters() {
        int num = (int) Math.floor(Math.random()*100);
        String name = "Nombre" + num;
        String species = "Species" + num;
        try {
            Class cls = Class.forName("Animal");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            Method getter1 = cls.getDeclaredMethod("getName");
            Method getter2 = cls.getDeclaredMethod("getSpecies");
            Method setter1 = cls.getDeclaredMethod("setName", String.class);
            Method setter2 = cls.getDeclaredMethod("setSpecies", String.class);
            setter1.invoke(instance, name + "2");
            setter2.invoke(instance, species + "2");
            String actualName = (String) getter1.invoke(instance);
            String actualSpecies = (String) getter2.invoke(instance);
            assertEquals(name + "2", actualName);
            assertEquals(species + "2", actualSpecies);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        try {
            Class cls = Class.forName("Animal");
            Field field = cls.getDeclaredField("name");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            field.get(instance);
            fail("name field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("Animal");
            Field field = cls.getDeclaredField("species");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            field.get(instance);
            fail("name field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
        try {
            Class cls = Class.forName("Animal");
            Field field = cls.getDeclaredField("numberOfTeeth");
            Object instance = cls.getDeclaredConstructor(String.class, String.class, int.class).newInstance(name, species, num);
            field.get(instance);
            fail("name field is expected to be private");
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchFieldException e) {
            fail("No se ha hallado el atributo name");
        } catch (NoSuchMethodException | InvocationTargetException | InstantiationException e) {
            fail("No se ha hallado el constructor o ha dado problemas");
        } catch (IllegalAccessException e) {
            assertTrue(true);
        }
    }
}
