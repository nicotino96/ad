import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class SimpleAPIPostFavoriteAnimalEndpointTestCase(unittest.TestCase):

    def test_animal_method_not_allowed_error_response(self):
        def test_body():
            self.__assert_endpoint("favorite_animal", client_json=None, expected_json_content=None, expected_status_code=405)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_animal_bad_request_wrong_body_error_response(self):
        def test_body():
            self.__assert_endpoint("favorite_animal", client_json={"wrong": "Haha"}, expected_status_code=400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_animal_bad_request_missing_body_error_response(self):
        def test_body():
            response = requests.post("http://localhost:8000/favorite_animal")
            self.assertEqual(response.status_code, 400)
       # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_animal_cat_response(self):
        def test_body():
            self.__assert_endpoint("favorite_animal", client_json={"name": "Cat"}, expected_json_content={"message": "Nice! Seven lives will be enough"}, expected_status_code=200)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_animal_other_response(self):
        def test_body():
            r = "test" + str(random.randint(1, 1000))
            self.__assert_endpoint("favorite_animal", client_json={"name": r}, expected_json_content={"message": "OK! Have a nice day"}, expected_status_code=200)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py runserver", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.SIMPLE_API_ROOT)
            time.sleep(4)
            proc.send_signal(signal.CTRL_BREAK_EVENT)
            time.sleep(1)
            proc.kill()

        def app_dir_exists():
            return os.path.isdir(context.SIMPLE_API_ROOT + "simplerest25app")

        self.assertTrue(app_dir_exists())
        t = threading.Thread(target=run_server)
        t.start()
        time.sleep(1)
        block()
        t.join(timeout=6)

    def __assert_endpoint(self, endpoint, client_json=None, expected_json_content=None, expected_status_code=200):
        if client_json is None:
            response = requests.get("http://localhost:8000/" + endpoint)
        else:
            response = requests.post("http://localhost:8000/" + endpoint, json=client_json)
        if expected_status_code is not None:
            self.assertEqual(response.status_code, expected_status_code)
        if expected_json_content is not None:
            self.assertEqual(response.json(), expected_json_content)


if __name__ == '__main__':
    unittest.main()
