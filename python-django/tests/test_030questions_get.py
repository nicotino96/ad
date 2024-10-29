import context
import os
import random
import requests
import signal
import subprocess
import threading
import time
import unittest


class DashboardsAPIQuestionsEndpointTestCase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DashboardsAPIQuestionsEndpointTestCase, self).__init__(*args, **kwargs)
        self.r1 = "test_" + str(random.randint(1, 1000))
        self.r2 = "test_" + str(random.randint(1, 1000))
        self.r3 = "test_" + str(random.randint(1, 1000))

    def setUp(self):
        # Generate fixture file for database
        file = open("test_030questions_get.json", "w")
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
    "model": "dashboard25app.dashboard",
    "pk": 2,
    "fields": {
      "title": "Foromotos",
      "summary": "Test"
    }
  },
  {
    "model": "dashboard25app.question",
    "pk": 1,
    "fields": {
      "dashboard": 1,
      "title": "Pitagoras1",
      "summary": "'''+self.r1+'''",
      "publication_date": "2022-07-14T09:59:42.347Z"
    }
  },
  {
    "model": "dashboard25app.question",
    "pk": 2,
    "fields": {
      "dashboard": 1,
      "title": "Pitagoras2",
      "summary": "'''+self.r2+'''",
      "publication_date": "2022-07-14T10:01:42.280Z"
    }
  },
  {
    "model": "dashboard25app.question",
    "pk": 3,
    "fields": {
      "dashboard": 1,
      "title": "Pitagoras3",
      "summary": "'''+self.r3+'''",
      "publication_date": "2022-07-14T10:02:07.941Z"
    }
  },
    {
    "model": "dashboard25app.question",
    "pk": 4,
    "fields": {
      "dashboard": 2,
      "title": "Moto",
      "summary": "Test",
      "publication_date": "2022-07-14T10:02:07.941Z"
    }
  }
]
        ''')
        file.close()

    def test_dashboards2_questions_has_one_question(self):
        def test_body():
            response = requests.get("http://localhost:8000/api/v1/dashboards/2/questions")
            self.assertEqual(len(response.json()), 1)
            self.assertEqual(response.status_code, 200)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_contains_expected_first_element(self):
        def test_body():
            expected = {
                "id": 3,
                "title": "Pitagoras3",
                "summary": self.r3,
                "publication_date": "2022-07-14T10:02:07.941Z"
            }
            self.__assert_endpoint("api/v1/dashboards/1/questions", expected_json_content=expected, expected_json_array_index=0)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_contains_expected_second_element(self):
        def test_body():
            expected = {
                "id": 2,
                "title": "Pitagoras2",
                "summary": self.r2,
                "publication_date": "2022-07-14T10:01:42.280Z"
            }
            self.__assert_endpoint("api/v1/dashboards/1/questions", expected_json_content=expected, expected_json_array_index=1)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_contains_expected_third_element(self):
        def test_body():
            expected = {
                "id": 1,
                "title": "Pitagoras1",
                "summary": self.r1,
                "publication_date": "2022-07-14T09:59:42.347Z"
            }
            self.__assert_endpoint("api/v1/dashboards/1/questions", expected_json_content=expected, expected_json_array_index=2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_size1_contains_expected_first_element(self):
        def test_body():
            expected = {
                "id": 3,
                "title": "Pitagoras3",
                "summary": self.r3,
                "publication_date": "2022-07-14T10:02:07.941Z"
            }
            response = requests.get("http://localhost:8000/api/v1/dashboards/1/questions?size=1")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 1)
            self.assertEqual(response.json()[0], expected)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_size5_contains_expected_elements(self):
        def test_body():
            expected1 = {
                "id": 3,
                "title": "Pitagoras3",
                "summary": self.r3,
                "publication_date": "2022-07-14T10:02:07.941Z"
            }
            expected2 = {
                "id": 2,
                "title": "Pitagoras2",
                "summary": self.r2,
                "publication_date": "2022-07-14T10:01:42.280Z"
            }
            expected3 = {
                "id": 1,
                "title": "Pitagoras1",
                "summary": self.r1,
                "publication_date": "2022-07-14T09:59:42.347Z"
            }
            response = requests.get("http://localhost:8000/api/v1/dashboards/1/questions?size=5")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 3)
            self.assertEqual(response.json()[0], expected1)
            self.assertEqual(response.json()[1], expected2)
            self.assertEqual(response.json()[2], expected3)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_size400(self):
        def test_body():
            response = requests.get("http://localhost:8000/api/v1/dashboards/1/questions?size=nooo")
            self.assertEqual(response.status_code, 400)

        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_older_than1_contains_expected_two_elements(self):
        def test_body():
            expected1 = {
                "id": 2,
                "title": "Pitagoras2",
                "summary": self.r2,
                "publication_date": "2022-07-14T10:01:42.280Z"
            }
            expected2 = {
                "id": 1,
                "title": "Pitagoras1",
                "summary": self.r1,
                "publication_date": "2022-07-14T09:59:42.347Z"
            }
            response = requests.get("http://localhost:8000/api/v1/dashboards/1/questions?before=2022-07-14T10:02:07.941Z")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 2)
            self.assertEqual(response.json()[0], expected1)
            self.assertEqual(response.json()[1], expected2)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_older_than2_contains_expected_last_element(self):
        def test_body():
            expected = {
                "id": 1,
                "title": "Pitagoras1",
                "summary": self.r1,
                "publication_date": "2022-07-14T09:59:42.347Z"
            }
            response = requests.get("http://localhost:8000/api/v1/dashboards/1/questions?before=2022-07-14T10:01:42.280Z")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 1)
            self.assertEqual(response.json()[0], expected)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_dashboards1_questions_older_than2_size1_contains_expected_middle_element(self):
        def test_body():
            expected = {
                "id": 2,
                "title": "Pitagoras2",
                "summary": self.r2,
                "publication_date": "2022-07-14T10:01:42.280Z"
            }
            response = requests.get("http://localhost:8000/api/v1/dashboards/1/questions?before=2022-07-14T10:02:07.941Z&size=1")
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json()), 1)
            self.assertEqual(response.json()[0], expected)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_030questions_get.json --noinput", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.DASHBOARD_API_ROOT)
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

