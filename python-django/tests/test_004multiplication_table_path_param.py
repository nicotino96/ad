import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class SimpleAPIMultiplicationPathParamEndpointTestCase(unittest.TestCase):

    # FIX-ME: Ideally this would request all 1 to 5, but I'm getting
    # ConnectionRefusedError: [WinError 10061] if requesting more
    # than 1 endpoint per test
    def test_rand_number1to5_produce_correct_http_response(self):
        def test_body():
            choice = random.choice([("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)])
            self.__assert_endpoint("multiplications/" + choice[0], self.__table(choice[1]))
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_rand_number6to10_produce_correct_http_response(self):
        def test_body():
            choice = random.choice([("six", 6), ("seven", 7), ("eight", 8), ("nine", 9), ("ten", 10)])
            self.__assert_endpoint("multiplications/" + choice[0], self.__table(choice[1]))
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_numbers_404_correct_http_response(self):
        def test_body():
            r = "test" + str(random.randint(1, 10000))
            expected = {
                "error": "Number not valid. Only one to ten are supported"
            }
            self.__assert_endpoint("multiplications/" + r, expected, 404)
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
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(json_content, response.json())

    def __table(self, n):
        return list(map(lambda x: (x * n), range(1, 11)))


if __name__ == '__main__':
    unittest.main()
