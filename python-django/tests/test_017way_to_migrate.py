import context
import os
import subprocess
import unittest


class WallAPIDatabaseFirstEntryTestCase(unittest.TestCase):

    def test_first_sql_row_exists_in_database(self):
        self.assertTrue(os.path.isdir(context.WALL_API_ROOT + "wallrest25app"))
        command = 'sqlite3.exe apis/WallAPI/db.sqlite3 "SELECT id, title, content FROM wallrest25app_entry LIMIT 1"'
        output = subprocess.Popen(command, shell=True, cwd=context.PROJECT_ROOT, stdout=subprocess.PIPE).communicate()[0]
        self.assertEqual(output.decode('utf8').strip(), "1|Hola|Un primer ladrillo en el muro")


if __name__ == '__main__':
    unittest.main()

