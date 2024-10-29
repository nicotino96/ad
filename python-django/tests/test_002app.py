import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class SimpleAPIHealthEndpointTestCase(unittest.TestCase):

    def test_health_endpoint_has_correct_bool(self):
        def test_body():
            self.__assert_endpoint("health", {"running": True})

        # Tiny check - Was views.py removed?
        self.assertFalse(os.path.exists(context.SIMPLE_API_ROOT + "simplerest25app/views.py"))
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


if __name__ == '__main__':
    unittest.main()
