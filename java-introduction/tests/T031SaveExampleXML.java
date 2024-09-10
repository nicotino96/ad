import org.junit.BeforeClass;
import org.junit.Test;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Random;

import static org.junit.Assert.*;

public class T031SaveExampleXML {

    @BeforeClass
    public static void clearXMLs() {
        String file1 = "assets\\example.xml";
        try {
            FileWriter fileWriter1 = new FileWriter(file1);
            BufferedWriter bufferedWriter1 = new BufferedWriter(fileWriter1);
            bufferedWriter1.write("");
            bufferedWriter1.flush();
            fileWriter1.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }

    @Test
    public void testHomeCinemaPreferencesWriteExample() {
        try {
            Class cls = Class.forName("HomeCinemaPreferences");
            Object instance = cls.getDeclaredConstructor().newInstance();
            Method saveToFile = cls.getDeclaredMethod("saveExampleXML");
            saveToFile.invoke(instance);
        } catch (ClassNotFoundException e) {
            fail("La clase especificada no existe");
        } catch (NoSuchMethodException e) {
            fail("La clase especificada no contiene un metodo con el nombre indicado o con un constructor apropiado");
        } catch (IllegalAccessException | InvocationTargetException | InstantiationException e) {
            fail("La clase especificada no puede ser instanciada");
        }
        assertXMLContainsLevel0NodeWithValue("assets\\example.xml", "Student");
        assertXMLContainsLevel1NodeWithTextContent("assets\\example.xml", "Name", "Pepe Depura");
        assertXMLContainsLevel1NodeWithTextContent("assets\\example.xml", "IsLearning", "true");
    }

    

    private void assertXMLContainsLevel0NodeWithValue(String xmlFile, String nodeName) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document xmlDocument = builder.parse(xmlFile);
            Element rootElement = xmlDocument.getDocumentElement();
            assertEquals(nodeName, rootElement.getNodeName());
        } catch (IOException | SAXException | ParserConfigurationException e) {
            fail("There was an exception");
        }
    }

    private void assertXMLContainsLevel1NodeWithTextContent(String xmlFile, String nodeName, String content) {
        try {
            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = factory.newDocumentBuilder();
            Document xmlDocument = builder.parse(xmlFile);

            Element rootElement = xmlDocument.getDocumentElement();
            NodeList childNodes = rootElement.getChildNodes();
            for (int i = 0; i < childNodes.getLength(); i++) {
                Node child = childNodes.item(i);
                if (child.getNodeName().equals(nodeName)) {
                    assertEquals(content, child.getTextContent());
                    return;
                }
            }
        } catch (IOException | SAXException | ParserConfigurationException e) {
            fail("There was an exception");
        }
        fail("The searched node " + nodeName + " was not found");
    }
}

