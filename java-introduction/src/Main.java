import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.TransformerException;

public class Main {
    public static void main(String[] args) throws ParserConfigurationException, TransformerException {
        SimpleMathDemo demo = new SimpleMathDemo();
        System.out.println(demo.randomNumberInRange(1,5));
        System.out.println(demo.randomNumberBetween(2,5));
        System.out.println(demo.getTheSmallerValue(1,2,3,4));
        HomeCinemaPreferences hcp = new HomeCinemaPreferences();
        hcp.saveExampleXML();

    }
}

