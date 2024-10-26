import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class DashboardsAPIAllEndpointTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DashboardsAPIAllEndpointTestCase, self).__init__(*args, **kwargs)
        self.r1 = "test_" + str(random.randint(1, 1000))
        self.r2 = "test_" + str(random.randint(1, 1000))

    def setUp(self):
        # Generate fixture file for database
        file = open("test_029get_all_dashboards.json", "w")
        file.write('''
        [
  {
    "model": "dashboard25app.dashboard",
    "pk": 1,
    "fields": {
      "title": "Forocoches",
      "summary": "''' + self.r1 + '''"
    }
  },
  {
    "model": "dashboard25app.dashboard",
    "pk": 2,
    "fields": {
      "title": "Foromotos",
      "summary": "''' + self.r2 + '''"
    }
  }
]
        ''')
        file.close()

    def test_all_dashboards_contains_expected_first_element(self):
        def test_body():
            expected = {
                "id": 1,
                "title": "Forocoches",
                "summary": self.r1,
            }
            self.__assert_endpoint("api/v1/dashboards", expected_json_content=expected, expected_in_json_array=True)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_all_dashboards_contains_expected_second_element(self):
        def test_body():
            expected = {
                "id": 2,
                "title": "Foromotos",
                "summary": self.r2,
            }
            self.__assert_endpoint("api/v1/dashboards", expected_json_content=expected, expected_in_json_array=True)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_029get_all_dashboards.json --noinput", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.DASHBOARD_API_ROOT)
            time.sleep(4)
            proc.send_signal(signal.CTRL_BREAK_EVENT)
            time.sleep(1)
            proc.kill()

        def app_dir_exists():
            return os.path.isdir(context.DASHBOARD_API_ROOT + "dashboard25app")

        self.assertTrue(app_dir_exists())
        t = threading.Thread(target=run_server)
        t.start()
        time.sleep(1)
        block()
        t.join(timeout=6)

    def __assert_endpoint(self, endpoint, expected_json_content=None, expected_in_json_array=False):
        response = requests.get("http://localhost:8000/" + endpoint)
        self.assertEqual(response.status_code, 200)
        if expected_json_content is not None:
            if expected_in_json_array:
                found = False
                for element in response.json():
                    if element == expected_json_content:
                        found = True
                self.assertTrue(found)
            else:
                self.assertEqual(response.json(), expected_json_content)


if __name__ == '__main__':
    unittest.main()

