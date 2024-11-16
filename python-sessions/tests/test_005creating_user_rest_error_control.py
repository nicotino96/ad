import bcrypt
import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class IdeAPIRegisterNotHappyPathTestCase(unittest.TestCase):

    def test_missing_param_password(self):
        def test_body():
            request_body_missing_param = {
                "useremail": "test_" + str(time.time()) + "@test.co.uk",
                "username": "Test User",
            }
            self.__assert_post_endpoint("v1/users", request_body_missing_param, {"error": "Missing parameter"}, 400)

        # Run server and run test
        self.__test_with_server_alive(test_body)
    
    def test_missing_param_email(self):
        def test_body():
            request_body_missing_param = {
                "username": "Test User",
                "password": "asdf12345"
            }
            self.__assert_post_endpoint("v1/users", request_body_missing_param, {"error": "Missing parameter"}, 400)

        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_missing_param_username(self):
        def test_body():
            request_body_missing_param = {
                "password": "asdf12345",
                "useremail": "test_" + str(time.time()) + "@test.co.uk",
            }
            self.__assert_post_endpoint("v1/users", request_body_missing_param, {"error": "Missing parameter"}, 400)

        # Run server and run test
        self.__test_with_server_alive(test_body)
    
    def test_email_not_valid_due_to_missing_character(self):
        def test_body():
            request_body_invalid_email = {
                "useremail": "test_" + str(time.time()) + "test.co.uk",
                "username": "Test User",
                "password": "asdf12345"
            }
            self.__assert_post_endpoint("v1/users", request_body_invalid_email, {"error": "Invalid email"}, 400)

        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_email_not_valid_due_to_length_restriction(self):
        def test_body():
            email = "t@"
            length = 7
            for n in range(length - 3):
                email = email + "w"
            request_body_short_email = {
                "useremail": email,
                "username": "Test User",
                "password": "asdf12345"
            }
            self.__assert_post_endpoint("v1/users", request_body_short_email, {"error": "Invalid email"}, 400)

        # Run server and run test
        self.__test_with_server_alive(test_body)
    
    def test_already_registered(self):
        # INSERT an user directly into the DB
        valid_email = "test_" + str(time.time()) + "@test.co.uk"
        self.assertTrue(os.path.isdir(context.IDEAPI_ROOT + "idearest25app"))
        command = 'sqlite3.exe apis/IdeAPI/db.sqlite3 "INSERT INTO idearest25app_customuser (e_mail, username, encrypted_password) VALUES (\'' + valid_email + '\', \'Test User\', \'$2b$12$l2NvEv5Fm7abtLDhWNyKu.pL3orDvp700e8vaLJPfTDKnptWsflV.\')"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]
        
        # Now assert 409
        def send_request():
            request_body = {
                "useremail": valid_email,
                "username": "Test User",
                "password": "asdf12345"
            }
            self.__assert_post_endpoint("v1/users", request_body, {"error": "Already registered"}, 409)

        # Run server and run test
        self.__test_with_server_alive(send_request)


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
        
    def __assert_post_endpoint(self, endpoint, json_body, json_response, status_code=200):
        response = requests.post("http://localhost:8000/" + endpoint, json=json_body)
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.json(), json_response)
      

if __name__ == '__main__':
    unittest.main()
