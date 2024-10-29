import context
import unittest

class RecapTestCase(unittest.TestCase):

    def test_dev_has_finished(self):
        developer_learned_a_lot = True
        self.assertTrue(developer_learned_a_lot)


if __name__ == '__main__':
    unittest.main()
