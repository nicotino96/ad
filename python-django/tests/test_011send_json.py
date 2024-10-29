import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class SimpleAPIExamplePostJsonBodyEndpointTestCase(unittest.TestCase):

    def test_correct_json_body_ok_response(self):
        def test_body():
            r = "test" + str(random.randint(1, 1000))
            response = requests.post("http://localhost:8000/resource/19", json={"mood": r})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()["message"], "You have sent a POST to the resource 19 and you're " + r)
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


if __name__ == '__main__':
    unittest.main()
