import context
import unittest
import xml.etree.ElementTree as ET

class ExistDBSimpleHelloWorldResultTestCase(unittest.TestCase):
    
    def test_xml_is_correct(self):
        tree = ET.parse(context.PROJECT_ROOT + '/exist/results/hello.xql.xml')
        root = tree.getroot()
        self.assertEqual(root.tag, "results")
        for child in root:
            self.assertEqual(child.tag, "message")
            self.assertEqual(child.text, "Hello World!")
        

if __name__ == '__main__':
    unittest.main()
