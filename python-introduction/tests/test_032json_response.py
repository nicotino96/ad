import context
import os
import signal
import threading
import unittest
import requests
import subprocess
import time


class DjangoExampleJSONEndpointTestCase(unittest.TestCase):

    def test_django_json_example_endpoint_has_correct_bool(self):
        self.assertTrue(self.__app_dir_exists())
        threading.Thread(target=self.__run_server).start()
        time.sleep(1)
        response = requests.get("http://localhost:8000/api/v1/example")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["ok"], True)

    def test_django_json_example_endpoint_has_correct_msg(self):
        self.assertTrue(self.__app_dir_exists())
        threading.Thread(target=self.__run_server).start()
        time.sleep(1)
        response = requests.get("http://localhost:8000/api/v1/example")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Todo correcto")

    def __run_server(self):
        # https://pythongeeks.org/subprocess-in-python/
        managepy_location = context.PROJECT_ROOT + "/api/RestAPI/"
        # https://docs.python.org/3/library/subprocess.html?highlight=subprocess#subprocess.Popen.send_signal
        flags = subprocess.CREATE_NEW_PROCESS_GROUP
        proc = subprocess.Popen("python manage.py runserver", creationflags=flags, cwd=managepy_location)
        time.sleep(4)
        proc.send_signal(signal.CTRL_BREAK_EVENT)
        time.sleep(1)
        proc.kill()

    def __app_dir_exists(self):
        return os.path.isdir(context.PROJECT_ROOT + "/api/RestAPI/webservice25app")


if __name__ == '__main__':
    unittest.main()

