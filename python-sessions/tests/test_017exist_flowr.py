import context
import unittest
import xml.etree.ElementTree as ET

class ExistSessionsResultTestCase(unittest.TestCase):
    
    def test_name_is_correct(self):
        tree = ET.parse(context.PROJECT_ROOT + '/exist/results/sessions.xql.xml')
        root = tree.getroot()
        self.assertEqual(root.tag, "register")
        nameTagExists = False
        for child in root:
            if child.tag == 'title':
                nameTagExists = True
                self.assertEqual(child.text, "Harry Potter y el prisionero de Azkaban")
        self.assertTrue(nameTagExists)

    def test_first_element_in_access_times_is_correct(self):
        self.__test_nth_element_is_correct(0)

    def test_second_element_in_access_times_is_correct(self):
        self.__test_nth_element_is_correct(1)

    def test_third_element_in_access_times_is_correct(self):
        self.__test_nth_element_is_correct(2)

    def test_fourth_element_in_access_times_is_correct(self):
        self.__test_nth_element_is_correct(3)

    # Starting in 0
    def __test_nth_element_is_correct(self, n):
        expected_array = self.__get_expected_result()
        tree = ET.parse(context.PROJECT_ROOT + '/exist/results/sessions.xql.xml')
        root = tree.getroot()
        self.assertEqual(root.tag, "register")
        accessTimesExists = False
        for child in root:
            if child.tag == 'accessTimes':
                accessTimesExists = True
                nth_access_time = child[n]
                viewed_by = nth_access_time[0]
                date = nth_access_time[1]
                self.assertEqual(viewed_by.tag, "user")
                self.assertEqual(date.tag, "date")
                self.assertEqual(viewed_by.text, expected_array[n]['user'])
                expected_date = expected_array[n]['day'] + "/" + expected_array[n]['month'] + "/" + expected_array[n]['year']
                self.assertEqual(date.text, expected_date)
        self.assertTrue(accessTimesExists)

   
    def __get_expected_result(self):
        tree = ET.parse(context.PROJECT_ROOT + '/exist/xml/sessions.xml')
        root = tree.getroot()
        result = []
        for child in root:
            matches = False
            for child2 in child:
                if child2.tag == "books":
                    for child3 in child2:
                        for child4 in child3:
                            if child4.tag == "name":
                                if child4.text == "Harry Potter y el prisionero de Azkaban":
                                    matches = True
            if matches:
                for child2 in child:
                    if child2.tag == "username":
                        u = child2.text
                    if child2.tag == "login":
                        for child3 in child2:
                            if child3.tag == "date":
                                for child4 in child3:
                                    if child4.tag == "year":
                                        y = child4.text
                                    if child4.tag == "month":
                                        m = child4.text
                                    if child4.tag == "day":
                                        d = child4.text
                result.append({
                    "user": u,
                    "year": y,
                    "month": m,
                    "day": d
                })
        return sorted(result, key=lambda x: x['user'])



if __name__ == '__main__':
    unittest.main()
