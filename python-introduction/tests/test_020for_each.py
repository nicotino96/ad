import context
import unittest
from advanced import loops


class DinoLoopTestCase(unittest.TestCase):

    def test_dino_is_found(self):
        self.assertTrue(loops.find_dino("Triceratops"))
        self.assertTrue(loops.find_dino("Tiranosaurio"))
        self.assertTrue(loops.find_dino("Diplodocus"))
        self.assertTrue(loops.find_dino("Cuellilargo"))
        self.assertTrue(loops.find_dino("Pterodáctilo"))

    def test_dino_is_not_found(self):
        self.assertFalse(loops.find_dino("Homo Habilis"))


if __name__ == '__main__':
    unittest.main()

