import context
import os
import subprocess
import unittest


class IdeAPICustomUserModelTestCase(unittest.TestCase):

    def test_db_was_migrated(self):
        self.assertTrue(os.path.isdir(context.IDEAPI_ROOT + "idearest25app"))
        command = 'sqlite3.exe apis/IdeAPI/db.sqlite3 "SELECT COUNT(e_mail) FROM idearest25app_customuser WHERE id=-1"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]
        self.assertEqual(output.decode('utf8').strip(), "0")

    def test_custom_user_model(self):
        models_filename = context.IDEAPI_ROOT + "idearest25app/models.py"
        self.assertTrue(os.path.exists(models_filename))

        expected = self.__expected_lines_content()
        models_file = open(models_filename, 'r')
        lines = models_file.readlines()
        for line in lines:
            for i in range(len(expected)):
                if line.strip().__contains__(expected[i]["line"]):
                    expected[i]["found"] = True
        models_file.close()
        for expected_line in expected:
            self.assertTrue(expected_line["found"], "This TEST is a bit picky. You have to ensure that the following line is EXACTLY CONTAINED in your models.py: " + expected_line["line"] + " Please, verify your whitespaces")

    def __expected_lines_content(self):
        # Pretty lame way of inspecting models
        # Other options are:
        # * django.setup() and import models directly
        # * makemigrations --dry-run and check migrations
        # But I choose this simple yet hacky solution
        return [
            {"line": "class CustomUser(models.Model):", "found": False},
            {"line": "models.CharField(max_length=290, unique=True)", "found": False},
            {"line": "models.CharField(max_length=200)", "found": False},
            {"line": "models.CharField(max_length=120)", "found": False}
        ]


if __name__ == '__main__':
    unittest.main()
