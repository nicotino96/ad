import context
import os
import requests
import secrets
import signal
import subprocess
import threading
import time
import unittest


class IdeAPIGetIdeasEndpointTestCase(unittest.TestCase):

    def setUp(self):
        # Generate fixture file for manage.py testserver argument
        file = open("test_012retrieve_ideas.json", "w")
        file.write('''[
{
 "model": "idearest25app.category",
 "pk": 1,
 "fields": {
  "title": "Cat1"
 }
},
{
 "model": "idearest25app.category",
 "pk": 2,
 "fields": {
  "title": "Cat2"
 }
},
{
 "model": "idearest25app.customuser",
 "pk": 1,
 "fields": {
  "e_mail": "''' + "test_" + str(time.time()) + "@test.co.uk" + '''",
  "username": "Test User",
  "encrypted_password": "$2b$12$Re22Ht4N5pZxrLGEgZcy..ZmrycSInMpWE.Lk6BYcYyw7OufwzvBS"
 }
},
{
 "model": "idearest25app.customuser",
 "pk": 2,
 "fields": {
  "e_mail": "''' + "test2_" + str(time.time()) + "@test.co.uk" + '''",
  "username": "Test User",
  "encrypted_password": "$2b$12$Re22Ht4N5pZxrLGEgZcy..ZmrycSInMpWE.Lk6BYcYyw7OufwzvBS"
 }
},
{
 "model": "idearest25app.customuser",
 "pk": 3,
 "fields": {
  "e_mail": "''' + "test3_" + str(time.time()) + "@test.co.uk" + '''",
  "username": "Test User",
  "encrypted_password": "$2b$12$Re22Ht4N5pZxrLGEgZcy..ZmrycSInMpWE.Lk6BYcYyw7OufwzvBS"
 }
},
{
 "model": "idearest25app.idea",
 "pk": 1,
 "fields": {
  "title": "Idea1",
  "description": "Description1",
  "user": 1,
  "category": 1
 }
},
{
 "model": "idearest25app.idea",
 "pk": 2,
 "fields": {
  "title": "Idea2",
  "description": "Description2",
  "user": 3,
  "category": 1
 }
},
{
 "model": "idearest25app.idea",
 "pk": 3,
 "fields": {
  "title": "Idea3",
  "description": "Description3",
  "user": 2,
  "category": 2
 }
},
{
 "model": "idearest25app.idea",
 "pk": 4,
 "fields": {
  "title": "Idea4",
  "description": "Description4",
  "user": 2,
  "category": 2
 }
}
]
        ''')
        file.close()

    def test_category_not_valid_response(self):
        def test_body():
            self.__assert_get_array_endpoint("v1/categories/3/ideas", expected_status_code=404)

        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_get1(self):
        def test_body():
            expected = {
                "id": 1,
                "author_id": 1,
                "idea_name": "Idea1",
                "description": "Description1"
            }
            self.__assert_get_array_endpoint("v1/categories/1/ideas", expected_element_in_response=expected, expected_json_length=2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_get2(self):
        def test_body():
            expected = {
                "id": 2,
                "author_id": 3,
                "idea_name": "Idea2",
                "description": "Description2"
            }
            self.__assert_get_array_endpoint("v1/categories/1/ideas", expected_element_in_response=expected, expected_json_length=2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_get3(self):
        def test_body():
            expected = {
                "id": 3,
                "author_id": 2,
                "idea_name": "Idea3",
                "description": "Description3"
            }
            self.__assert_get_array_endpoint("v1/categories/2/ideas", expected_element_in_response=expected, expected_json_length=2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_get4(self):
        def test_body():
            expected = {
                "id": 4,
                "author_id": 2,
                "idea_name": "Idea4",
                "description": "Description4"
            }
            self.__assert_get_array_endpoint("v1/categories/2/ideas", expected_element_in_response=expected, expected_json_length=2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_012retrieve_ideas.json --noinput", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.IDEAPI_ROOT)
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

    def __assert_get_array_endpoint(self, endpoint, expected_json_length=None, expected_element_in_response=None, expected_status_code = 200):
        response = requests.get("http://localhost:8000/" + endpoint)
        self.assertEqual(response.status_code, expected_status_code)
        if expected_json_length is not None:
            self.assertEqual(len(response.json()), expected_json_length)
        if expected_element_in_response is not None:
            element_is_contained = False
            for e in response.json():
                if e == expected_element_in_response:
                    element_is_contained = True
                    break
            self.assertTrue(element_is_contained)


if __name__ == '__main__':
    unittest.main()

