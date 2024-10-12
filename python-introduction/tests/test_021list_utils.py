import context
import io
import random
import unittest
from unittest.mock import patch
from advanced import loops


class ListUtilsTestCase(unittest.TestCase):

    def test_dino2_is_ok(self):
        self.assertTrue(loops.find_dino2("Triceratops"))
        self.assertTrue(loops.find_dino2("Diplodocus"))
        self.assertTrue(loops.find_dino2("Pterodáctilo"))
        self.assertFalse(loops.find_dino2("Molusco"))

    def test_len_example_correct_output(self):
        s = len([None, None, None, None, None])
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            loops.example_list_size()
            self.assertTrue(fake_out.getvalue().__contains__("El tamaño de la primera lista es: 2"))
            self.assertTrue(fake_out.getvalue().__contains__("El tamaño de la segunda lista es: " + str(s)))
            self.assertTrue(fake_out.getvalue().__contains__("El tamaño de la tercera lista es: 2"))

    def test_retrieve_value_correct_returned_value(self):
        self.assertEqual(loops.retrieve_value(0), 4)
        self.assertEqual(loops.retrieve_value(1), 8)
        self.assertEqual(loops.retrieve_value(2), -35)
        self.assertEqual(loops.retrieve_value(3), "Pepe Depura")
        self.assertEqual(loops.retrieve_value(4), 12)
        self.assertEqual(loops.retrieve_value(random.randint(200, 300)), None)


if __name__ == '__main__':
    unittest.main()
