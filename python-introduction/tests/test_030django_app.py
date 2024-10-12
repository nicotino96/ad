import context
import os
import signal
import threading
import unittest
import requests
import subprocess
import time


class DjangoFirstViewTestCase(unittest.TestCase):

    def test_django_first_view_is_correct(self):
        self.assertTrue(self.__app_dir_exists())
        threading.Thread(target=self.__run_server).start()
        time.sleep(1)
        response = requests.get("http://localhost:8000/example")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content.decode('utf8').__contains__("Hola a todo el mundo, ahora bien hecho"))

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

