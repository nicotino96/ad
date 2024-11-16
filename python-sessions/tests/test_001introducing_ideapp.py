import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class IdeAPIProjectExistsTestCase(unittest.TestCase):

    def test_django_project_exists(self):
        def test_body():
            response = requests.get("http://localhost:8000/")
            # 200 after fresh install
            # 404 will take place later when urls.py contains stuff
            self.assertTrue((response.status_code == 200) or (response.status_code == 404))

        # Tiny check - Does project folder actually exist?
        self.assertTrue(os.path.exists(context.IDEAPI_ROOT))
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py runserver", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.IDEAPI_ROOT)
            time.sleep(4)
            proc.send_signal(signal.CTRL_BREAK_EVENT)
            time.sleep(1)
            proc.kill()

        t = threading.Thread(target=run_server)
        t.start()
        time.sleep(1)
        block()
        t.join(timeout=6)


if __name__ == '__main__':
    unittest.main()
