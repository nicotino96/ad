import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class WallAPIPaginationEndpointTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(WallAPIPaginationEndpointTestCase, self).__init__(*args, **kwargs)
        self.r1 = "test_" + str(random.randint(1, 1000))
        self.r2 = "test_" + str(random.randint(1, 1000))
        self.r3 = "test_" + str(random.randint(1, 1000))

    def setUp(self):
        # Generate fixture file for database
        file = open("test_025older_than.json", "w")
        file.write('[{"model": "wallrest25app.entry", "pk": 1, "fields": {"title": "Title1", "content": "'+self.r1+'", "publication_date": "2022-07-13T10:58:27Z"}}, {"model": "wallrest25app.entry", "pk": 2, "fields": {"title": "Title2", "content": "'+self.r2+'", "publication_date": "2022-07-13T11:04:50Z"}}, {"model": "wallrest25app.entry", "pk": 3, "fields": {"title": "Title3", "content": "'+self.r3+'", "publication_date": "2022-07-13T11:11:55Z"}}]')
        file.close()

    def test_older_than_alone_works(self):
        def test_body():
            expected1 = {
                "title": "Title2",
                "content": self.r2,
                "created": "2022-07-13T11:04:50Z"
            }
            expected2 = {
                "title": "Title1",
                "content": self.r1,
                "created": "2022-07-13T10:58:27Z"
            }
            response = requests.get("http://localhost:8000/entries?older_than=2022-07-13T11:05:00Z")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 2)
            self.assertEqual(response.json()[0], expected1)
            self.assertEqual(response.json()[1], expected2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_older_than_with_size_works(self):
        def test_body():
            expected1 = {
                "title": "Title2",
                "content": self.r2,
                "created": "2022-07-13T11:04:50Z"
            }
            response = requests.get("http://localhost:8000/entries?older_than=2022-07-13T11:05:00Z&size=1")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 1)
            self.assertEqual(response.json()[0], expected1)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_025older_than.json --noinput", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.WALL_API_ROOT)
            time.sleep(4)
            proc.send_signal(signal.CTRL_BREAK_EVENT)
            time.sleep(1)
            proc.kill()

        def app_dir_exists():
            return os.path.isdir(context.WALL_API_ROOT + "wallrest25app")

        self.assertTrue(app_dir_exists())
        t = threading.Thread(target=run_server)
        t.start()
        time.sleep(1)
        block()
        t.join(timeout=6)


if __name__ == '__main__':
    unittest.main()
