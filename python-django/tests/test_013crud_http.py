import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class SimpleAPICRUDExampleEndpointTestCase(unittest.TestCase):

    def test_animal_method_not_allowed_error_response(self):
        def test_body_get():
            response = requests.get("http://localhost:8000/example")
            self.assertEqual(response.json()["message"], "Reading some data, huh?")

        def test_body_post():
            response = requests.post("http://localhost:8000/example")
            self.assertEqual(response.json()["message"], "This should create a new thing!")

        def test_body_put():
            response = requests.put("http://localhost:8000/example")
            self.assertEqual(response.json()["message"], "You can update any element with this")

        def test_body_delete():
            response = requests.delete("http://localhost:8000/example")
            self.assertEqual(response.json()["message"], "This will remove one or many elements, for sure!")

        # Run server and run test
        self.__test_with_server_alive(test_body_get)
        self.__test_with_server_alive(test_body_post)
        self.__test_with_server_alive(test_body_put)
        self.__test_with_server_alive(test_body_delete)

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


if __name__ == '__main__':
    unittest.main()

