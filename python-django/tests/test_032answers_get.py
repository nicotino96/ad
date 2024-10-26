import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class DashboardsAPIAnswersEndpointTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DashboardsAPIAnswersEndpointTestCase, self).__init__(*args, **kwargs)
        self.r1 = "test_" + str(random.randint(1, 1000))
        self.r2 = "test_" + str(random.randint(1, 1000))
        self.r3 = "test_" + str(random.randint(1, 1000))

    def setUp(self):
        # Generate fixture file for database
        file = open("test_032answers_get.json", "w")
        file.write('''
        [
  {
    "model": "dashboard25app.dashboard",
    "pk": 1,
    "fields": {
      "title": "Forocoches",
      "summary": "Test"
    }
  },
  {
    "model": "dashboard25app.question",
    "pk": 1,
    "fields": {
      "dashboard": 1,
      "title": "Pitagoras1",
      "summary": "Test1",
      "publication_date": "2022-07-14T09:59:42.347Z"
    }
  },
  {
    "model": "dashboard25app.question",
    "pk": 2,
    "fields": {
      "dashboard": 1,
      "title": "Pitagoras2",
      "summary": "Test2",
      "publication_date": "2022-07-14T10:01:42.280Z"
    }
  },
  {
    "model": "dashboard25app.answer",
    "pk": 1,
    "fields": {
      "question": 2,
      "description": "'''+self.r1+'''",
      "publication_date": "2022-07-14T10:03:10.516Z"
    }
  },
  {
    "model": "dashboard25app.answer",
    "pk": 2,
    "fields": {
      "question": 2,
      "description": "'''+self.r2+'''",
      "publication_date": "2022-07-14T10:03:20.062Z"
    }
  },
  {
    "model": "dashboard25app.answer",
    "pk": 3,
    "fields": {
      "question": 2,
      "description": "'''+self.r3+'''",
      "publication_date": "2022-07-14T10:03:30.330Z"
    }
  },
  {
    "model": "dashboard25app.answer",
    "pk": 4,
    "fields": {
      "question": 1,
      "description": "Test",
      "publication_date": "2022-07-14T10:03:30.330Z"
    }
  }
]
        ''')
        file.close()

    def test_question1answers_has_one_element(self):
        def test_body():
            response = requests.get("http://localhost:8000/api/v1/questions/1/answers")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 1)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_question2answers_contains_expected_first_element(self):
        def test_body():
            expected = {
                "summary": self.r3,
                "publication_date": "2022-07-14T10:03:30.330Z"
            }
            self.__assert_endpoint("api/v1/questions/2/answers", expected_json_content=expected, expected_json_array_index=0)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_question2answers_contains_expected_second_element(self):
        def test_body():
            expected = {
                "summary": self.r2,
                "publication_date": "2022-07-14T10:03:20.062Z"
            }
            self.__assert_endpoint("api/v1/questions/2/answers", expected_json_content=expected, expected_json_array_index=1)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_question2answers_contains_expected_third_element(self):
        def test_body():
            expected = {
                "summary": self.r1,
                "publication_date": "2022-07-14T10:03:10.516Z"
            }
            self.__assert_endpoint("api/v1/questions/2/answers", expected_json_content=expected, expected_json_array_index=2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_032answers_get.json --noinput", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.DASHBOARD_API_ROOT)
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

    def __assert_endpoint(self, endpoint, expected_json_content=None, expected_json_array_index=None):
        response = requests.get("http://localhost:8000/" + endpoint)
        self.assertEqual(response.status_code, 200)
        if expected_json_content is not None:
            if expected_json_array_index is not None:
                self.assertEqual(response.json()[expected_json_array_index], expected_json_content)
            else:
                self.assertEqual(response.json(), expected_json_content)


if __name__ == '__main__':
    unittest.main()
