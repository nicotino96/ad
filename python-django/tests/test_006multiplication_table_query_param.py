import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class SimpleAPIMultiplicationQueryParamEndpointTestCase(unittest.TestCase):

    def test_rand_number1to10_produce_correct_http_response(self):
        def test_body():
            r = random.randint(1, 11)
            self.__assert_endpoint("v3/multiplications?i=" + str(r), self.__table(r))
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_missing_parameter_returns_correct_error_response(self):
        def test_body():
            self.__assert_endpoint("v3/multiplications", {"error": "Missing 'i' parameter"}, 400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_bad_parameter_returns_correct_error_response(self):
        def test_body():
            self.__assert_endpoint("v3/multiplications?i=false", {"error": "Parameter 'i' must be a number"}, 400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_rand_number_negative_produces_correct_http_response(self):
        def test_body():
            r = random.randint(-100, 0)
            self.__assert_endpoint("v3/multiplications?i=" + str(r), self.__table(r))
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

    def __assert_endpoint(self, endpoint, json_content, status_code=200):
        response = requests.get("http://localhost:8000/" + endpoint)
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.json(), json_content)

    def __table(self, n):
        return list(map(lambda x: (x * n), range(1, 11)))


if __name__ == '__main__':
    unittest.main()

