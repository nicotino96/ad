import context
import os
import unittest


class WallAPIEntryModelExistsTestCase(unittest.TestCase):

    def test_entry_model(self):
        models_filename = context.WALL_API_ROOT + "wallrest25app/models.py"
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
            {"line": "class Entry(models.Model):", "found": False},
            {"line": "models.CharField(max_length=140)", "found": False},
            {"line": "models.CharField(max_length=5500)", "found": False},
            {"line": "models.DateTimeField(auto_now=True)", "found": False}
        ]


if __name__ == '__main__':
    unittest.main()
