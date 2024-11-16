import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class IdeAPICategoriesEndpointTestCase(unittest.TestCase):
    random_title1 = "Title" + str(random.randint(1, 10000))
    random_title2 = "Title" + str(random.randint(1, 10000))
    random_title3 = "Title" + str(random.randint(1, 10000))

    def setUp(self):
        # Generate fixture file for manage.py testserver argument
        file = open("test_010get_all_categories.json", "w")
        file.write('''[
{
 "model": "idearest25app.category",
 "pk": 1,
 "fields": {
  "title": "''' +self.random_title1+'''"
 }
},
{
 "model": "idearest25app.category",
 "pk": 2,
 "fields": {
  "title": "''' +self.random_title2+'''"
 }
},
{
 "model": "idearest25app.category",
 "pk": 3,
 "fields": {
  "title": "''' +self.random_title3+'''"
 }
}
]
        ''')
        file.close()

    def test_all_categories_contains_expected_first_element(self):
        self.__test_get_returns_element(1, self.random_title1)

    def test_all_categories_contains_expected_second_element(self):
        self.__test_get_returns_element(2, self.random_title2)
        
    def test_all_categories_contains_expected_third_element(self):
        self.__test_get_returns_element(3, self.random_title3)

    def __test_get_returns_element(self, id, title):
        def test_body():
            expected = {
                "category_id": id,
                "category_name": title
            }
            self.__assert_get_array_endpoint("v1/categories", expected_json_length=3, expected_element_in_response=expected)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_010get_all_categories.json --noinput ", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.IDEAPI_ROOT)
            time.sleep(4)
            proc.send_signal(signal.CTRL_BREAK_EVENT)
            time.sleep(1)
            proc.kill()

        def app_dir_exists():
            return os.path.isdir(context.IDEAPI_ROOT + "idearest25app")

        self.assertTrue(app_dir_exists())
        t = threading.Thread(target=run_server)
        t.start()
        time.sleep(1)
        block()
        t.join(timeout=6)

    def __assert_get_array_endpoint(self, endpoint, expected_json_length, expected_element_in_response):
        response = requests.get("http://localhost:8000/" + endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), expected_json_length)
        element_is_contained = False
        for e in response.json():
            if e == expected_element_in_response:
                element_is_contained = True
                break
        self.assertTrue(element_is_contained)

        
if __name__ == '__main__':
    unittest.main()
