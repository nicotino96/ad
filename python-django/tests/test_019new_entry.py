import context
import os
import requests
import signal
import subprocess
import threading
import time
import unittest


class WallAPINewEntryEndpointTestCase(unittest.TestCase):

    def setUp(self):
        # Generate fixture file for manage.py testserver argument
        file = open("test_019new_entry.json", "w")
        file.write('[{"model": "wallrest25app.entry", "pk": 1, "fields": {"title": "Title1", "content": "Content1", "publication_date": "2022-07-13T10:58:27Z"}}, {"model": "wallrest25app.entry", "pk": 2, "fields": {"title": "Title2", "content": "Content2", "publication_date": "2022-07-13T11:04:50Z"}}]')
        file.close()
        # Copy settings.py adding TEST DATABASE setting for manage.py testserver argument
        # This will make db.test.sqlite3, which can be used in
        # some tests for verifying added data
        settings_file = open(context.WALL_API_ROOT + "WallAPI/settings.py", 'r')
        modified_settings_file = open(context.WALL_API_ROOT + "WallAPI/settings_test_019new_entry.py", "w")
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

    def test_new_entry_response(self):
        def test_body():
            expected = {"it_was_ok": True}
            client_body = {"new_title": "ATitle", "new_content": "AContent"}
            self.__assert_endpoint("entries", client_json=client_body, expected_json_content=expected, expected_status_code=201)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_new_entry_is_actually_added(self):
        def test_body():
            expected = {"it_was_ok": True}
            client_body = {"new_title": "ATitle2", "new_content": "AContent2"}
            # Send POST
            self.__assert_endpoint("entries", client_json=client_body, expected_json_content=expected, expected_status_code=201)
            # And assert content in DB
            self.__assert_test_database_contains("|ATitle2|AContent2")
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def test_new_entry_response_bad_request(self):
        def test_body():
            client_body = {}
            self.__assert_endpoint("entries", client_json=client_body, expected_status_code=400)
        # Run server and run test
        self.__test_with_server_alive(test_body)

    def __test_with_server_alive(self, block):
        def run_server():
            proc = subprocess.Popen("python manage.py testserver ../../tests/test_019new_entry.json --noinput --settings WallAPI.settings_test_019new_entry", creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, cwd=context.WALL_API_ROOT)
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

    def __assert_test_database_contains(self, string_sqlite_tuple):
        command = 'sqlite3.exe apis/WallAPI/db.test.sqlite3 "SELECT id, title, content FROM wallrest25app_entry"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0].decode('utf8').strip()
        self.assertTrue(output.__contains__(string_sqlite_tuple))

    def tearDown(self):
        temp_settings = os.path.abspath(context.WALL_API_ROOT + "WallAPI/settings_test_019new_entry.py")
        os.remove(temp_settings)
        test_database = os.path.abspath(context.WALL_API_ROOT + "db.test.sqlite3")
        os.remove(test_database)


if __name__ == '__main__':
    unittest.main()
