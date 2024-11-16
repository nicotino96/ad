import context
import os
import requests
import secrets
import signal
import subprocess
import threading
import time
import unittest


class IdeAPIPostIdeaEndpointTestCase(unittest.TestCase):
    random_token = secrets.token_hex(10)

    def setUp(self):
        # Generate fixture file for manage.py testserver argument
        file = open("test_011post_idea.json", "w")
        file.write('''[
{
 "model": "idearest25app.category",
 "pk": 1,
 "fields": {
  "title": "Cat1"
 }
},
{
 "model": "idearest25app.customuser",
 "pk": 1,
 "fields": {
  "e_mail": "''' + "test_" + str(time.time()) + "@test.co.uk" + '''",
  "username": "Test User",
  "encrypted_password": "$2b$12$Re22Ht4N5pZxrLGEgZcy..ZmrycSInMpWE.Lk6BYcYyw7OufwzvBS"
 }
},
{
 "model": "idearest25app.usersession",
 "pk": 1,
 "fields": {
  "creator": 1,
  "token": "''' + self.random_token + '''"
 }
}
]
        ''')
        file.close()
        # Copy settings.py adding TEST DATABASE setting for manage.py testserver argument
        # This will make db.test.sqlite3, which can be used in
        # some tests for verifying added data
        settings_file = open(context.IDEAPI_ROOT + "IdeAPI/settings.py", 'r')
        modified_settings_file = open(context.IDEAPI_ROOT + "IdeAPI/settings_test_011post_idea.py", "w")
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

    def test_new_idea_unauthenticated_response(self):
        def test_body():
            expected = {"error": "Authentication not valid"}
            client_body = {
                "new_idea_title": "ATitle",
                "description": "AContent"
            }
            self.__assert_endpoint("v1/categories/1/ideas", client_json=client_body, expected_json_content=expected, expected_status_code=401)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_missing_parameter_response(self):
        def test_body():
            expected = {"error": "You are missing a parameter"}
            client_body = {
                "new_idea_title": "ATitle",
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/categories/1/ideas", client_json=client_body, client_headers=client_headers, expected_json_content=expected, expected_status_code=400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_category_not_valid_response(self):
        def test_body():
            expected = {"error": "Category not found"}
            client_body = {
                "new_idea_title": "ATitle",
                "description": "AContent"
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/categories/2/ideas", client_json=client_body, client_headers=client_headers, expected_json_content=expected, expected_status_code=404)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_success_response(self):
        def test_body():
            expected = {"success": True}
            client_body = {
                "new_idea_title": "ATitle",
                "description": "AContent"
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/categories/1/ideas", client_json=client_body, client_headers=client_headers, expected_json_content=expected, expected_status_code=201)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_idea_is_added(self):
        def test_body():
            expected = {"success": True}
            client_body = {
                "new_idea_title": "ATitle",
                "description": "AContent"
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/categories/1/ideas", client_json=client_body, client_headers=client_headers, expected_json_content=expected, expected_status_code=201)
        # Run server and run test
        self.__test_with_server_alive(test_body)
        # Test DB content
        self.__assert_test_database_contains("|ATitle|AContent")

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_011post_idea.json --noinput --settings IdeAPI.settings_test_011post_idea", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.IDEAPI_ROOT)
            time.sleep(4)
            proc.send_signal(signal.CTRL_BREAK_EVENT)
            time.sleep(1)
            proc.kill()

        def app_dir_exists():
            return os.path.isdir(context.IDEAPI_ROOT + "idearest25app")

        self.assertTrue(app_dir_exists())
        t = threading.Thread(target=run_server)
        t.start()
        time.sleep(1)
        block()
        t.join(timeout=6)

    def __assert_endpoint(self, endpoint, client_json=None, client_headers=None, expected_json_content=None, expected_status_code=200):
        if client_json is None:
            response = requests.get("http://localhost:8000/" + endpoint)
        elif client_headers is None:
            response = requests.post("http://localhost:8000/" + endpoint, json=client_json)
        else:
            response = requests.post("http://localhost:8000/" + endpoint, json=client_json, headers=client_headers)
        if expected_status_code is not None:
            self.assertEqual(response.status_code, expected_status_code)
        if expected_json_content is not None:
            self.assertEqual(response.json(), expected_json_content)

    def __assert_test_database_contains(self, string_sqlite_tuple):
        command = 'sqlite3.exe apis/IdeAPI/db.test.sqlite3 "SELECT id, title, description FROM idearest25app_idea"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0].decode('utf8').strip()
        self.assertTrue(output.__contains__(string_sqlite_tuple))

    def tearDown(self):
        temp_settings = os.path.abspath(context.IDEAPI_ROOT + "IdeAPI/settings_test_011post_idea.py")
        os.remove(temp_settings)
        test_database = os.path.abspath(context.IDEAPI_ROOT + "db.test.sqlite3")
        os.remove(test_database)


if __name__ == '__main__':
    unittest.main()

