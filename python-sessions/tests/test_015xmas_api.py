import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class XmasAPIGetPresentsEndpointTestCase(unittest.TestCase):
    
    def test_message_is_correct(self):
        def test_body():
            response = requests.get("http://localhost:8000/v1/wishlist")
            self.assertEqual(response.status_code, 200)
            msg = response.json()["mensaje"]
            print(msg)
        
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_list_is_correct(self):
        def test_body():
            response = requests.get("http://localhost:8000/v1/wishlist")
            self.assertEqual(response.status_code, 200)
            gifts = response.json()["deseos"]
            for r in gifts:
                print(r)
        
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        self.assertTrue(os.path.exists(context.XMAS_API_ROOT))

        def run_server():
            proc = subprocess.Popen("python manage.py runserver ", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.XMAS_API_ROOT)
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
