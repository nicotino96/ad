import context
import signal
import threading
import unittest
import requests
import subprocess
import time


class DefaultDjangoProjectExistsTestCase(unittest.TestCase):

    def test_django_project_exists(self):
        print("I will start another thread to run the server...")
        threading.Thread(target=self.__run_server).start()
        time.sleep(1)
        print("Zzz... I have slept 2 seconds... Let's send an HTTP request!")
        response = requests.get("http://localhost:8000/")
        # 200 after fresh install
        # 404 will take place later when urls.py contains stuff
        self.assertTrue((response.status_code == 200) or (response.status_code == 404))
        print("HTTP request finished and assertions done")

    def __run_server(self):
        # https://pythongeeks.org/subprocess-in-python/
        managepy_location = context.PROJECT_ROOT + "/api/RestAPI/"
        # https://docs.python.org/3/library/subprocess.html?highlight=subprocess#subprocess.Popen.send_signal
        flags = subprocess.CREATE_NEW_PROCESS_GROUP
        print("Thread: Launching manage.py runserver and sleeping 4 seconds")
        proc = subprocess.Popen("python manage.py runserver", creationflags=flags, cwd=managepy_location)
        time.sleep(4)
        print("Thread: Terminating and waiting 1 extra seconds to allow Django to cleanup...")
        proc.send_signal(signal.CTRL_BREAK_EVENT)
        time.sleep(1)
        proc.kill()


if __name__ == '__main__':
    unittest.main()

