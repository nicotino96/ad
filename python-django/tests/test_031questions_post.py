import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class DashboardsAPINewQuestionEndpointTestCase(unittest.TestCase):

    def setUp(self):
        # Generate fixture file for manage.py testserver argument
        file = open("test_031questions_post.json", "w")
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
          }
        ]
                ''')
        file.close()
        # Copy settings.py adding TEST DATABASE setting for manage.py testserver argument
        # This will make db.test.sqlite3, which can be used in
        # some tests for verifying added data
        settings_file = open(context.DASHBOARD_API_ROOT + "DashboardAPI/settings.py", 'r')
        modified_settings_file = open(context.DASHBOARD_API_ROOT + "DashboardAPI/settings_test_031questions_post.py", "w")
        lines = settings_file.readlines()
        for line in lines:
            modified_settings_file.write(line)
            # Hacky condition to insert line
            if line.__contains__('NAME') and line.__contains__('db.sqlite3'):
                modified_settings_file.write("        'TEST': {\n")
                modified_settings_file.write("            'NAME': BASE_DIR / 'db.test.sqlite3',\n")
                modified_settings_file.write("        },\n")
        settings_file.close()
        modified_settings_file.close()

    def test_new_question_response(self):
        def test_body():
            client_body = {"title": "New Question", "summary": "A Question"}
            self.__assert_endpoint("api/v1/dashboards/1/questions", client_json=client_body, expected_status_code=201)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_new_question_is_actually_adde1(self):
        def test_body():
            client_body = {"title": "New Question", "summary": "A Question"}
            # Send POST
            self.__assert_endpoint("api/v1/dashboards/1/questions", client_json=client_body, expected_status_code=201)
            # And assert content in DB
            self.__assert_test_database_contains("SELECT id, title, summary FROM dashboard25app_question WHERE dashboard_id=1", "|New Question|A Question")
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_new_question_is_actually_added2(self):
        def test_body():
            client_body = {"title": "New Question2", "summary": "A Question2"}
            # Send POST
            self.__assert_endpoint("api/v1/dashboards/2/questions", client_json=client_body, expected_status_code=201)
            # And assert content in DB
            self.__assert_test_database_contains("SELECT id, title, summary FROM dashboard25app_question WHERE dashboard_id=2", "|New Question2|A Question2")
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_new_question_response_bad_request(self):
        def test_body():
            self.__assert_endpoint("api/v1/dashboards/2/questions", client_json={}, expected_status_code=400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_031questions_post.json --noinput --settings DashboardAPI.settings_test_031questions_post", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.DASHBOARD_API_ROOT)
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

    def __assert_endpoint(self, endpoint, client_json=None, expected_status_code=200):
        if client_json is None:
            response = requests.get("http://localhost:8000/" + endpoint)
        else:
            response = requests.post("http://localhost:8000/" + endpoint, json=client_json)
        if expected_status_code is not None:
            self.assertEqual(response.status_code, expected_status_code)

    def __assert_test_database_contains(self, sql_command, string_sqlite_tuple):
        command = 'sqlite3.exe apis/DashboardAPI/db.test.sqlite3 "' + sql_command + '"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0].decode('utf8').strip()
        self.assertTrue(output.__contains__(string_sqlite_tuple))

    def tearDown(self):
        temp_settings = os.path.abspath(context.DASHBOARD_API_ROOT + "DashboardAPI/settings_test_031questions_post.py")
        os.remove(temp_settings)
        test_database = os.path.abspath(context.DASHBOARD_API_ROOT + "db.test.sqlite3")
        os.remove(test_database)


if __name__ == '__main__':
    unittest.main()
