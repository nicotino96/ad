import context
import os
import signal
import threading
import unittest
import requests
import subprocess
import time


class DjangoExampleJSONArrayEndpointTestCase(unittest.TestCase):

    def test_django_json_animals_contains_correct_animal1(self):
        self.assertTrue(self.__app_dir_exists())
        threading.Thread(target=self.__run_server).start()
        time.sleep(1)
        response = requests.get("http://localhost:8000/api/v1/animals")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0], "Foca monje (Monachus monachus)")

    def test_django_json_animals_contains_correct_animal2(self):
        self.assertTrue(self.__app_dir_exists())
        threading.Thread(target=self.__run_server).start()
        time.sleep(1)
        response = requests.get("http://localhost:8000/api/v1/animals")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[1], "Fartet (Aphanius iberus)")

    def test_django_json_animals_contains_correct_animal3(self):
        self.assertTrue(self.__app_dir_exists())
        threading.Thread(target=self.__run_server).start()
        time.sleep(1)
        response = requests.get("http://localhost:8000/api/v1/animals")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[2], "Samaruc (Valencia hispanica)")

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
