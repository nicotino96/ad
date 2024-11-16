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
        file = open("test_013post_comment.json", "w")
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
},
{
 "model": "idearest25app.idea",
 "pk": 1,
 "fields": {
  "title": "Idea1",
  "description": "Description1",
  "user": 1,
  "category": 1
 }
}
]
        ''')
        file.close()
        # Copy settings.py adding TEST DATABASE setting for manage.py testserver argument
        # This will make db.test.sqlite3, which can be used in
        # some tests for verifying added data
        settings_file = open(context.IDEAPI_ROOT + "IdeAPI/settings.py", 'r')
        modified_settings_file = open(context.IDEAPI_ROOT + "IdeAPI/settings_test_013post_comment.py", "w")
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
            client_body = {
                "content": "AComment"
            }
            self.__assert_endpoint("v1/ideas/1/comments", client_json=client_body, expected_status_code=401)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_missing_parameter_response(self):
        def test_body():
            client_body = {
                "comment_invalid_key": "AComment",
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/ideas/1/comments", client_json=client_body, client_headers=client_headers, expected_status_code=400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_idea_not_valid_response(self):
        def test_body():
            client_body = {
                "content": "AComment",
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/ideas/5/comments", client_json=client_body, client_headers=client_headers, expected_status_code=404)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_success_response(self):
        def test_body():
            client_body = {
                "content": "AComment"
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/ideas/1/comments", client_json=client_body, client_headers=client_headers, expected_status_code=201)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_comment_is_added(self):
        def test_body():
            client_body = {
                "content": "AComment"
            }
            client_headers = { 'Api-Session-Token': self.random_token }
            self.__assert_endpoint("v1/ideas/1/comments", client_json=client_body, client_headers=client_headers, expected_status_code=201)
        # Run server and run test
        self.__test_with_server_alive(test_body)
        
        # Test DB content
        self.__assert_test_database_contains("|AComment")

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_013post_comment.json --noinput --settings IdeAPI.settings_test_013post_comment", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.IDEAPI_ROOT)
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

    def __assert_endpoint(self, endpoint, client_json=None, client_headers=None, expected_status_code=200):
        if client_json is None:
            response = requests.get("http://localhost:8000/" + endpoint)
        elif client_headers is None:
            response = requests.post("http://localhost:8000/" + endpoint, json=client_json)
        else:
            response = requests.post("http://localhost:8000/" + endpoint, json=client_json, headers=client_headers)
        if expected_status_code is not None:
            self.assertEqual(response.status_code, expected_status_code)

    def __assert_test_database_contains(self, string_sqlite_tuple):
        command = 'sqlite3.exe apis/IdeAPI/db.test.sqlite3 "SELECT id, content FROM idearest25app_comment"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0].decode('utf8').strip()
        self.assertTrue(output.__contains__(string_sqlite_tuple))

    def tearDown(self):
        temp_settings = os.path.abspath(context.IDEAPI_ROOT + "IdeAPI/settings_test_013post_comment.py")
        os.remove(temp_settings)
        test_database = os.path.abspath(context.IDEAPI_ROOT + "db.test.sqlite3")
        os.remove(test_database)


if __name__ == '__main__':
    unittest.main()


