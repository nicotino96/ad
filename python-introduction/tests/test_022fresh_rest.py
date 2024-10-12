import context
import unittest


class RestTestCase(unittest.TestCase):

    def test_dev_has_rested(self):
        mind_of_developer_is_in_peace = True
        self.assertTrue(mind_of_developer_is_in_peace)


if __name__ == '__main__':
    unittest.main()
