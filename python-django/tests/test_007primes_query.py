import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class SimpleAPIPrimesQueryEndpointTestCase(unittest.TestCase):

    def test_zero_returns_error(self):
        def test_body():
            self.__assert_endpoint("prime?q=0", {"error": "Parameter must be a number bigger than zero"}, 400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_missing_parameter_returns_error(self):
        def test_body():
            self.__assert_endpoint("prime", {"error": "Missing required 'q' parameter"}, 400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_1_correct_result(self):
        def test_body():
            self.__assert_endpoint("prime?q=1", {"is_prime_number": True})
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_2_correct_result(self):
        def test_body():
            self.__assert_endpoint("prime?q=2", {"is_prime_number": True})
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_4_correct_result(self):
        def test_body():
            self.__assert_endpoint("prime?q=4", {"is_prime_number": False})
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_small_random_has_correct_result(self):
        def test_body():
            r = random.randint(10, 100)
            self.__assert_endpoint("prime?q=" + str(r), {"is_prime_number": self.__is_p(r)})
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_big_random_has_correct_result(self):
        def test_body():
            r = random.randint(10000, 100000)
            self.__assert_endpoint("prime?q=" + str(r), {"is_prime_number": self.__is_p(r)})
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

    def __is_p(self, n):
        assert n > 2
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    unittest.main()

