import bcrypt
import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class IdeAPILoginHappyPathTestCase(unittest.TestCase):
    result_token = None

    def test_unsupported(self):
        def test_body():
            self.__assert_get_endpoint("v1/sessions", {"error": "HTTP method unsupported"}, 405)

        # Run server and run test
        self.__test_with_server_alive(test_body)
    
    def test_success_response(self):
        # INSERT an user directly into the DB
        valid_email = "test_" + str(time.time()) + "@test.co.uk"
        valid_pass = "asdf5568"
        hashed = bcrypt.hashpw(valid_pass.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        self.assertTrue(os.path.isdir(context.IDEAPI_ROOT + "idearest25app"))
        command = 'sqlite3.exe apis/IdeAPI/db.sqlite3 "INSERT INTO idearest25app_customuser (e_mail, username, encrypted_password) VALUES (\'' + valid_email + '\', \'Test User\', \'' + hashed + '\')"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]

        def test_body():
            def assert_response_body(response):
                self.assertTrue(response.get('token', None) is not None)

            request_body = {
                "login_email": valid_email,
                "login_password": valid_pass
            }
            self.__assert_post_endpoint("v1/sessions", request_body, assert_response_body_fn=assert_response_body, status_code=201)

        # Run server and run test
        self.__test_with_server_alive(test_body)
    
    def test_session_added_to_db(self):
        # INSERT an user directly into the DB
        valid_email = "test_" + str(time.time()) + "@test.co.uk"
        valid_pass = "asdf5568"
        hashed = bcrypt.hashpw(valid_pass.encode('utf8'), bcrypt.gensalt()).decode('utf8')
        self.assertTrue(os.path.isdir(context.IDEAPI_ROOT + "idearest25app"))
        command = 'sqlite3.exe apis/IdeAPI/db.sqlite3 "INSERT INTO idearest25app_customuser (e_mail, username, encrypted_password) VALUES (\'' + valid_email + '\', \'Test User\', \'' + hashed + '\')"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]

        def test_body():
            def assert_response_body(response):
                self.assertTrue(response.get('token', None) is not None)
                self.result_token = response['token']

            request_body = {
                "login_email": valid_email,
                "login_password": valid_pass
            }
            self.__assert_post_endpoint("v1/sessions", request_body, assert_response_body_fn=assert_response_body, status_code=201)

        # Run server and run test
        self.__test_with_server_alive(test_body)
        
        # And now verify DB
        self.assertTrue(os.path.isdir(context.IDEAPI_ROOT + "idearest25app"))
        command = 'sqlite3.exe apis/IdeAPI/db.sqlite3 "SELECT COUNT(token) FROM idearest25app_usersession WHERE token=\'' + self.result_token + '\'"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]
        self.assertEqual(output.decode('utf8').strip(), "1")

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py runserver", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.IDEAPI_ROOT)
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

    def __assert_get_endpoint(self, endpoint, json_content, status_code=200):
        response = requests.get("http://localhost:8000/" + endpoint)
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.json(), json_content)
        
    def __assert_post_endpoint(self, endpoint, json_body, json_response=None, assert_response_body_fn=None, status_code=200):
        response = requests.post("http://localhost:8000/" + endpoint, json=json_body)
        self.assertEqual(response.status_code, status_code)
        if json_response is not None:
            self.assertEqual(response.json(), json_response)
        if assert_response_body_fn is not None:
            assert_response_body_fn(response.json())


if __name__ == '__main__':
    unittest.main()
