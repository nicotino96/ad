import bcrypt
import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class IdeAPIRegisterHappyPathTestCase(unittest.TestCase):

    def test_unsupported(self):
        def test_body():
            self.__assert_get_endpoint("v1/users", {"error": "Unsupported HTTP method"}, 405)

        # Run server and run test
        self.__test_with_server_alive(test_body)
    
    def test_success_response(self):
        def test_body():
            request_body = {
                "useremail": "test_" + str(time.time()) + "@test.co.uk",
                "username": "Test User",
                "password": "asdf12345"
            }
            self.__assert_post_endpoint("v1/users", request_body, {"is_registered": True}, 201)

        # Run server and run test
        self.__test_with_server_alive(test_body)
    
    def test_user_added_to_db(self):
        random_email = "test_" + str(time.time()) + "@test.co.uk"
        def send_request():
            request_body = {
                "useremail": random_email,
                "username": "Test User",
                "password": "asdf12345"
            }
            self.__assert_post_endpoint("v1/users", request_body, {"is_registered": True}, 201)

        # Run server and run test
        self.__test_with_server_alive(send_request)
        
        # And now verify DB
        self.assertTrue(os.path.isdir(context.IDEAPI_ROOT + "idearest25app"))
        command = 'sqlite3.exe apis/IdeAPI/db.sqlite3 "SELECT COUNT(e_mail) FROM idearest25app_customuser WHERE e_mail=\'' + random_email + '\'"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]
        self.assertEqual(output.decode('utf8').strip(), "1")

    def test_user_added_to_db_with_correctly_hashed_pw(self):
        random_email = "test_" + str(time.time()) + "@test.co.uk"
        some_pass = "asdf12345greetings"
        def send_request():
            request_body = {
                "useremail": random_email,
                "username": "Test User",
                "password": some_pass
            }
            self.__assert_post_endpoint("v1/users", request_body, {"is_registered": True}, 201)

        # Run server and run test
        self.__test_with_server_alive(send_request)
        
        # And now verify DB
        self.assertTrue(os.path.isdir(context.IDEAPI_ROOT + "idearest25app"))
        command = 'sqlite3.exe apis/IdeAPI/db.sqlite3 "SELECT encrypted_password FROM idearest25app_customuser WHERE e_mail=\'' + random_email + '\'"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]
        db_pass = output.decode('utf8').strip()
        print(db_pass)
        self.assertTrue(bcrypt.checkpw(some_pass.encode('utf8'), db_pass.encode('utf8')))

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
        
    def __assert_post_endpoint(self, endpoint, json_body, json_response, status_code=200):
        response = requests.post("http://localhost:8000/" + endpoint, json=json_body)
        self.assertEqual(response.status_code, status_code)
        self.assertEqual(response.json(), json_response)


if __name__ == '__main__':
    unittest.main()
