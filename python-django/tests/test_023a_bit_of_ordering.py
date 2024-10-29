import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class WallAPIOrderingEndpointTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(WallAPIOrderingEndpointTestCase, self).__init__(*args, **kwargs)
        self.r1 = "test_" + str(random.randint(1, 1000))

    def setUp(self):
        # Generate fixture file for database
        file = open("test_023a_bit_of_ordering.json", "w")
        file.write('[{"model": "wallrest25app.entry", "pk": 1, "fields": {"title": "Title1", "content": "Content1", "publication_date": "2022-07-13T10:58:27Z"}}, {"model": "wallrest25app.entry", "pk": 2, "fields": {"title": "Title2", "content": "'+self.r1+'", "publication_date": "2022-07-13T11:04:50Z"}}]')
        file.close()

    def test_first_entry_is_newer_one(self):
        def test_body():
            expected = {
                "title": "Title2",
                "content": self.r1,
                "created": "2022-07-13T11:04:50Z"
            }
            self.__assert_endpoint("entries", expected_json_content=expected, expected_json_array_index=0)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_023a_bit_of_ordering.json --noinput", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.WALL_API_ROOT)
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

    def __assert_endpoint(self, endpoint, client_json=None, expected_json_content=None, expected_status_code=200, expected_json_array_index=None):
        if client_json is None:
            response = requests.get("http://localhost:8000/" + endpoint)
        else:
            response = requests.post("http://localhost:8000/" + endpoint, json=client_json)
        if expected_status_code is not None:
            self.assertEqual(response.status_code, expected_status_code)
        if expected_json_content is not None:
            if expected_json_array_index is not None:
                self.assertEqual(response.json()[expected_json_array_index], expected_json_content)
            else:
                self.assertEqual(response.json(), expected_json_content)


if __name__ == '__main__':
    unittest.main()
